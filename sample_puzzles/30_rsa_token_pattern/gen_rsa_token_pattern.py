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

# Given the values in the file rsa_token_values.txt:
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

from random import randint, choice 
NUM_LINES = 10

token_types = ['pal', 'mini', 'rising', 'falling', 'regular']

def regular():
    return choice( range( 100000, 1000000 ) )

def pal():
    firstThreeDigits = choice( range( 100, 1000 ) )
    return ( firstThreeDigits * 1000 ) + ( int(str(firstThreeDigits)[::-1]) )

def mini():
    firstTwoDigits1 = choice( range( 10, 100) )
    firstTwoDigits2 = choice( range( 10, 100) )
    left = ( firstTwoDigits1 * 10 ) + ( int(str(firstTwoDigits1)[0]) )
    right = ( firstTwoDigits2 * 10 ) + ( int(str(firstTwoDigits2)[0]) )
    return ( left * 1000 ) + right

for i in range(1000):
    print(mini())

"""
with open('rsa_token_values.txt', 'w') as fout:
    # cycle over the number of lines
    
    # choose the type of token (pal, mini, rising, falling)
    token = makeToken( choice( token_types ) )
    
    # given the type of token, create digits for token
    
    # format token (add space, new line, etc)
    concat( token[:3], " ", token[3:], "\n" )


    # write token to the output file
"""
