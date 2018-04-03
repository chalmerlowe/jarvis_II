# TITLE: statistics >> gen_statistics.py
# AUTHOR: Chalmer Lowe
# DESCRIPTION:


# The file: statistics.txt, has multiple numbers, separated by commas on each
#     line. NOTE: Not all lines will have the same number of values.
# In addition, each line has one of several statistical terms as the first
#     element: mean, median, mode, variance, standard deviation
# For each line, identify the stats term, and perform that calculation on
#     the numbers on the list. All results should be rounded to a whole number
#     value (NOTE: do not simply truncate).
#     Sum the total of all results.
# For example:
#
#     mean,1,2,3,4,5           >                      3
#     median,1,3,5,7           >                      4
#     variance,2,1,1,0,0,1,3   > 1.1428571428571428 > 1
#     stdev,2,1,1,0,0,1,3      > 1.0690449676496976 > 1
#                              ---------------------------
#                                        total:       9

# ==============================================================
# Your code goes here:

from statistics import mean, median, mode, variance, stdev

def stats_calc(term, values):
    calc = {'mean': mean,
	    'median': median,
	    'variance': variance,
	    'stdev': stdev,
	    }

    return round(calc[term](values))


with open('stats.txt') as fin:
    results = []
    for line in fin:
        line = line.strip().split(',')
        term, values = line[0], line[1:]
        values = [int(val) for val in values]

        result = stats_calc(term, values)
        results.append(result)
	# print(result)

total = sum(results)
print(total)

# 21550995688




# ==============================================================
# Solution One
from statistics import mean, median, variance, stdev

# key is the key term which determines what operation to perform
# data is data contained within each line
def stat_func(key, data):
    functions = {
        'mean': mean,
	'median': median,
	'variance': variance,
	'stdev': stdev,
    }

    return round(functions[key](data))


total = 0

with open('stats.txt', 'r') as f:
    for line in f:
        data = line.rstrip('\n').split(',')
        total += stat_func(data[0], map(int, data[1:]))

print(total)
