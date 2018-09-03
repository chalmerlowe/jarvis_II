list1 = range(1000)
list2 = range(1000)

nl = []

for number in list1:
    for num in list2:
        product = number * num
        nl.append(product)

print(len(nl))
            
