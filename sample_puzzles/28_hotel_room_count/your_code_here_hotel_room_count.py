# TITLE: hotel_room_count >> your_code_here_hotel_room_count.py
# AUTHOR: Chalmer Lowe
# DESCRIPTION:

# In this puzzle, your objective is to identify how many rooms in one or more
# hotels meet certain criteria (namely which room numbers are evenly divisible
# by one or both of two numbers that will be provided). NOTE: ALL room numbers
# are in the hundreds: 100, 101, 1300, 1301, etc.

# You are given a file (hotels.txt) with certain values on certain lines.

# line 1: the number of hotels
# line 2: blank
# line 3: the number of floors in the hotel
# line 4: the number of rooms on each floor
# line 5: divisor #1 and divisor #2 (separated by a single space)

# lines 6 through 9: repeat of lines 2 through 5 (but with different values)
# lines 10 through 13: repeat of lines 2 through 5 (but with different values)

# This repetition continues until the number of hotels is exhausted.

# For example, if given the following values:

# 2             # number of hotels

# 3             # number of floors in hotel #1
# 4             # number of rooms per floor.
# 2 3           # find all room numbers divisible by 2 OR 3

# 4             # number of floors in hotel #2
# 6             # number of rooms per floor
# 3 5           # find all room numbers divisible by 3 OR 5

# The description of hotel #1 yields these hotel room numbers:
# 100, 101, 102, 103    > divisible by 2 OR 3: 100, 102
# 200, 201, 202, 203    > divisible by 2 OR 3: 200, 201, 202
# 300, 301, 302, 303    > divisible by 2 OR 3: 300, 302, 303

# Hotel #1 Room Count = 8

# The description of hotel #2 yields these hotel room numbers:
# 100, 101, 102, 103, 104, 105    > divisible by 3 OR 5: 100, 102, 105
# 200, 201, 202, 203, 204, 205    > divisible by 3 OR 5: 200, 201, 204, 205
# 300, 301, 302, 303, 304, 305    > divisible by 3 OR 5: 300, 303, 305
# 400, 401, 402, 403, 404, 405    > divisible by 3 OR 5: 400, 402, 405

# Hotel #2 Room Count = 13

# ANSWER: 8 + 13 = 21

# ==============================================================
# Your code goes here:
