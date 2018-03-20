list1 = range(1000)
list2 = range(1000)

nl = [number * num for number in list1 for num in list2]

print(len(nl))
            
