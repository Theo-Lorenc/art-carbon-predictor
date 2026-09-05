import sqlite3
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)
pd.set_option("display.width", 1000)

conn = sqlite3.connect("database/carbon.db")

query = """
SELECT
    project_id,
    document_name,
    document_title,
    document_type,
    upload_date,
    download_url

FROM project_documents

WHERE project_id = 'ART0126'
"""

query = """
SELECT
    project_id,
    COUNT(*) AS rows,
    COUNT(DISTINCT document_name) AS unique_docs

FROM project_documents

GROUP BY project_id

ORDER BY rows DESC
"""

query = """
SELECT
    COUNT(*) AS rows,
    COUNT(DISTINCT document_name) AS unique_docs
FROM project_documents
WHERE project_id = 'ART0126';
"""

query = """
PRAGMA table_info(project_documents);
"""

query = """
PRAGMA index_list(project_documents);
"""


df = pd.read_sql(query, conn)

print(df.to_string())

df.to_excel(
    "data/Costa_Rica_Documents.xlsx",
    index=False
)

conn.close()

print("Export complete")