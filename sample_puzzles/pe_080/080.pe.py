from math import sqrt
from decimal import Decimal, getcontext

lower_value = 1
upper_value = 101
getcontext().prec = 102

all_vals = []
for num in range(lower_value, upper_value):
    val = Decimal(num).sqrt()
    if val % 1 != 0:
        val = str(val).replace('.', '')
        val = val[:100]
        val = [int(n) for n in val]
        total = sum(val)



        # total = sum(int(n) for n in str(val).replace('.', '')[:100])
        all_vals.append(total)

print(sum(all_vals))
