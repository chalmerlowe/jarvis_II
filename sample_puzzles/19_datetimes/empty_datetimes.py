# TITLE: datetimes >> empty_datetimes.py
# AUTHOR: Chalmer Lowe
# DESCRIPTION:

# The file: datetimes.txt, has datetime stamps in four different formats:
#     YYYY MM DD hh:mm:ss
#     MM/DD/YYYY hh:mm:ss PM
#     yyyy-MM-ddTHH:mm:ss.ffffff
#     ddd, dd mmm yyyy hh:mm:ss

# In the file, there will be one datetime stamp per line, and the timestamps
#    are not in order.
#
# Organize the timestamps in ascending order and calculate the difference
#    between each adjacent timestamp. Identify the total number of seconds
#    difference between the two timestamps with the greatest difference.

# For example:
#     d3 = 1901-01-30T14:31:59.123456      << chronologically first
#     d4 = 01/30/1901 02:35:59 PM          << chronologically second
#     d2 = 1901 01 30 16:31:59             << chronologically third
#     d1 = Sat, 30 Mar 1901 14:31:59       << chronologically last

# d4 - d3   : 0 days, 239 sec, 876544 microsec = 239.876544 sec
# d2 - d4   : 0 days, 6960 sec                 = 6960 sec
# d1 - d2   : 58 days, 79200 sec               = 58 * 86400 s/day + 79200 sec =
#                                                                   5090400 sec

# In this case, the timestamps d1 and d2 had the greatest difference in seconds,
# with a total of 5090400 seconds.

# ==============================================================
# Your code goes here:
