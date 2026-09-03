import sqlite3
import pandas as pd

conn = sqlite3.connect("database/carbon.db")

query = """
SELECT
    p.country,
    p.project_id,
    p.project_name,
    p.project_type,
    p.methodology,
    s.project_status,
    s.issued_credits,
    s.last_status_changed

FROM projects p

JOIN project_snapshots s
ON p.project_id = s.project_id

ORDER BY
    p.country,
    p.project_name
"""

df = pd.read_sql(query, conn)

print(df.head())

df.to_excel(
    "data/Project_Detail.xlsx",
    index=False
)

conn.close()

print("Project Detail exported")