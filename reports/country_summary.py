import sqlite3
import pandas as pd

conn = sqlite3.connect("database/carbon.db")

query = """
SELECT
    p.country,
    COUNT(DISTINCT p.project_id) AS projects,
    SUM(s.issued_credits) AS total_credits

FROM projects p

JOIN project_snapshots s
    ON p.project_id = s.project_id

GROUP BY p.country

ORDER BY total_credits DESC
"""

df = pd.read_sql(query, conn)

print(df)

df.to_excel(
    "data/Country_Summary.xlsx",
    index=False
)

conn.close()

print("Country Summary exported")