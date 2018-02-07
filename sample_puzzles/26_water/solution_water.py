# TITLE: water >> solution_water.py
# AUTHOR: Aidan Lowe and Chalmer Lowe
# DESCRIPTION:


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
# There are several possible approaches shown below.

# SOLUTION ZERO ========================================

file = open('water.txt').read().split('\n')[:-1]

top1 = None
top2 = None
top3 = None
top4 = None
top5 = None
IDs = []

def getnum(inp):
    if inp == None:
        return 0
    return int(inp.split(';')[1])

for line in file:
    ID, amount = line.split(';')
    amount = int(amount)
    if ID in IDs:
        continue
    else:
        IDs.append(ID)
    
    if amount > getnum(top1):
        top5, top4, top3, top2, top1 = top4, top3, top2, top1, line
    elif amount > getnum(top2):
        top5, top4, top3, top2 = top4, top3, top2, line
    elif amount > getnum(top3):
        top5, top4, top3 = top4, top3, line
    elif amount > getnum(top4):
        top5, top4 = top4, line
    elif amount > getnum(top5):
        top5 = line

print('Top 5:', top1, top2, top3, top4, top5)


# SOLUTION ONE ========================================

from operator import itemgetter

customers = list()
memo = []

with open('water.txt') as fin:
    for line in fin:
        custid, usage = line.strip().split(';')
        
        # skip processing if we have already seen a customer ID
        if custid in memo:
            continue

        # saves each customer ID and the usage as a tuple:
        # [('b4flc10', 498), ('zqirrxz', 495), ('bwfggot', 493), ('3w0ysce', 491) ...
        customers.append((custid, int(usage)))
        memo.append(custid)

# sort the tuples based on the value in the second position.                
customers = sorted(customers, key=itemgetter(1), reverse=True)   

# save only the customer names for the first 5 customers
customers = [element[0] for element in customers[:5]]

print("Top 5:", customers)
