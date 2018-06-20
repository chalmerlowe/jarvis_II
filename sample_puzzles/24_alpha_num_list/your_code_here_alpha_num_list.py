# TITLE: alpha_num_list >> your_code_here_alpha_num_list.py
# AUTHOR: Chalmer Lowe
# DESCRIPTION:

# The file: alpha_num_list.txt contains a sequence of letters and numbers 
#     that may include duplicates.
#     Deduplicate the sequence and identify the item at the 42nd position
#     position, counting from zero. Ensure that you do not alter the order
#     of the items as you deduplicate.

# For example, if given the following sequence:
#     A A 1 3 C 3 C 1 D 13 D 2 2 A 3 4 5 6 A

# Upon deduplication, you are left with the following:
#     A 1 3 C D 13 2 4 5 6

#     ^ ^ ^ ^ ^  ^
#     0 1 2 3 4  5th position

# All of the above items are in the same relative order as the original...
#     i.e. the 'C' is before the 'D'.


# If asked to identify the item at the fifth position, counting from zero, the answer is:
#     13

# ----------------------------------
#
# Your code goes here:

path = 'alpha_num_list.txt'

# listify will read the first line of a file and return a list
# in which each "word" is an element. 

def listify(filename):
    finput = open(filename, 'r')
    return finput.readline().split('\n')[0].split(' ')


# deduplicateList takes a list as input and returns a new list
# containing all the elements of the first, sans duplicates

def deduplicateList(linput):
    loutput = []
    for x in linput:
        if not (x in loutput):
            loutput.append(x)
    return loutput

alpha_num_list = listify(path)
deduplicated_list = deduplicateList(alpha_num_list)

print deduplicated_list[42]


