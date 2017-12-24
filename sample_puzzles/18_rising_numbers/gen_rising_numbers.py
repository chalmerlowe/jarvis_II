# TITLE: rising numbers >> gen_rising_numbers.py
# AUTHOR: Chalmer Lowe
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
from random import shuffle


def rising_checker(number):
    '''Check a number (in string format) for a rising
    number pattern.
    '''

    highest = 0
    for digit in number:
        digit = int(digit)
        if digit >= highest:
            highest = digit
        else:
            return None
    else:
        return number

with open('rising_numbers.txt', 'w') as fout:
    nums = [str(num) for num in range(10, 10000)]
    shuffle(nums)
    span = 25
    while len(nums) > span:
        output, nums = nums[:span], nums[span:]
        output = ','.join(output) + '\n'
        fout.write(output)
    else:
        output = ','.join(nums) + '\n'
        fout.write(output)

'''

'''
