# RSA tokens produce a sequence of pseudorandom six-digit numbers
#     that update every 60 seconds. 
# The six-digit numbers are used to help authenticate users that
#     log into systems, typically by requiring the user to supply
#     both a PIN and the six-digit number.
# On the screen, the numbers are broken into two groups of three
#     and might look something like the following:
#     * 247 456
#     * 765 294
#     * 232 543

# Interestingly, the six-digit numbers occasionally have patterns
#     such as the following:
#     * 123 321     - a palindrome if you consider all six numbers
#     * 121 454     - two mini palindromes, one in each group of three
#                     (they do not need to be identical)
#     * 123 679     - rising numbers (each subsequent number is equal to 
#                     or larger than the previous number)
#     * 654 321     - falling numbers (each subsequent number is
#                     equal to or smaller than the previous number)

# Given the values in the file rsa_token_values_I.txt:
# Count how many times each pattern occurs and identify the smallest and 
# largest counts (ignore count of items that don't match any category).
# For example, given the following...

#     * 123 321     palindrome
#     * 247 456     no category
#     * 765 294     no category
#     * 123 679     rising
#     * 345 543     palindrome

# largest count is 2 (palindrome) and smallest count is 1 (rising), 
#     ignore the no category samples.

from random import sample
from gen_utilities import stitcher

NUM_LINES = 1000

with open('rsa_token_values_I.txt', 'w') as fout:
    numbers = []
    for num in range(1000000):
        numbers.append(list(str(num).rjust(6, '0')))

    pre_tokens = sample(numbers, NUM_LINES)
    
    for token in pre_tokens:        
        fout.write(stitcher(token, new_line=True))