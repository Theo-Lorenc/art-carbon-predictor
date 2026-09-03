import sqlite3
import pandas as pd

conn = sqlite3.connect("database/carbon.db")

df = pd.read_sql(
    "SELECT * FROM project_snapshots",
    conn
)

print(df)

conn.close()