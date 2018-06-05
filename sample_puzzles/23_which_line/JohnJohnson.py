# TITLE: which line empty file >> your_code_here_which_line.py
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
#
# Your code goes here:
weCareAboutFileSizeAndMemory = True 
if weCareAboutFileSizeAndMemory:
    count=1
    with open('words.txt') as fi:
        for line in fi:
            if line[0:-1]=='python':
                print( count )
                break
            else:
                count+=1
else:
    with open('words.txt') as fi:
        text = fi.read()
    text = text[0:text.find('python')]
    print( text.count('\n')+1 )