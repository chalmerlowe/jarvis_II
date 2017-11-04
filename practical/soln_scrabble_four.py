# Using file 113809of.fic identify how many words have:
# identify the count of letters in the words:
# 1. which three letters appear most/least frequently
# 1. which which letter occurs most frequently as a double (i.e. 'ee', 'oo', etc)

# Will use pprint to help make the display a little cleaner later
import pprint

fin = open('113809of.fic').readlines()

# Removing the newline character so that they do not get counted and throw off
#     the count of characters
terms = []
for line in fin:
    terms.append(line.strip())

# Counting each of the letters
letters = {}
for term in terms:
    for letter in term:
        letters[letter] = letters.get(letter, 0) + 1

# temp variables to hold the current highest/lowest letter counts AND letters
highest = ['', 0]
second_highest = ['', 0]
third_highest = ['', 0]

lowest = ['', 113809]
second_lowest = ['', 113809]
third_lowest = ['', 113809]


# Mechanism to track the letter(s) with the highest and lowest three counts

for letter, count in letters.items():
    if count > highest[1]:
        third_highest = second_highest
        second_highest = highest
        highest = [letter , count]
    elif count > second_highest[1]:
        third_highest = second_highest
        second_highest = [letter, count]

    if count < lowest[1]:
        third_lowest = second_lowest
        second_lowest = lowest
        lowest = [letter , count]

    elif count < second_lowest[1]:
        third_lowest = second_lowest
        second_lowest = [letter, count]


print('Letters with the highest counts:', highest, second_highest, third_highest, sep='\n')
print('-' * 60)
print('Letters with the lowest counts:', third_lowest, second_lowest, lowest, sep='\n')
print('-' * 60)
pprint.pprint(letters)

digraphs = []
for term in terms:
    for start in range(len(term) - 1):
        digraph = term[start:start+2]
        if len(digraph) == 2:
            if digraph[0] == digraph[1]:
                digraphs.append(digraph)

digraph_count = {}
for digraph in digraphs:
    digraph_count[digraph] = digraph_count.get(digraph, 0) + 1

highest_double = ''
highest_double_count = 0
for dg, count in digraph_count.items():
    if count > highest_double_count:
        highest_double_count = count
        highest_double = dg

print('-' * 60)
print('The double with the highest count is:', highest_double)
pprint.pprint(digraph_count)
