my_output = open('results.txt', 'w')

while True:
    output = input('Name one of your favorite foods: ')
    if output == 'exit':
        break
        
    else:
        my_output.write(output + '\n')

my_output.close()