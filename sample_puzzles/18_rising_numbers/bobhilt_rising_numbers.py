# TITLE: rising numbers >> empty_rising_numbers.py
# AUTHOR: Chalmer Lowe - solution by Bob Hiltner
# DESCRIPTION:
# Identify and sum all the numbers in the file that have a
#     "rising numerical pattern": meaning for each digit in the
#     number, the digit is either equal to OR greater than the
#     preceding digit (in this order: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9).
#
# For example:
#     * 12345 > rising
#     * 11112 > rising
#     * 11229 > rising
#     * 88899 > rising
#     * 54321 > NOT rising
#     * 88799 > NOT rising
#     * 45456 > NOT rising

# Based on the numbers above, the sum would be:
#     12345 + 11112 + 11229 + 88899 = 123585

# ==============================================================
# Your code here:
import pandas as pd
import numpy as np

def is_rising(number):
    #pick off last digit
    current = number % 10
    number //= 10
    while number:
        digit = number % 10
        if digit > current:
            return False

        current = digit
        number //= 10
    return True
        

nums = np.ravel(pd.read_csv('rising_numbers.txt', header=None))
#1. casts as float.  How to avoid this?
#2. can "ravel" type functionality be incorporated into the read_csv call?

nums = nums[~np.isnan(nums)]

total = 0
for num in nums:
    if is_rising(num):
        total += num

#3. Can this total be efficiently wrapped into a 
#   one-liner lambda/mapped + filter function?
        
print('Sum of "rising" numbers is:', int(total))
