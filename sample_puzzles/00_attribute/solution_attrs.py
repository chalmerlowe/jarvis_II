# Solution 0 -----------------------

import pickle

class obj():
    pass

data = open('object.p', 'rb')

my_obj = pickle.load(data)

total = 0

for attr in dir(my_obj):
    if '__' not in attr:
       value = my_obj.__getattribute__(attr)
       
       if value % 2 == 1:
           total += value

print('Answer: {}'.format(total))

# Expected Answer: 1799870

# Solution 1 -----------------------

import pickle

class obj():
    pass

with open('object.p', 'rb') as data:
    my_obj = pickle.load(data)    
    attr_values = [my_obj.__getattribute__(attr) 
                   for attr in dir(my_obj) if '__' not in attr]
    odds = [num for num in attr_values if num % 2 == 1]

print('Answer: {}'.format(sum(odds)))

# Solution 2 ------------------------

import pickle

class obj():
    pass

with open('object.p', 'rb') as data:
    result = 0
    for i, a in enumerate([x for x in dir(my_obj) if '__' not in x]):
        value = my_obj.__getattribute__(a)
        if value % 2 == 1:
            result += value

print('Answer: {}'.format(result))
