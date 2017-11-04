import pandas as pd
import time

div = pd.read_csv('AMEX_dividends_N.csv')
daily = pd.read_csv('AMEX_daily_prices_N.csv')

print('DIVIDENDS\n', div.head(7))
print('-' * 60)
print('DAILY PRICES\n', daily.head(7))

# Some students mentioned that the processing takes some time.
# This should be expected with a large data set on a laptop.
# To figure out how long it takes, we added in a snippet of code to
# measure the current time and the time at the end.
start = time.clock()

stocks = pd.merge(daily, div,
                  on='stock_symbol',
                  how='inner',
                 )

selected_stocks = stocks[stocks.date_y == '1991-06-24']
deduped_stocks = selected_stocks.stock_symbol.unique()
print('Unique array:', deduped_stocks)
print('Element zero from the unique array:', deduped_stocks[0])

print('Same result, one liner:', stocks[stocks.date_y == '1991-06-24'].stock_symbol.unique()[0])

# Calculating and printing the elapsted time
midway = time.clock()
print('Time >> first attempt:', midway - start)

# having noted that the above takes some time we discussed the idea of doing the
# filtering before hand and then deduplicating...

div = div[div.date == '1991-06-24']
print(div)

stocks = pd.merge(daily, div,
                  on='stock_symbol',
                  how='inner',
                 )

deduped_stocks = stocks.stock_symbol.unique()

# Calculating and printing the elapsted time
end = time.clock()
print('Time >> second attempt:', end - midway)
