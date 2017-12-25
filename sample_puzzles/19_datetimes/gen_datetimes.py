# TITLE: datetimes >> gen_datetimes.py
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

from random import randint, choice, random, shuffle
from datetime import datetime, timedelta

NUMBER_OF_TIMESTAMPS = 10000


def gen_timestamp(dt, version=None):
    '''Generate a datetime stamp using one of several timestamp formats:

    version 1:
    YYYY MM DD hh:mm:ss

    version 2:
    MM/DD/YYYY hh:mm:ss PM

    version 3:
    yyyy-MM-ddTHH:mm:ss.ffffff

    version 4:
    ddd, dd mmm yyyy hh:mm:ss
    '''

    if version == 1:
        return dt.strftime('%Y %m %d %H:%M:%S')
    elif version == 2:
        return dt.strftime('%m/%d/%Y %I:%M:%S %p')
    elif version == 3:
        return dt.strftime('%Y-%m-%dT%H:%M:%S.%f')
    elif version == 4:
        return dt.strftime('%a, %d %b %Y %H:%M:%S')

def second_converter(seconds):
    seconds, microseconds = divmod(seconds, 1)
    days, seconds = divmod(seconds, 86400)
    days = int(days)
    seconds = int(seconds)
    microseconds = int(microseconds * 1000000)

    return days, seconds, microseconds


current_time = datetime(2011, 1, 1, 0, 0, 0, 0) # pick a date.

tstamps = []
for cycle in range(NUMBER_OF_TIMESTAMPS):
    seconds = randint(1, 100000) + choice([0, 0, 0, random()])
    tdelta = timedelta(*second_converter(seconds))
    current_time += tdelta
    version = randint(1, 4)
    tstamps.append(gen_timestamp(current_time, version=version))

with open('timestamps.txt', 'w') as fout:
    shuffle(tstamps)
    for tstamp in tstamps:
        fout.write(tstamp + '\n')
