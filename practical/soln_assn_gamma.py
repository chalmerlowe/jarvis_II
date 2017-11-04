import csv

with open('AMEX_daily_prices_N.csv') as fin:
    header = fin.readline()

    data = csv.reader(fin)

    stocks = set()
    for line in data:
        symbol = line[1]
        opening = float(line[3])
        closing = float(line[6])
        if 30 < opening < 420 and 32 < closing < 422:
            stocks.add(symbol)

# Primary Answer:            
with open('assn_gamma.txt', 'w') as fout:
    sorted_stocks = sorted(stocks)
    output = ','.join(sorted_stocks)
    fout.write(output)   

    
# Bonus Challenge:    
with open('assn_gamma_bonus.txt', 'w') as fout:
    sorted_stocks = sorted(stocks)

    # Because I am pulling out stocks two at a time...
    #     I need to generate half as many steps when I 
    #     go through the for loop.
    #     I could have used: range(len(stocks)/2)
    #     but I chose to go through the range object in
    #     steps of two instead using slices and increments.
    #     WHY? Because.
    
    for cycle in range(len(stocks))[::2]:
        item1 = sorted_stocks.pop(0) 
        item2 = sorted_stocks.pop(0)
        
        output = ','.join([item1, item2]) + '\n'
        fout.write(output)