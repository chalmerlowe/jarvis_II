# coding: utf-8
import pickle
from random import randint

output = open('object.p', 'wb')

class obj():
    pass

o = obj()

for n in range(0, 7000, 7):
    name = f'attr_{hex(n)[2:]}'
    o.__setattr__(name, n + randint(0, 5))
    
pickle.dump(o, output)
output.close()
