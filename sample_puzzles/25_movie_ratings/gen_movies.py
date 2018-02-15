import random

file = open('movies.txt', 'w')

for x in range(100):
    file.write(random.choice('123444455555') + '\n')

file.close()