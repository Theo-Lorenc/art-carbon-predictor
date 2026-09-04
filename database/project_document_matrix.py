import sqlite3
import pandas as pd

conn = sqlite3.connect("database/carbon.db")

query = """
SELECT
    p.project_id,
    p.project_name,
    s.issued_credits,
    d.document_type

FROM projects p

LEFT JOIN project_snapshots s
    ON p.project_id = s.project_id

LEFT JOIN project_documents d
    ON p.project_id = d.project_id

ORDER BY
    s.issued_credits DESC,
    p.project_id
"""

df = pd.read_sql(query, conn)

pivot = pd.pivot_table(
    df,
    index=[
        "project_id",
        "project_name",
        "issued_credits"
    ],
    columns="document_type",
    aggfunc="size",
    fill_value=0
)

pivot.to_excel(
    "data/Project_Document_Matrix.xlsx"
)

print(pivot)

conn.close()