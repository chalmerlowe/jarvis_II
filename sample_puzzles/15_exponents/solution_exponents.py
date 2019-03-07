# TITLE: exponents >> solution_exponents.py
# AUTHOR: Chalmer Lowe
# DESCRIPTION:

# for all numbers between 1 and 10 (inclusive), the sum of all:
#     * squares of numbers divisible by 2 AND
#     * cubes of numbers divisible by 3 AND
#     * fourth powers of numbers divisible by 4 AND
#     * fifth powers of numbers divisible by 5
#     is 108669
#
# Find the sum of all squares, cubes, biquadratics, and fifth powers
#     for numbers divisible by 2, 3, 4, and 5, respectively, between
#     1 and 10000.

# ==============================================================
# Your code goes here:

# Solution Zero:

sums = []
for exponent in [2, 3, 4, 5]:
    interim_sums = []    
    for num in range(0, 10001, exponent):
        interim_sums.append(num ** exponent)
    total = sum(interim_sums)
    sums.append(total)

answer = sum(sums)    
print(answer)

# Solution One:

exponents = [2, 3, 4, 5]
interim_sums = []
upper_bound = 10000 + 1

def solver(upper_bound):
    for exp in exponents:
        interim_sums.append(sum([n ** exp for n in range(0, upper_bound, exp)]))
    return sum(interim_sums)

print('The answer is:', solver(upper_bound))

# 33388360001665649978667
