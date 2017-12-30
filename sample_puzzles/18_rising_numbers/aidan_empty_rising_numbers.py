# TITLE: rising numbers >> empty_rising_numbers.py
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
# Your code here:


file = open('rising_numbers.txt').read().split('\n')

nums = []
for line in file:
    nums.extend(line.split(','))

# nums = ['12345', '11112', '11229', '88899', '54321', '88799', '45456']
nums.remove('')

total = 0
for num in nums:
    curdigit = 0
    rising = True
    for digit in num:
        if curdigit <= int(digit):
            curdigit = int(digit)
        else:
            rising = False
    if rising:
        total += int(num)

print('sum of rising numbers:', total)