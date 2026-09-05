import pandas as pd

# =====================================================
# LOAD FILES
# =====================================================

projects = pd.read_excel(
    "data/Forecast_Projects.xlsx"
)

features = pd.read_excel(
    "data/Forecast_Features.xlsx"
)

# =====================================================
# DATES
# =====================================================

projects["predicted_issue_date"] = pd.to_datetime(
    projects["predicted_issue_date"]
)

# =====================================================
# CURRENT COUNTRY CREDIT TOTALS
# =====================================================

country_totals = (

    features.groupby("country")

    .agg(

        current_credits=(
            "issued_credits",
            "sum"
        )

    )

    .reset_index()

)

# =====================================================
# COUNTRY EVENT FORECASTS
# =====================================================

country_events = (

    projects.groupby(
        [
            "country",
            "forecast_event",
            "predicted_issue_date"
        ]
    )

    .agg(

        predicted_new_credits=(
            "predicted_credits",
            "sum"
        ),

        confidence=(
            "confidence",
            "mean"
        ),

        projects_contributing=(
            "project_id",
            "nunique"
        )

    )

    .reset_index()

)

# =====================================================
# MERGE CURRENT TOTALS
# =====================================================

country_events = country_events.merge(

    country_totals,

    on="country",

    how="left"

)

# =====================================================
# SORT EVENTS
# =====================================================

country_events = country_events.sort_values(

    [
        "country",
        "predicted_issue_date"
    ]

)

# =====================================================
# RUNNING FUTURE TOTALS
# =====================================================

country_events["predicted_total_credits"] = (

    country_events.groupby("country")

    ["predicted_new_credits"]

    .cumsum()

    +

    country_events["current_credits"]

)

# =====================================================
# ROUND CONFIDENCE
# =====================================================

country_events["confidence"] = (

    country_events["confidence"]

    .round(1)

)

# =====================================================
# FORMAT DATES
# =====================================================

country_events["predicted_issue_date"] = (

    country_events["predicted_issue_date"]

    .dt.strftime("%Y-%m-%d")

)

# =====================================================
# FINAL COLUMN ORDER
# =====================================================

country_events = country_events[

    [

        "country",

        "forecast_event",

        "predicted_issue_date",

        "projects_contributing",

        "confidence",

        "current_credits",

        "predicted_new_credits",

        "predicted_total_credits"

    ]

]

# =====================================================
# EXPORT
# =====================================================

country_events.to_excel(

    "data/Forecast_Countries.xlsx",

    index=False

)

print(country_events)

print(
    "\nForecast Countries exported"
)