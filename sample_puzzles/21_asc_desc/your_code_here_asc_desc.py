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

# the strategy was to create a simple solution that read the entire
# data set in one instruction and did not modify the read data.  this
# would ensure a much different soln than Chalmer's

def keyz(itm):
    itm = itm.split(',')
    return (itm[0], -float(itm[2]))


with open('asc_desc.csv') as f:
            data = f.readlines()

data = sorted(data, key=keyz)
dt = data[500-1].split(',')
print("Answer:", int(dt[1]) + float(dt[2]))

#Answer: 159.055



