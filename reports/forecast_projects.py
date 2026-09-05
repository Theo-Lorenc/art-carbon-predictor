import pandas as pd

df = pd.read_excel(
    "data/Forecast_Features.xlsx"
)

rows = []

today = pd.Timestamp.today()

for _, row in df.iterrows():

    if row["stage_score"] == 5:
        first_days = 180

    elif row["stage_score"] == 4:
        first_days = 365

    elif row["stage_score"] == 3:
        first_days = 730

    elif row["stage_score"] == 2:
        first_days = 1095

    else:
        first_days = 1460

    confidence = min(
        95,
        row["stage_score"] * 15
        +
        row["verification_activity"] * 2
    )

    for event in range(1, 4):

        forecast_date = (

            today

            +

            pd.Timedelta(
                days=first_days
            )

            +

            pd.DateOffset(
                years=event-1
            )
        )

        predicted_credits = (

            max(
                100000,
                row["document_count"]
                * 50000
                * event
            )

        )

        rows.append({

            "project_id":
                row["project_id"],

            "country":
                row["country"],

            "project_name":
                row["project_name"],

            "forecast_event":
                event,

            "predicted_issue_date":
                forecast_date.strftime(
                    "%Y-%m-%d"
                ),

            "predicted_credits":
                round(predicted_credits),

            "confidence":
                round(confidence)

        })

forecast = pd.DataFrame(rows)

forecast.to_excel(
    "data/Forecast_Projects.xlsx",
    index=False
)

print(
    forecast.head()
)

print(
    "Project Forecasts exported"
)