
myname = input('what do you call yourself? ')
counter = 0

while counter <= 10:
    print(myname)
    counter += 1

while True:
    print(myname)
    if counter == 20:
        break
    counter += 1

myage = input('how old are you? ')

for tempvariable in range(int(myage)):
    print(tempvariable)

print('This should count up to ' + myage)
