import datetime
import operator

file = open('output.csv', 'r')

data = []
bigTime = None
bigIP = None
Bytes= {}

for line in file:
    line = line.strip().split(' ')

    fpacket = datetime.datetime.strptime(line[9], '%Y-%m-%d-%H:%M:%S.%f')
    lpacket = datetime.datetime.strptime(line[10], '%Y-%m-%d-%H:%M:%S.%f')
    fip = line[0]

    delta = lpacket - fpacket

    if not bigTime:
        bigTime = delta
        bigIP = fip
    elif bigTime < delta:
        bigTime = delta
        bigIP = fip

    Bytes[fip] = Bytes.get(fip, 0) + int(line[5])

print(bigTime, bigIP)

print(sorted(Bytes.items(), key=operator.itemgetter(1))[0])
print(sorted(Bytes.items(), key=operator.itemgetter(1))[-1])
