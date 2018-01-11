# TITLE: even to hept >> soln_evens_to_hepts.py
# AUTHOR: Chalmer Lowe
# DESCRIPTION:

# Read all the values from the file output.txt, then sum the
#     count of all the numbers that are evens, triples,
#     quints, or hepts, meaning:
#     * evens:   all numbers evenly divisible by 2
#     * triples: all numbers evenly divisible by 3
#     * quints:  all numbers evenly divisible by 5
#     * hepts:   all numbers evenly divisible by 7

# NOTE: ensure that you don't duplicate any counts

# For example:
#     For the numbers between 2 and 20 inclusive,
#     evens:   2, 4, 6, 8, 10, 12, 14, 16, 18, 20   > 10 count
#     triples: 3, 9, 15 (6, 12 and 18 are dupes)    >  3 count
#     quints:  5, (10, 15, 20 are dupes)            >  1 count
#     hepts:   7 (14 is a dupe)                     >  1 count
#                                                 ----------
#                                                     15 count
#
# ----------------------------------

def passes_criteria(num):
    '''check for numbers that meet the four criteria'''

    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        return 1
    return 0

count = 0
with open('output.txt') as fin:
    for line in fin:
        number = int(line)
        count += passes_criteria(number)

print('Answer: ', count)
# 771428
