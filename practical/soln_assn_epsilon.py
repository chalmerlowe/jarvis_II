import sqlite3
import pandas as pd

conn = sqlite3.connect('log_file.sql')

size = pd.read_sql('''SELECT name, payload, datetime 
                      FROM superheroes 
                      WHERE payload > 486000 AND payload < 489500''', conn)

print('The minimum selected payload:', size.payload.min(), '\n')
print('The maximum selected payload:', size.payload.max(), '\n')
print('The median selected payload:', size.payload.median(), '\n')
print('The selected values:', size.payload.values, '\n')
print('Details about my DataFrame:', size.info(), '\n')