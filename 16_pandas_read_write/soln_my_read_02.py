import pandas as pd
import sqlite3
conn = sqlite3.connect('log_file.sql')

df = pd.read_sql('''SELECT email, lat, long, datetime 
                    FROM superheroes 
                    WHERE name LIKE "%barry%"''', conn)

print(df.head(10))