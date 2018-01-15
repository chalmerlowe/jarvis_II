# TITLE: which line solution >> solution_which_line.py
# AUTHOR: Chalmer Lowe
# DESCRIPTION:

# You are given a file: words.txt where each line:
#     * either contains a single word OR
#     * is blank (i.e. only has a newline character '\n')

# One of the lines in the file has the word "python" on it. Identify which line
#     has the word "python", by line number (starting at 1)

# Example:

# aardvark        line 1
# antelope        line 2
#                 line 3 is blank
# pangolin        line 4
# python          line 5 has the word python
# zebra           line 6
# elephant        line 7
#                 line 8 is blank
# cobra           line 9

# ANSWER is 5.

# WARNING: there are many ways to separate out the words in the text.
#          some techniques may accidentally eliminate the blank lines such
#          that you inadvertantly miscount. Be careful to count all lines,
#          blank OR not.
#
# ----------------------------------

with open('words.txt') as fin:
    counter = 1
    for line in fin:
        line = line.rstrip()
        if line == 'python':
            print(counter, line)
        counter += 1

# a more pythonic version is as follows:

with open('words.txt') as fin:
    for index, word in enumerate(fin, 1):
        if 'python' == word.rstrip():
            print(index, word)

# Answer: 3151
