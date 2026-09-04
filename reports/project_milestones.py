import sqlite3
import pandas as pd
from datetime import datetime

conn = sqlite3.connect("database/carbon.db")

query = """
SELECT
    p.project_id,
    p.project_name,
    p.country,
    s.issued_credits,
    d.document_type,
    d.upload_date

FROM projects p

LEFT JOIN project_snapshots s
    ON p.project_id = s.project_id

LEFT JOIN project_documents d
    ON p.project_id = d.project_id
"""

df = pd.read_sql(query, conn)

def milestone_score(group):

    score = 0
    milestone = "Unknown"
    milestone_date = None

    docs = set(group["document_type"].dropna())

    if "TREES Concept" in docs:
        score = 1
        milestone = "Concept"

    if "TREES Registration Document - Public Comment" in docs:
        score = 2
        milestone = "Registration"

    if "TREES Monitoring Report - Public Comment" in docs:
        score = 3
        milestone = "Monitoring"

    credits = group["issued_credits"].max()

    if credits > 0:
        score = 4
        milestone = "Issued"

    if "CATS Cancellation Certificate" in docs:
        score = 5
        milestone = "Cancelled"

    milestone_dates = group[
        group["document_type"].notna()
    ]["upload_date"]

    if len(milestone_dates) > 0:
        milestone_date = milestone_dates.max()

    return pd.Series({
        "country": group["country"].iloc[0],
        "project_name": group["project_name"].iloc[0],
        "issued_credits": credits,
        "milestone": milestone,
        "score": score,
        "milestone_date": milestone_date
    })

milestones = (
    df.groupby("project_id")
      .apply(milestone_score)
      .reset_index()
)

today = pd.Timestamp.today()

milestones["milestone_date"] = pd.to_datetime(
    milestones["milestone_date"],
    errors="coerce"
)

milestones["days_since_milestone"] = (
    today - milestones["milestone_date"]
).dt.days

milestones = milestones.sort_values(
    ["score", "days_since_milestone"],
    ascending=[False, True]
)

print(milestones)

milestones.to_excel(
    "data/Project_Milestones.xlsx",
    index=False
)

conn.close()

print("Project milestones exported")