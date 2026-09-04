import sqlite3
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

conn = sqlite3.connect("database/carbon.db")

query = """
SELECT

    p.project_id,
    p.project_name,
    p.country,

    s.issued_credits,

    COUNT(d.document_id) AS document_count,

    pd.project_creation_date,
    pd.project_start_date

FROM projects p

LEFT JOIN project_snapshots s
    ON p.project_id = s.project_id

LEFT JOIN project_documents d
    ON p.project_id = d.project_id

LEFT JOIN project_details pd
    ON p.project_id = pd.project_id

GROUP BY
    p.project_id

ORDER BY
    s.issued_credits DESC
"""

df = pd.read_sql(query, conn)

print(df)

df.to_excel(
    "data/Issued_vs_Not_Issued.xlsx",
    index=False
)

conn.close()