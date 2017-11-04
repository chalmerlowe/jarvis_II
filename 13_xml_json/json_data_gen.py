import csv
import json



with open('AMEX_daily_prices_N.csv', encoding='utf-8-sig') as fin:
    reader = csv.reader(fin)

    data = {}

    header = ''
    for line in reader:
        if not header:
            header = line
            continue
        exchange, stock_sym, date, _open, high, low, close, volume, adj = line
        data[stock_sym] = data.get(stock_sym, []) + [high]

print(len(data))

with open('data.json', 'w') as fout:
    json.dump(data, fout)


with open('data.json') as inputfile:
    prices = json.load(inputfile)

    select_stock = {}
    for stock in prices:
        for price in prices[stock]:
            num_price = float(price)
            if num_price > 20.0:
                select_stock[stock] = select_stock.get(stock, []) + [price]


with open('prices.json', 'w') as outputfile:
    json.dump(select_stock, outputfile)

print(len(select_stock))
