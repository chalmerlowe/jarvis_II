# TITLE: datetimes >> soln_datetimes.py
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
# ANSWER: 99991.320867 seconds
# ==============================================================

from datetime import datetime, timedelta

def parse_timestamp(dt):
    '''Parse a datetime stamp using one of several timestamp formats:

    version 1:
    YYYY MM DD hh:mm:ss

    version 2:
    MM/DD/YYYY hh:mm:ss PM

    version 3:
    yyyy-MM-ddTHH:mm:ss.ffffff

    version 4:
    ddd, dd mmm yyyy hh:mm:ss
    '''

    if '/' in dt:
        return datetime.strptime(dt, '%m/%d/%Y %I:%M:%S %p')
    elif '-' in dt:
        return datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S.%f')
    elif ',' in dt:
        return datetime.strptime(dt, '%a, %d %b %Y %H:%M:%S')
    else:
        return datetime.strptime(dt, '%Y %m %d %H:%M:%S')


with open('timestamps.txt') as fin:
    tstamps = []
    for line in fin:
        tstamp = line.rstrip()
        tstamps.append(parse_timestamp(tstamp))

results = sorted(tstamps)


longest_diff = timedelta(0, 0, 0)
while len(results) >= 2:
    t1, t2, results = results[0], results[1], results[1:]
    delta = t2 - t1
    if delta > longest_diff:
        longest_diff = delta
        print(longest_diff.total_seconds())

print(longest_diff.total_seconds())
