# TITLE: water >> solution_water_2.py
# AUTHOR: Aidan Lowe and Chalmer Lowe
# DESCRIPTION:

# You work for a water distribution company and have a file
#     (water_dupe.txt) with
#     data for each customer's water usage in gallons.
# Your job is to find the customer with the highest usage and the customer
#     with the lowest usage.

# The file: water_dupe.txt, has multiple lines. Each line contains two elements:
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

# SOLUTION 0 ---------------------------------------------

with open('water_dupe.txt') as fin:
    water_use = dict()
    for line in fin:
        ID, amount = line.strip().split(';')
        amount = int(amount)
        if ID in water_use:
            water_use[ID] += amount
        else:
            water_use[ID] = amount

max_use = max(water_use.values())
min_use = min(water_use.values())    
            
for key, value in water_use.items():
    if value == max_use:
        print("MAX:", key, value)
    if value == min_use:
        print("MIN:", key, value)
        

# SOLUTION 1 ---------------------------------------------

from collections import defaultdict
from operator import itemgetter

with open('water_dupe.txt') as fin:
    water_use = defaultdict(int)      # auto creates keys upon demand
    for line in fin:
        ID, amount = line.split(';')
        amount = int(amount)
        water_use[ID] += amount

    items = sorted(water_use.items(), key=itemgetter(1))

    print('lowest:', items[0])
    print('highest:', items[-1])

