# TITLE: alpha_num_list generator >> gen_alpha_num_list.py
# AUTHOR: Chalmer Lowe
# DESCRIPTION:

# This script generates the data to be used in the alpha_num_list puzzle.

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


from random import shuffle, randint

letters = list('ABCDEFGHIJKLMNOPQSTUVWXYZ')   # Missing the 'R' 
shuffle(letters)

nums = list(range(1, 61))
shuffle(nums)

alpha_nums = zip(letters, nums)

alpha_nums = [str(item) for sublist in alpha_nums for item in sublist]

sub = alpha_nums[:42]
end = alpha_nums[43:]
print(sub, end, sep='\n')

first_half = []
for item in sub:
    dupe_count = randint(10, 42)
    dupes = [item] * dupe_count
    first_half += dupes
    
    
second_half = []
for item in end:
    dupe_count = randint(10, 42)
    dupes = [item] * dupe_count
    second_half += dupes 

shuffle(first_half)
shuffle(second_half)
    
terms = first_half + ['R'] + second_half

output = ' '.join(terms) + '\n'
with open('alpha_num_list.txt', 'w') as fout:
    fout.write(output)