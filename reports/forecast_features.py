import sqlite3
import pandas as pd

conn = sqlite3.connect("database/carbon.db")

query = """

SELECT

    p.project_id,
    p.country,
    p.project_name,

    d.project_creation_date,
    d.project_start_date,

    s.project_status,
    s.issued_credits,
    s.last_status_changed

FROM projects p

LEFT JOIN project_details d
ON p.project_id = d.project_id

LEFT JOIN project_snapshots s
ON p.project_id = s.project_id

"""

df = pd.read_sql(query, conn)

df = (
    df.sort_values(
        "issued_credits",
        ascending=False
    )
    .drop_duplicates(
        "project_id"
    )
)

# =====================================================
# DOCUMENT COUNTS
# =====================================================

docs = pd.read_sql("""
SELECT
    project_id,
    document_type,
    upload_date
FROM project_documents
""", conn)

document_counts = (
    docs.groupby("project_id")
    .size()
    .reset_index(
        name="document_count"
    )
)

df = df.merge(
    document_counts,
    on="project_id",
    how="left"
)

feature_map = {

    "TREES Concept":
        "concept_docs",

    "TREES Monitoring Report - Public Comment":
        "monitoring_public_docs",

    "TREES Monitoring Report - Verified":
        "monitoring_verified_docs",

    "TREES Validation Report":
        "validation_docs",

    "TREES Verification Report":
        "verification_reports",

    "TREES Verification Opinion":
        "verification_opinions",

    "Host Country Letter of Authorization":
        "host_country_letters",

    "Annual Report to UNFCCC reporting Corresponding Adjustment":
        "corresponding_adjustments",

    "CATS Cancellation Certificate":
        "cancellation_certificates",

    "FCPF Supporting Documents":
        "fcpf_documents"
}

for doc_type, feature_name in feature_map.items():

    temp = (
        docs[
            docs["document_type"] == doc_type
        ]
        .groupby("project_id")
        .size()
        .reset_index(
            name=feature_name
        )
    )

    df = df.merge(
        temp,
        on="project_id",
        how="left"
    )

for col in feature_map.values():

    df[col] = (
        df[col]
        .fillna(0)
    )

df["document_count"] = (
    df["document_count"]
    .fillna(0)
)

# =====================================================
# DATES
# =====================================================

today = pd.Timestamp.today()

df["project_start_date"] = pd.to_datetime(
    df["project_start_date"],
    errors="coerce"
)

df["project_age_years"] = (
    (
        today -
        df["project_start_date"]
    ).dt.days
    / 365.25
).round(1)

# =====================================================
# LAST DOCUMENT
# =====================================================

last_doc = (
    docs.groupby("project_id")
    ["upload_date"]
    .max()
    .reset_index()
)

last_doc["upload_date"] = pd.to_datetime(
    last_doc["upload_date"]
)

last_doc.rename(
    columns={
        "upload_date":
        "last_document_date"
    },
    inplace=True
)

df = df.merge(
    last_doc,
    on="project_id",
    how="left"
)

df["days_since_last_document"] = (

    today -
    df["last_document_date"]

).dt.days

# =====================================================
# STATUS CHANGE
# =====================================================

df["last_status_changed"] = pd.to_datetime(
    df["last_status_changed"],
    errors="coerce",
    utc=True
)

df["days_since_status_change"] = (

    pd.Timestamp.now(
        tz="UTC"
    )

    -

    df["last_status_changed"]

).dt.days

# =====================================================
# FLAGS
# =====================================================

df["has_monitoring"] = (
    df["monitoring_verified_docs"] > 0
).astype(int)

df["has_validation"] = (
    df["validation_docs"] > 0
).astype(int)

df["has_verification"] = (
    df["verification_reports"] > 0
).astype(int)

df["has_host_country_letter"] = (
    df["host_country_letters"] > 0
).astype(int)

df["has_corresponding_adjustment"] = (
    df["corresponding_adjustments"] > 0
).astype(int)

df["has_cancellation_certificate"] = (
    df["cancellation_certificates"] > 0
).astype(int)

# =====================================================
# TARGETS
# =====================================================

df["is_issued"] = (
    df["issued_credits"] > 0
).astype(int)

# =====================================================
# STAGE ENGINE
# =====================================================

def determine_stage(row):

    if row["issued_credits"] > 0:
        return "Issued"

    if row["verification_reports"] > 0:
        return "Verification"

    if row["validation_docs"] > 0:
        return "Validation"

    if row["monitoring_verified_docs"] > 0:
        return "Monitoring"

    return "Concept"

df["current_stage"] = (
    df.apply(
        determine_stage,
        axis=1
    )
)

stage_score_map = {

    "Concept": 1,
    "Monitoring": 2,
    "Validation": 3,
    "Verification": 4,
    "Issued": 5

}

df["stage_score"] = (
    df["current_stage"]
    .map(stage_score_map)
)

# =====================================================
# MOMENTUM
# =====================================================

df["verification_activity"] = (

    df["verification_reports"]

    +

    df["verification_opinions"]

)

df["documentation_density"] = (

    df["document_count"]

    /

    df["project_age_years"]

).fillna(0)

# =====================================================
# COUNTRY FEATURES
# =====================================================

country_features = (

    df.groupby("country")

    .agg(

        country_project_count=(
            "project_id",
            "count"
        ),

        country_total_credits=(
            "issued_credits",
            "sum"
        ),

        country_avg_stage_score=(
            "stage_score",
            "mean"
        ),

        country_avg_document_count=(
            "document_count",
            "mean"
        )

    )

    .reset_index()

)

df = df.merge(
    country_features,
    on="country",
    how="left"
)

# =====================================================
# EXCEL
# =====================================================

df["last_status_changed"] = (
    df["last_status_changed"]
    .dt.tz_localize(None)
)

df.to_excel(
    "data/Forecast_Features.xlsx",
    index=False
)

print(df.head())

conn.close()

print(
    "Forecast Features exported"
)