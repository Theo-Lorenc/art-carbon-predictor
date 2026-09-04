import sqlite3
import pandas as pd

conn = sqlite3.connect("database/carbon.db")

query = """
SELECT
    p.country,
    p.project_id,
    p.project_name,
    COUNT(d.document_id) as document_count

FROM projects p

LEFT JOIN project_documents d
ON p.project_id = d.project_id

GROUP BY
    p.project_id,
    p.project_name,
    p.country

ORDER BY
    document_count DESC
"""

df = pd.read_sql(query, conn)

max_docs = df["document_count"].max()

df["progress_score"] = (
    (df["document_count"] / max_docs) * 100
).round(1)

df.to_excel(
    "data/Project_Progress.xlsx",
    index=False
)

print(df)

conn.close()