# open a file
fin = open('../datasets/server_location.txt')

# read each line in the file and process it...
for line in fin:
    # split each line into fields, wherever you find a pipe character: '|'
    fields = line.split('|')

    # each field is stored in a list and indexed (starting at 0, 1, 2...)
    # compare the contents of the specific fields to specific values
    # != means 'not equal to'
    if fields[0] != '31.175.105.171' and fields[5] == 'Portland':
        # clean up the line, by stripping newline characters off the right side
        print(line.rstrip())
