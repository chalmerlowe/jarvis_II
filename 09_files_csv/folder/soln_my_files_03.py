fin = open('log_file_1000.csv')

count = 0
for line in fin:
    count += 1
    if 'SELINA' in line:
        print('Corrupt line:', count, line)
        
print('Total lines:', count)