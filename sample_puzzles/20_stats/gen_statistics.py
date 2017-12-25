# TITLE: statistics >> gen_statistics.py
# AUTHOR: Chalmer Lowe
# DESCRIPTION:


# The file: statistics.txt, has multiple numbers, separated by commas on each
#     line. NOTE: Not all lines will have the same number of values.
# In addition, each line has one of several statistical terms as the first
#     element: mean, median, mode, variance, standard deviation
# For each line, identify the stats term, and perform that calculation on
#     the numbers on the list. All results should be rounded to two values.
#     Sum the total of all results.
# For example:
#
#     mean,1,2,3,4,5           >                      3
#     median,1,3,5,7           >                      4.0
#     variance,2,1,1,0,0,1,3   > 1.1428571428571428 > 1.14
#     stdev,2,1,1,0,0,1,3      > 1.0690449676496976 > 1.07
#                              ---------------------------
#                                        total:     12.21

# ==============================================================

from random import choice, randint

NUMBER_OF_LINES = 100000 

terms = ['mean', 'median', 'variance', 'stdev']

with open('stats.txt', 'w') as fout:
    for cycle in range(NUMBER_OF_LINES):
        # choose terms
        term = choice(terms)

        # create a list of numbers
        count = randint(5, 11)
        variant = randint(1, 6)
        lower = count + variant
        upper = count * variant * 100
        values = []
        for item in range(count):

            values.append(str(randint(lower, upper)))

        output = term + ',' + ','.join(values) + '\n'
        print(output, end='')
        fout.write(output)
