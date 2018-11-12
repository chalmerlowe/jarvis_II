# TITLE: 01_scrabble >> your_code_goes_here.py
# AUTHOR: Chalmer Lowe
# DATE: 20181111
# DESCRIPTION:

# In this puzzle, you will be given a file (1138090f.txt) that contains
#     a series of words, one word per line.
#
# Sort the words, by length. Ensure that you use a Stable Sorting algorithm.
# Once you have sorted the words by length, find all the words at the
#     following indexs:
#     * 22615
#     * 10582
#     * 353
#     * 1660
#     * 43880
#
# and display them on a single line, separated by spaces.

# For example... if the words in the file were:
#
# cat
# we
# python
# orangutan
# love

# And if you were given the indexes: 1, 4, 2, then
#     the answer would be:
#
#     we love python

# ==============================================================
# Your code goes here:

# Solution 0 ----------------------------

fin = open('1138090f.txt')

words = []

for line in fin:
    words.append(line.strip())

sorted_words = sorted(words, key=len)

positions = [22615, 10582, 353, 1660, 43880]

terms = []
for index in positions:
    terms.append(sorted_words[index])

print(' '.join(terms))

# Expected answer: python rocks for data science

# Solution 1 -----------------------------
# For someone looking for one-liner solution to get the sorted words
#     out of the file, see the list comprehension embedded in the sorted()
#     function.

with open('1138090f.txt') as fin:
    sorted_words = sorted([word.strip() for word in fin.readlines()], key=len)

positions = [22615, 10582, 353, 1660, 43880]

# similarly... the printing process can be handled with a second list
#     comprehension. The values in the comprehension can be unpacked
#     using the asterix. The similarly, the values can be printed on a
#     single line using the sep=' ' argument. 

print(*[sorted_words[index] for index in positions], sep=' ')
