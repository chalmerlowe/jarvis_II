# TITLE: water >> solution_water.py
# AUTHOR: Aidan Lowe and Chalmer Lowe
# DESCRIPTION:

# You work for a water distribution company and have all a file
#     (water_dupe.txt) with
#     data for each customer's water usage in gallons.
# Your job is to find the customer with the highest usage and the customer
#     with the lowest usage.

# The file: water.txt, has multiple lines. Each line contains two elements:
#     a customer ID and a number that are separated by semicolons.
#
#     * Find the customers with the highest and lowest usages
#     * NOTE: Some customer IDs repeat... if a customer ID repeats, then
#             simply sum up the amounts for that customer ID.

# For example, given the following lines:
#    j2o31i4;562
#    ja02i3k;743
#    yw83h2o;560      < duplicate: sum all lines with this customer ID
#    i2o3401;489
#    yw83h2o;320      < duplicate: sum all lines with this customer ID
#    2u3hoas;108
#    i12j018;712

# the highest and lowest customers by usage would be:
#    yw83h2o >>> with a usage of 880 (560 + 320)
#    2u3hoas >>> with a usage of 108

# ==============================================================
# Your code goes here:

file = open('water_dupe.txt').read().split('\n')[:-1]

from collections import defaultdict

mDict = defaultdict(int)
for line in file:
    ID, amount = line.split(';')
    amount = int(amount)
    mDict[ID] += amount

items = sorted(mDict, key=mDict.__getitem__)

# items = [x + ';' + str(mDict[x]) for x in items[-5:]]
print('highest:', items[-1], mDict[items[-1]])
print('lowest:', items[0], mDict[items[0]])
