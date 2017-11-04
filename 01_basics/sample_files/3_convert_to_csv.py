# opening two files:
#     one as input
#     one as output

fin = open('../datasets/server_location.txt', 'r')
fout = open('../datasets/server_location.csv', 'w')

# in this case, notice: I changed the target variable... to row...
# for loops should use variable names that make code easy to read/understand
for row in fin:
    # replace each example of a pipe '|' with a comma ','
    # replace is another example of the built in capabilities associated with
    # strings, that make it easy for you to do routine tasks
    output = row.replace('|', ',')

    # write each revised line to the output file
    fout.write(output)

# close the file when we are finished going through each line
fout.close()
