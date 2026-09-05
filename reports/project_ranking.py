import sqlite3
import pandas as pd

conn = sqlite3.connect("database/carbon.db")

query = """
SELECT
    p.country,
    p.project_name,
    s.project_status,
    s.issued_credits,
    s.last_status_changed

FROM projects p

JOIN project_snapshots s
ON p.project_id = s.project_id
"""

df = pd.read_sql(query, conn)

df["last_status_changed"] = pd.to_datetime(
    df["last_status_changed"],
    errors="coerce",
    utc=True
)

today = pd.Timestamp.now(tz="UTC")

df["days_since_status_change"] = (
    today - df["last_status_changed"]
).dt.days

# Excel compatibility
df["last_status_changed"] = (
    df["last_status_changed"]
    .dt.tz_localize(None)
)

df = df.sort_values(
    "days_since_status_change"
)

df.to_excel(
    "data/Project_Ranking.xlsx",
    index=False
)

print(df[
    [
        "country",
        "project_name",
        "days_since_status_change"
    ]
].head(10))

conn.close()

print("Project Ranking exported")