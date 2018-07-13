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
from math import floor, ceil
NUM_LINES = 10

def makeNDigitPalindrome(n):
    if type(n) is not int:
        raise TypeError("argument `n` must be type: int\n    given: %s" % str(n))
    if (n <= 0):
        raise ValueError("argument `n` must be greater than 0\n    given: %i" % n)
    elif (n == 1):
        return choice( range( 1, 10 ) )

    else:
        substring = choice( range( 10 ** (int( n / 2 ) - 1), 10 ** int( n / 2 ) ) )
        if ((n % 2) == 0):
            '''If n is even: concatenate `substring` with its reverse'''
            return ( (substring * (10 ** int( n / 2 )))
                     + int( str( substring )[::-1]) )
        else:
            '''If n is odd: concatenate `substring` with a random 1-digit integer and `substring`'s reverse'''
            centerDigit = choice( range( 10 ) )
            return ( (substring * (10 ** ceil( n / 2 )))
                     + (centerDigit * (10 ** int( n / 2 )))
                     + int( str( substring )[::-1]))

def regular():
    return choice( range( 100000, 1000000 ) )

def pal():
    return makeNDigitPalindrome( int( 6 ) )


def mini():
    return ( (makeNDigitPalindrome( int( 3 ) ) * 1000)
             + makeNDigitPalindrome( int( 3 ) ) )

def rising():
    digit = choice( range( 1, 9 ) )
    token = 0

    for i in range( 6 )[::-1]:
        token += digit * (10 ** i)
        digit = choice( range( digit, 10) )

    return token

def falling():
    digit = choice( range( 1, 10 ) )
    token = 0

    for i in range( 6 )[::-1]:
        token += digit * (10 ** i)
        digit = choice( range( 0, digit + 1 ) )

    return token

token_types = [pal, mini, rising, falling, regular]
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
