# The file, data_32.txt, has a series of equations, one 
#      per line of the file.
# 
# The equations fall into four categories:
#     * addition
#     * subtraction
#     * multiplication
#     * division

# Within each category, you will find three types of equations using
#     both standard operators and/or text-based operators, as shown below:
# ADDITION:        x plus y       OR x + y OR sum of x and y
# SUBTRACTION:     x minus y      OR x - y OR difference between x and y
# MULTIPLICATION:  x times y      OR x * y OR product of x and y
# DIVISION:        x divided by y OR x / y OR division of x by y

# Read each line of the file, determine which category of 
#     mathematical equation you should perform and then calculate
#     the result for that line, rounded to two decimal places.
# Your answer is the sum of all the results.

# For example,if given the following equations, you would calculate
#     the results shown:

#     sum of 6 and 6                 # 12
#     4 * 4                          # 16
#     10 * 3                         # 30
#     8 + 5                          # 13 
#     7 times 2                      # 14
#     0 plus 2                       #  2
#     1 + 1                          #  2
#     8 * 2                          # 16
#     difference between 7 and 4     #  3
#     division of 7 by 4             #  1.75   # round to 2 decimal places

# Finally, sum all these to produce the answer, again, rounded to
#     two decimal places, if necessary: 109.75

# An additional file with just the sample equations given above is
#     also included as test_data_32.txt
# ----------------------------------------------------------------------

# SOLUTION ZERO: -------------------------------------------------------

FILENAME = 'data_32.txt'

with open(FILENAME) as fin:
    total = 0
    
    for line in fin:
        numbers = []
        line = line.strip().split(' ')
        for item in line:
            if item.isnumeric():
                numbers.append(int(item))
        
        num_one, num_two = numbers
        if 'plus' in line or '+' in line or 'sum' in line:        
            total += round(num_one + num_two, 2)
        if 'minus' in line or '-' in line or 'difference' in line:        
            total += round(num_one - num_two, 2)
        if 'times' in line or '*' in line or 'product' in line:        
            total += round(num_one * num_two, 2)
        if 'divided' in line or '/' in line or 'division' in line:        
            total += round(num_one / num_two, 2) 

print(round(total, 2))


# SOLUTION ONE: --------------------------------------------------------

import re

add_pattern = re.compile(r'((\d*)\s(plus|\+)\s(\d*)|sum of (\d*) and (\d*))')
sub_pattern = re.compile(r'((\d*)\s(minus|\-)\s(\d*)|difference between (\d*) and (\d*))')
mul_pattern = re.compile(r'((\d*)\s(times|\*)\s(\d*)|product of (\d*) and (\d*))')
div_pattern = re.compile(r'((\d*)\s(divided by|\/)\s(\d*)|division of (\d*) by (\d*))')

def num_collector(match):
    matches = []
    for element in match.groups():
        if element and element.isnumeric():
            matches.append(int(element))
    return matches

with open('data_32.txt') as fin:
    values = []
    total = 0
    for line in fin:
        line = line.strip()
        add_match = add_pattern.search(line)
        sub_match = sub_pattern.search(line)
        mul_match = mul_pattern.search(line)
        div_match = div_pattern.search(line)
        
        if add_match:
            matches = num_collector(add_match)
            total += round(sum(matches), 2)
            
        if sub_match:
            matches = num_collector(sub_match)
            total += round(matches[0] - matches[1], 2)

        if mul_match:
            matches = num_collector(mul_match)
            total += round(matches[0] * matches[1], 2)

        if div_match:
            matches = num_collector(div_match)
            total += round(matches[0] / matches[1], 2)

print(round(total, 2))