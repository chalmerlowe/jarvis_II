import sqlite3

conn = sqlite3.connect('my_second_sql.db')
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
    exchange, symbol, date, open_price, high, low, close, volume, adjust = line.split(',')
    conn.execute(insert, (symbol, date, open_price, close, volume))

cur = conn.cursor()

query = '''SELECT symbol, open_price, close
           FROM stocks
           WHERE close > 925'''

for row in cur.execute(query):
    print(row)


