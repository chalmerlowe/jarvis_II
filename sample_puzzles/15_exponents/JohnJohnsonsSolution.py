#Lazy man's solution
totals_dic = {2:0,3:0,4:0,5:0}
for i in range(1,10001):
    for divisor in totals_dic:
        if i % divisor==0:
            totals_dic[divisor]+=i**divisor
sum = 0
for divisor in totals_dic:
    sum+=totals_dic[ divisor ]
    print( str(divisor)+': '+str(totals_dic[ divisor ]) )
print( 'total: '+str(sum) )
