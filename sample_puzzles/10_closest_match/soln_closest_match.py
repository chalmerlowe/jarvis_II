# TITLE: closest_matches:
# AUTHOR: Chalmer Lowe
# DESCRIPTION:

# Given the word list (words.txt) associated with this
#     puzzle** and the target word: 'octopus'
#     0) identify the 10 words "closest"* to the target word
#     1) count the total number of characters in the 10
#        words
#
# NOTE: The Python Standard Library provides a specific
#     tool to identify close matches between strings.
#     (There is NO need to install 3rd party libraries
#      such as NLTK.)

# For example, given this list and the target word 'help':
# ['hello', 'help', 'hide', 'hem', 'heft', 'them', 'heel']

# The following words are the three words most closely
#     matched sequentially to the target word 'help'.

# * help
# * hell
# * hello

# * NOTE: The definition of 'closest' in this case is based on
#         the parameters defined by the Python Standard Library
#         that I used to solve the puzzle. It will almost assuredly
#         differ if you use a 'roll-your-own' algorithm OR a 3rd party library.
# ** NOTE: The word list was derived from
#         /usr/share/dict/words on a Mac

# Put your code here:

# IMPORTS ==============================================
import difflib

with open('words.txt') as fin:
    words = fin.readlines()
    words = [word.strip() for word in words]
    top_ten = difflib.get_close_matches('octopus', words, n=9)
    total = sum(len(word) for word in top_ten)

    print("Total number of characters: ", total)
    # Answer 63
