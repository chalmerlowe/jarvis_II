# TITLE: mean means solution >> solution_mean_means.py
# AUTHOR: Chalmer Lowe
# DESCRIPTION:

# The file: mean_means.csv contains line upon line of numbers.
#     Each line has a random number of numbers, separated by commas.
#     Read each line and calculate the mean (average) for that line, rounded to
#     three digits.
#     Find all the means between 81 and 92, exclusive (81 < m < 92) and
#     calculate the mean of just those values, again rounding the final
#     result to three digits.
#
#     NOTE: to calculate the mean, sum a series of numbers and divide by
#           the total number of numbers.

# For example, if you were given the constraint that you are looking for means
#     between 81 and 92:
#     98, 99, 97, 92, 91          > average = 95.4       > out of bounds
#     82, 83, 90, 92, 91          > average = 87.6       > in of bounds
#     82.5, 83, 90.3456, 92, 91   > average = 87.769     > in of bounds, rounded
#     71, 78, 80, 83, 91          > average = 80.6       > out of bounds

#     87.6, 87.769      > answer = 87.684

#
# ----------------------------------
# Your code here:


from statistics import mean

with open('mean_means.csv') as fin:

    means = []
    for line in fin:

        line = line.strip().split(',')
        nums = [float(num) for num in line]
        average = round(mean(nums), 3)
        print(average)
        if 81 < average < 92:
            means.append(average)

print('answer: ', round(mean(means), 3))

# Answer: 86.852
