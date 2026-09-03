import sqlite3
import pandas as pd

conn = sqlite3.connect("database/carbon.db")

query = """
SELECT DISTINCT
    project_status
FROM project_snapshots
ORDER BY project_status
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()