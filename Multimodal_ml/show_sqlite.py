import sqlite3
import pandas as pd

conn = sqlite3.connect("data.db")
df = pd.read_sql("SELECT * FROM csv_data LIMIT 10", conn)
conn.close()

print(df)
