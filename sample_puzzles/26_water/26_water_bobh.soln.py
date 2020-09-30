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
# Your code goes here: - Bob Hiltner bobhilt@gmail.com

customer_water_use = dict()
with open('water.txt', 'r') as f:
    for line in f:
        customer, usage = line.strip().split(';')
        if customer not in customer_water_use:
            customer_water_use[customer] = usage

sorted_use = sorted(customer_water_use.items(), key=lambda y: y[1], reverse=True)[:5]
print(sorted_use)

# Solution 2: using pandas
###################################
import pandas as pd
water_df = pd.read_csv('water.txt', sep=';', header=None, names=['id','usage'])
print(water_df.groupby('id').first().sort_values(by='usage',ascending=False)[:5])