# TITLE: water >> gen_water.py
# AUTHOR: Aidan Lowe and Chalmer Lowe
# DESCRIPTION: This script generates the data file associated with the
#              following puzzle.


# You work for a water distribution company and have a file (water.txt) with
#     data for each customer's water usage in gallons.
# Your job is to find the five customers with the highest usage.

# The file: water.txt, has multiple lines. Each line contains two elements:
#     a customer ID and a number that are separated by semicolons.
#
#     * Find the customers with the highest usage
#     * NOTE: Some customer IDs repeat... Use only the FIRST instance of a
#       customer record to determine that customer's usage.

# For example, given the following lines:
#    j2o31i4;562
#    ja02i3k;743
#    yw83h2o;240      < duplicate: use only the fisrt line
#    i2o3401;489
#    yw83h2o;240      < duplicate: drop this record
#    2u3hoas;108
#    i12j018;712

# the top 2 customers by usage would be:
#    ja02i3k >>> with a usage of 743
#    i12j018 >>> with a usage of 712


# ==============================================================

from random import choice, randint, sample

file = open('water.txt', 'w')

idlist = []

for x in range(250):
    id = ''
    if randint(0, 4) > 3 and idlist != []:
        id = choice(idlist)
    else:
        id = ''.join(sample('abcdefghijklmnopqrstuvwxyz1234567890', 7))
        idlist.append(id)
    amount = choice(range(250, 750))
    output = id + ';' + str(amount) + '\n'
    file.write(output)

file.close()
