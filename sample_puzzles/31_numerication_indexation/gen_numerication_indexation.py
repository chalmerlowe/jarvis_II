# The file, data.txt, has a series of numbers and words,
#     with one number and one word per line.
#
# Using the number as a 0-based index, find the
#     character in the word at that index
#
# Use a combination of all the indexes and the characters you found to then
#     find the answer to the puzzle, in the following manner:
#
# Sum the numbers and then divide the sum by 6, rounding the result
#     to the nearest 10.
#
# Using the rounded result of this calculation as an index, find the result
#     among the characters you extracted.

# For example, given the following:
#
# 5  python                            # n
# 10 statsmodels                       # s
# 4  pandas                            # a
# 4  numpy                             # y
# 7  requests                          # s
# 5  pipenv                            # v
# 6  pendulum                          # m
# 7  selenium                          # m
# 9  matplotlib                        # b
# 8  tensorflow                        # o
# 12 beautifulsoup                     # p
# 6  ipython                           # n

# sum = 5 + 10 + 4 + 4 + 7 + 5 + 6 + 7 + 9 + 8 + 12 + 6 = 83
# sum / 6 = 13.833333333333334
# 13.833333333333334 rounded to the nearest 10 = 10.0

# The characters at each of the noted indexes are:
#     n s a y s v m m b o p n
#                         ^
#
# The answer, located at index 10 is:
#     p

# -------------------------------------------------------
# IMPORTS
from random import sample, randint
import sys

# VARIABLES
if sys.argv[1]:
    NUM_LINES = int(sys.argv[1])
else:
    NUM_LINES = 10

print(NUM_LINES)

# FILES
with open("../universal_puzzle_data/113809of.fic") as fin:
    lines = fin.read().split("\n")
    print(len(lines))

words = sample(lines, NUM_LINES)

with open("data.txt", "w") as fout:
    for word in words:
        index = randint(0, len(word) - 1)
        output = f"{index} {word}\n"
        fout.write(output)
