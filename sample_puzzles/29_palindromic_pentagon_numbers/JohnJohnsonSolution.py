#non-elegant solution without list comprehension
def pentagonnumber( n ):
    return str(int( n*(3*n - 1)/2 ))

def isPalindrome( n ):
    result =  True if n == n[::-1] else False
    return result

for i in range(10000, 0, -1):
    if isPalindrome(pentagonnumber(i)):
        print(pentagonnumber(i))
        break
