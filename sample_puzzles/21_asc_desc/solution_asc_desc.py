# TITLE: asc_desc >> solution_asc_desc.py
# AUTHOR: Chalmer Lowe
# DESCRIPTION:

# You are given the file: asc_desc.csv. It contains multiple lines,
# each of which contains a word, an integer and a float.
# 

# Your job is to sort each of the lines using a two-tiered approach:
# sort lines based on the values of the floats in DESCENDING numerical order
#     and sort the lines based on the words in ASCENDING alphabetical order

# With the lines properly sorted, find the 500th line
#     and add the integer value to the float value and submit that 
#     as your answer.

# For example, if given the following values in the csv and asked
#     to sum the values on the 5th line...

# conductions,2,300.001
# fitchews,5,500.002
# mulches,8,700.003
# conductions,3,500.001 
# fitchews,1,600.002
# mulches,5,600.003
# conductions,6,400.001
# mulches,7,500.003

# once sorted, will result in the following:

# conductions,3,500.001 
# conductions,6,400.001
# conductions,2,300.001
# fitchews,1,600.002
# fitchews,5,500.002 <<< fifth line >>> 500.002 + 5 = 505.002
# mulches,8,700.003
# mulches,5,600.003
# mulches,7,500.003

# Submit as your answer: 505.002

# ==============================================================
# Your code goes here:

from operator import itemgetter

with open('asc_desc.csv') as fin:
    items = [item.rstrip().split(',') for item in fin.readlines()]
    inputs = [[sublist[0], int(sublist[1]), float(sublist[2])] for sublist in items]
    floats_desc = sorted(inputs, key=itemgetter(2), reverse=True) 
    final = sorted(floats_desc, key=itemgetter(0))
print(final[499][1] + final[499][2])
