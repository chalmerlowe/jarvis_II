my_csv = open('log_file_1000.csv')

for line in my_csv:
    if '220.211.18.31' in line:
       print(line)

my_csv.close()        