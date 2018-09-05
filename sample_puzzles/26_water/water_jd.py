# TITLE: water >> your_code_here_water.py
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
# Your code goes here:

fin = open('water.txt','r')

# create a dictionary (key,value)-pair that equals to (customer,usage)
records = {}
for line in fin:
    customer, usage = line.split(';')    # unpack this tuple
    if customer not in records:
        records[customer] = usage
    else:
        pass       # skip the customer if already found in dictionary
fin.close()

for cust, use in sorted(records.items(), reverse=True, key = lambda x: x[1])[:5]:
    print("%s >>> with a usage of %s" %(cust, use) )
    
# Answer (top 5): should be :
# b4flc10 >>> with a usage of 498
# zqirrxz >>> with a usage of 495
# bwfggot >>> with a usage of 493
# 3w0ysce >>> with a usage of 491
# 2jptt1r >>> with a usage of 490
    