import sqlite3
import pandas as pd

conn = sqlite3.connect("database/carbon.db")

df = pd.read_sql(
    """
    SELECT
        project_id,
        project_key,
        project_name
    FROM projects
    """,
    conn
)

print(df)

conn.close()
