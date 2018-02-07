# TITLE: movies >> solution_movies.py
# AUTHOR: Aidan Lowe and Chalmer Lowe
# DESCRIPTION:

# You have a file (movies.txt) with a set of ratings for a specifc movie
#     ranging from 1-5
# Your job is to figure out how many times each rating was given
#     AND
# calculate the average rating for the movie

# EXAMPLE:

# 1
# 4
# 5
# 2
# 3
# 2

# In this example you would find one 1, two 2s, one 3, one 4, and one 5
# The average rating for this example would be 2.83


# ==============================================================
# Your code here:

# There are several possible approaches shown below.

# SOLUTION ZERO ========================================

file = open('movies.txt')
ratings = file.read().split('\n')[:-1]     # in this file, the last line is
                                           # blank.

ratenums = {'1':0, '2':0, '3':0, '4':0, '5':0}
ratesums = 0

for rate in ratings:
    ratenums[rate] += 1
    ratesums += int(rate)

avg = ratesums/len(ratings)

print('total ratings:', ratenums)
print('avg rating:', avg)


# SOLUTION ONE ========================================
# an alternate approach that simplifies the counting process

from collections import Counter
ratings = open('movies.txt').read().split('\n')

# A technique for bypassing the blank line
ratings = [int(rating) for rating in ratings if rating != '']
average = sum(ratings)/len(ratings)

c = Counter(ratings)
print('Ratings:', c)
print('Average:', average)
