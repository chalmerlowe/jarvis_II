import sqlite3

conn = sqlite3.connect('my_first_sql.db')
create = '''CREATE TABLE stocks (symbol text,
                                 date date,
                                 open_price float,
                                 close float,
                                 volume integer
                                 )'''

try:
    conn.execute(create)
except:
    pass

fin = open('AMEX_daily_prices_N.csv')

fin.readline()

insert = '''INSERT INTO stocks VALUES (?, ?, ?, ?, ?)'''


for line in fin:
    exchange, symbol, date, open_price, high, low, close, volume, adjust = line.strip().split(',')
    conn.execute(insert, (symbol, date, open_price, close, volume))

cur = conn.cursor()

query = 'SELECT * FROM stocks'

for row in cur.execute(query):
    print(row)
