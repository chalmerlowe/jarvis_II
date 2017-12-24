# TITLE: tri_vowels >> gen_tri_vowels.py
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

from random import sample, shuffle
percent = 0.10
dupe_percent = 0.30

with open('113809of.fic') as fin:
    words = [word.rstrip() for word in fin.readlines()]
    subset = int(len(words) * percent)

    words = sample(words, subset)
    dupe_subset = int(len(words) * dupe_percent)

    dupes = words[:dupe_subset]
    words = words + dupes + dupes
    shuffle(words)

with open('words.txt', 'w') as fout:
    for word in words:
        output = word + '\n'
        fout.write(output)
