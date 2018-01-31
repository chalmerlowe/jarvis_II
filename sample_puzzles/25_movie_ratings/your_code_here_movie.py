file = open('movies.txt')
ratings = file.read().split('\n')[:-1]

ratenums = {'1':0, '2':0, '3':0, '4':0, '5':0}
ratesums = 0

for rate in ratings:
    ratenums[rate] += 1
    ratesums += int(rate)

avg = ratesums/len(ratings)

print('total ratings:', ratenums)
print('avg rating:', avg)

# --------------------------------------------

from collections import Counter
ratings = open('movies.txt').read().split('\n')
ratings = [int(rating) for rating in ratings if rating != '']
average = sum(ratings)/len(ratings)

c = Counter(ratings)
print('Ratings:', c)
print('Average:', average)