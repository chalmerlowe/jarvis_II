# scrabble project zero

# File 113809of.fic and 113809of.rev.2.fic are different lengths, i.e. contain
# different numbers of words.
# Which file has the extra words?
# What are the extra words?


# open each file and immediately read in all lines
#     stored as lists.
file1 = open('113809of.fic').readlines()
file2 = open('113809of.rev.2.fic').readlines()

# Check the length of each list to ID the longest list.
if len(file1) > len(file2):
    print('File: 1138090f.fic has more words')
else:
    print('File: 1138090f.rev.2.fic has more words')

# For each term in one list, check to see if
#     that same term is in the second list...
#     IF it is, remove it from the second list >>> making the second
#     list shorter and easier to parse...
#     IF the term is not in the second list, simply print it.
for term in file1:
    if term in file2:
        file2.remove(term)
    else:
        print(term)
