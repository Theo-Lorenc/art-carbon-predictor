import sqlite3
import pandas as pd

conn = sqlite3.connect("database/carbon.db")

df = pd.read_sql(
    """
    SELECT *
    FROM project_details
    """,
    conn
)

print(df.head())

print()
print(f"Rows: {len(df)}")

conn.close()