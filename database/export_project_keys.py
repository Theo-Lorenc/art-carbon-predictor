import sqlite3
import pandas as pd

conn = sqlite3.connect("database/carbon.db")

df = pd.read_sql(
    """
    SELECT
        project_id,
        project_key
    FROM projects
    """,
    conn
)

print(df)

df.to_csv(
    "data/project_keys.csv",
    index=False
)

conn.close()

print("Project keys exported")