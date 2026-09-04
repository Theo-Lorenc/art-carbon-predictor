import sqlite3
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 300)

conn = sqlite3.connect("database/carbon.db")

query = """
SELECT
    project_id,
    document_type,
    MIN(upload_date) as first_seen,
    MAX(upload_date) as last_seen,
    COUNT(*) as count

FROM project_documents

GROUP BY
    project_id,
    document_type

ORDER BY
    project_id,
    first_seen
"""

df = pd.read_sql(query, conn)

print(df)

df.to_excel(
    "data/Document_Type_Summary.xlsx",
    index=False
)

conn.close()