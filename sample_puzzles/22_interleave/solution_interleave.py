# TITLE: interleave >> solution_interleave.py
# AUTHOR: Chalmer Lowe
# DESCRIPTION:

# You are given a file (interleave.txt) with two lines.

# Each line contains numbers separated by semicolons.
# You will need to interleave the values from the two lines and calculate
#     the difference between each sequential pair of numbers.
# Sum all the even differences.

# For example... given the following numbers...

#     a = [1, 4, 9]
#     b = [8, 3, 3]

# interleaved_nums = [1,  8,  4,  3,  9,  3]
#                     ^   ^   ^   ^   ^   ^
#                    a1, b1, a2, b2, a3, b3

# If we examine, sequentially, all pairs of values to find any pairs that have
#     a difference between them that is even:

# between a1 and b1: 1 - 8 = -7   which is an odd difference
# between b1 and a2: 8 - 4 = 4    which is an even difference
# between a2 and b2: 4 - 3 = 1    which is odd
# between b2 and a3: 3 - 9 = -6   which is even
# between a3 and b3: 9 - 3 = 6    which is even

# Adding all the even differences yields:
#     4 + -6 + 6 = 4

# Answer = 4

# ==============================================================
# Your code goes here:

with open('interleave.txt') as fin:
    total = 0
    line1 = fin.readline().strip().split(';')
    line2 = fin.readline().strip().split(';')

    # pairs = [ zip(line1, line2)]
    combos = [int(item) for sublist in zip(line1, line2) for item in sublist]
    pairs = zip(combos, combos[1:])
    for pair in pairs:
         first, second = pair
         diff = first - second
         if diff % 2 == 0:
             # print(diff)
             total += diff

print('Answer:', total)
