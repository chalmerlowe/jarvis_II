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
        if stock_sym in ["NGX", "NKX", "NOX", "NVX", "NXE", "NXG", "NXI", "NXJ", "NXK", "NXM", "NXZ", "NZX"]:
            data[stock_sym] = data.get(stock_sym, []) + [close]

with open('x_stocks.json', 'w') as fout:
    json.dump(data, fout,
              indent=4,
              sort_keys=True)
