# TITLE: even to quint generator >> gen_evens_to_quints.py
# AUTHOR: Chalmer Lowe
# DESCRIPTION:

# Read all the values from the file xxx.txt, then sum the
#     count of all the numbers that are evens, triples,
#     quints, or hepts, meaning:
#     * evens: all numbers evenly divisible by 2
#     * triples: all numbers evenly divisible by 3
#     * quints: all numbers evenly divisible by 5
#     * hepts: all numbers evenly divisible by 7

# NOTE: ensure that you don't duplicate any counts

# For example:
#     For the numbers between 2 and 20 inclusive,
#     evens: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20    > 10 count
#     triples: 3, 9, 15 (6, 12 and 18 are dupes)  >  3 count
#     quints: 5, (10, 15, 20 are dupes)           >  1 count
#     hepts:  7 (14 is a dupe)                    >  1 count
#                                                 ----------
#                                                   15 count
#
# ----------------------------------

from random import shuffle

numbers = list(range(2, 1000000))
shuffle(numbers)

with open('output.txt', 'w') as fout:
    for number in numbers:
        fout.write(str(number) + '\n')

with open('output.txt') as fin:
    nums = [int(n.rstrip()) for n in fin.readlines()]
    dedupes = set()
    for num in nums:
        if num % 2 == 0:
            dedupes.add(num)
        elif num % 3 == 0:
            dedupes.add(num)
        elif num % 5 == 0:
            dedupes.add(num)
        elif num % 7 == 0:
            dedupes.add(num)
        else:
            pass

print(len(dedupes))
# 771428
