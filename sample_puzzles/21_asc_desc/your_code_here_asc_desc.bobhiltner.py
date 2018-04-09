# TITLE: asc_desc >> your_code_here_asc_desc.py
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
"""
Created on Wed Apr  4 12:31:10 2018

@author: bobhilt
ascending descending sort puzzle
"""
from operator import itemgetter

def get_asc_desc_values(l,n):
    #l = list of tuples
    #n = index into list
    # returns 2nd + 3rd value at index n
    s=sorted(sorted(l, key=itemgetter(2), reverse=True),key=itemgetter(0))
    t = s[n]
    return t[1] + t[2]

with open('asc_desc.csv') as f:
   mylist = [l.strip("\n").split(",") for l in f.readlines()]
   mylist = [[t[0], int(t[1]), float(t[2])] for t in mylist]


#################################################################
print ("500th asc_desc value:",get_asc_desc_values(mylist,499))
#################################################################

########################3
import unittest

class TestGetAscDesc(unittest.TestCase):
    
    def test_sample(self):

        l = [
            ('conductions',2,300.001),
            ('fitchews',5,500.002),
            ('mulches',8,700.003),
            ('conductions',3,500.001),
            ('fitchews',1,600.002),
            ('mulches',5,600.003),
            ('conductions',6,400.001),
            ('mulches',7,500.003)]
        
        self.assertEqual(get_asc_desc_values(l,4), 505.002)
        



if __name__ == '__main__':
    unittest.main()

