# Using file 113809of.fic
# identify how many words start with an 'x'

# open the file and immediately read in all lines
#     stored as lists.
file1 = open('113809of.fic').readlines()

words = []

for term in file1:
    if term.startswith('x'):
        words.append(term)

# You were not asked to display the words, but it is a good idea to
#     look at your data to ensure that it matches your expectations.

print(words)

# NOTE: there is no reason to strip off the newline characters, since
#       all we care about is the first character

print('-' * 60)
print('There are ' + str(len(words)) + ' words that start with "x"')
