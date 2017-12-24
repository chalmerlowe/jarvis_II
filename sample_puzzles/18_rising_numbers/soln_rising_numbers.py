# TITLE: rising numbers >> soln_rising_numbers.py
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


with open('rising_numbers.txt') as fin:
    total = 0
    for line in fin:
        nums = line.rstrip().split(',')
        for num in nums:
            if rising_checker(num):
                total += int(num)

print('Answer:', total)
# 1588113
