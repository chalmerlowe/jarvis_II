import csv

with open('AMEX_daily_prices_N.csv') as fin:
    header = fin.readline()
    data = csv.reader(fin)

    stocks = {}
    for line in data:
        symbol = line[1]
        closing = float(line[6])
        opening = float(line[3])
        difference = closing - opening
        stocks[symbol] = stocks.get(symbol, []) + [difference]

for key in stocks:
    total = sum(stocks[key])
    if total < -40:
        print(key, total)
