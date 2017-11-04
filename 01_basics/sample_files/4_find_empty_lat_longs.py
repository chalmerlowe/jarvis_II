fin = open('../datasets/server_location.txt')

# set several variables to initial counts
countTotal = 0
countEmpty = 0


for line in fin:
    fields = line.split('|')

    # increment one of the counters (this counts each line processed)
    countTotal += 1

    # test to see if both fields are empty (i.e. they contain the empty string)
    if fields[3] == '' and fields[4] == '':

        # count only rows that have both fields empty
        countEmpty += 1


# print out the results...
# NOTE: the print function can print multiple things, seperated by commas
# it will print both string literals and values associated w/ variable labels
print('Total lines: ', countTotal)
print('Empty lines: ', countEmpty)

# we can do math to calculate values
# floats are a number type with decimals
percentage = countEmpty/float(countTotal)

print('Percentage: ', percentage)
