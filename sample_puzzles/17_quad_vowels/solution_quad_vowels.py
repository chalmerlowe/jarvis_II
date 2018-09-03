# TITLE: quad_vowels >> solution_quad_vowels.py
# AUTHOR: Chalmer Lowe
# DESCRIPTION:
# Read all the values from the file: words.txt.
# Each line contains a word.
# Each word has one or more vowels
# Deduplicate the words, so only a single copy remains
#     of any words that might have duplicates and count
#     all the words that have four OR more vowels.
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

def vowel_counter(word):
    vowels = 'aeiou'
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count

with open('words.txt') as fin:
    word_count = 0
    words = set(word.rstrip() for word in fin.readlines())

    for word in words:
        vowels = vowel_counter(word)
        if vowels > 3:
            word_count += 1

print('Answer:', word_count)


# The following solution uses slightly more pythonic and/or potentially
#     more elegant code.

with open('words.txt') as fin:    
    words = set(fin.readlines())
    vowels = 'aeiou'
    
    word_count = 0
    for word in words:
        if sum(1 for letter in word if letter in vowels) >= 4:    
            word_count += 1
    
print('Answer2:', word_count)
