import sqlite3
import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

conn = sqlite3.connect("database/carbon.db")

query = """
SELECT
    p.project_id,
    p.project_name,
    s.issued_credits,
    d.document_type,
    d.document_title,
    d.upload_date

FROM projects p

JOIN project_snapshots s
    ON p.project_id = s.project_id

JOIN project_documents d
    ON p.project_id = d.project_id

WHERE s.issued_credits > 0

ORDER BY
    p.project_id,
    d.upload_date
"""

df = pd.read_sql(query, conn)

print(df)

df.to_excel(
    "data/Issued_Project_Documents.xlsx",
    index=False
)

conn.close()

print("Export Complete")