import sqlite3
import pandas as pd

conn = sqlite3.connect("database/carbon.db")

query = """
SELECT
    p.project_id,
    p.project_name,
    s.issued_credits,
    d.upload_date,
    d.document_type,
    d.document_title

FROM projects p

LEFT JOIN project_snapshots s
    ON p.project_id = s.project_id

LEFT JOIN project_documents d
    ON p.project_id = d.project_id

WHERE p.project_id IN
(
    'ART0131',
    'ART0130',
    'ART0126'
)

ORDER BY
    p.project_id,
    d.upload_date
"""

df = pd.read_sql(query, conn)

print(df)

df.to_excel(
    "data/Issued_Project_Timeline.xlsx",
    index=False
)

conn.close()

print("Timeline exported")