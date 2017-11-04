# Python comes with "batteries included", which means that many of the most
# common tasks are already builtin

# Python has a collections module that includes
# functions such as the defaultdict function, which enables you
# to create specialized dictionaries quickly and easily that simplify common
# problems, like counting items
from collections import defaultdict

fin = open('../datasets/server_location.txt')

# when you create a new defaultdict, you need to tell it what type of values
# it will hold... in this case integers
cityDictionary = defaultdict(int)

for line in fin:
    fields = line.split('|')
    city = fields[5]

    # the following line checks to see if a city is in the dictionary,
    #     if no, it adds it and sets the count to 1
    #     if yes, it increments the count by 1
    # all of this decision-making happens in the background,
    # without needing to run through a manual set of if/else statements
    cityDictionary[city] += 1

# this sorts the keys in cityDictionaryand then
# loops over each key, one by one...
for key in sorted(cityDictionary):
    # this prints each key and converts the associated value to a string
    # it then prints each string, but does so with some
    # formatting... setting the width of each printed item and tweaking
    # the justification (to the right or left)
    print(key.ljust(36, '_'), str(cityDictionary[key]).rjust(6))
