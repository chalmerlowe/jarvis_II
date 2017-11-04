fin = open('yahoo_prices_short.csv')


close = list()
for line in fin:
    fields = line.strip().split(',')
    print(fields[0])
    close.append(fields[3])
