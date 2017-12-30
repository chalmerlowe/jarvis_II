# TITLE: tri_vowels >> empty_tri_vowels.py
# AUTHOR: Chalmer Lowe
# DESCRIPTION:
# Read all the values from the file words.txt.
# Each line contains a word.
# Each word has one or more vowels
# Deduplicate the words, so only a single copy remains
#     of any words that might have duplicates and count
#     all the words that have three OR more vowels.
#
# For example, if the following words were in the file:
#
# pathogen       > only 3 vowels
# preselecting   > 4 vowels
# spacefaring    > 4 vowels
# pathogen       # Duplicate and only 3 vowels
# adage          > only 3 vowels
# spacefaring    # Duplicate and 4 vowels

# Thus the total word count includes: preselecting, spacefaring
#     for a total of 2.

# ==============================================================
# Your code goes here:

# AIDAN COMMENT:
'''
When reading this I got conflicting information on what to do
Line 9 says words that have 3 or more vowels yet in the example on lines 13-21 it follows the logic that 3 is too few
I'm going to do both so I don't get it wrong and I'm going to assume Y doesn't count as a vowel
'''
file = open('words.txt').read().split('\n')
file = list(set(file))

count3, count4 = 0, 0

for word in file:
    vowels = 0
    for letter in 'aeiou':
        vowels += word.count(letter)
    if vowels > 3:
        count4 += 1
    if vowels >= 3:
        count3 += 1

print('3 or more vowels:', count3)
print('4 or more vowels:', count4)