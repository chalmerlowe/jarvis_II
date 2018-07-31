from random import randint, choice 
from math import ceil


def palindrome(n=6):
    '''Return a random sequence of n numbers that are palindromic.
    '''
    
    midpoint = ceil(n / 2)
    token = []
    for digit in range(midpoint):
        token.append(randint(0, 9))
        
    if n % 2 == 0:
        token += token[::-1]
    else:
        token += token[::-1][1:]     
    return token


def rising_falling(n=6, rising=True):
    '''Return a sequence of numbers that are rising (each subsequent number is
    equal to or larger than the previous number) OR falling (each subsequent
    number is equal to or smaller than the previous number).
    '''
    
    token = []
    if rising:
        current = 0
    else: 
        current = 9
    for digit in range(n):
        next = randint(0, 9)
        if rising:
            while next < current:
                next = randint(0, 9)
        else:
            while next > current:
                next = randint(0, 9)
        token.append(next)
        current = next        
    return token


def generic(n=6):
    '''Return a random sequence of n numbers.
    '''
    return [randint(0, 9) for digit in range(n)]
        

def stitcher(token, new_line=True):
    '''Return a string with the format three digits and three digits separated by a space:
    ddd ddd
    
    If new_line is True, returns the string with a new_line appended to the end:
    ddd ddd\n
    '''
    token = ''.join(str(digit) for digit in token)
    token = '{} {}'.format(''.join(token[:3]), token[3:])
    
    if new_line:
        token += '\n'

    return token


def create_user_id(lower=0, upper=99, digits=4):
    '''Return a userid string prepended with zeroes.
    
    The userids range from lower to upper (default is 0 and 99 respectively).
    
    The length of the userid string is set using digits (default is 4).
    '''
    return str(randint(lower, upper)).rjust(digits, '0')


def create_score():
    '''# TODO... define a method to create correlated scores
    '''
    return randint(0, 10)