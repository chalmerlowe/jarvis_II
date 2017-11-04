# <demo> stop
# generate multiple subplots on the same figure
# (based heavily on an example from the matplotlib website...)
# http://matplotlib.org/1.2.1/examples/pylab_examples/multiple_figs_demo.html
# we start by importing needed libraries

import numpy as np
import matplotlib.pyplot as plt

# <demo> stop
# numpy's linspace() function will generate evenly spaced numbers over an interval...
# it returns 50 numbers (num=50) by default

x1 = np.linspace(0.0, 5.0, num=200)
x2 = np.linspace(0.0, 5.0, num=200)

# NOTE: in a case where we need to set multiple names for essentially the same value(s)
# this syntax works:
# I am hesitant to use it for anything important...because I tend to miss the second
# variable when I quickly scan down my code
# x1 = x2 = np.linspace(0.0, 5.0, num=200)

# <demo> stop
# np.cos() calculates the cosine of each element in a passed array
# np.pi produces a static value for pi out to 15 decimal places.
# np.exp() calculates the natural exponential function (e^x) for each
#     element in a passed array, where e = 2.71828. This function acts as a dampener
#     in the following equation. As the value of (-x1) decreases (from
#     0 to -5), the value of np.exp gets closer and closer to zero.

y1 = np.cos(2 * np.pi/2.0 * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi/2.0 * x1)

# <demo> stop
# plt.interactive() sets the plot so that you can manipulate it incrementally in real-time

plt.interactive(True)

# this next command creates a subplot with a matrix of rows and columns 
# that has the following characteristics:
#     plt.subplot(nrows=2, ncols=1, plot_number=1)
# where nrows and ncols ID the number of rows/columns respectively
# where plot_number is the currently active (writeable) plot in the matrix

plt.subplot(2, 1, 1)

# <demo> stop
# we next write to the currently active plot based on these characteristics:
# plt.plot(x-axis values, y-axis values, formatting for the line)
# in this case, we use:
#     x1 values along the x-axis
#     y1 values along the y-axis
#     'y' = yellow
#     'o' yields circle marks
#     '-' (dash) yields a solid line
#     AND
#     'r' = red
#     '.' = small dots
#     '-' (dash) again yields a solid line 

plt.plot(x1, y1, 'yo-')
plt.plot(x2, y2, 'r.-')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped & undamped oscillations')

# <demo> stop
# next we set the second subplot as the active one and
# we define a green line with green marker dots.

plt.subplot(2, 1, 2)
plt.plot(x1, y1, 'g^-')
plt.xlabel('time (s)')
plt.ylabel('Damped')

# <demo> stop
# NOTE: when you have plt.interactive() set to True:
# it is possible to not only set values, but change values...
plt.xticks(np.arange(5), ['zero', 'one', 'two', 'three', 'four'])

plt.savefig('subplots.png')
