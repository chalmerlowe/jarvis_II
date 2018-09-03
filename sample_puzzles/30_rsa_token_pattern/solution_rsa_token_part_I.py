
def cleaner(token):
    return token.replace(' ', '')

def ispalindromic(token):
    token = cleaner(token)
    if token == token[::-1]:
        return True
    return False

def isminipalindromic(token):
    token = cleaner(token)
    first_half = token[:3]
    last_half = token[3:]
    if (first_half == first_half[::-1] and
        last_half == last_half[::-1]):
        return True
    return False
    
def isrising(token):
    token = cleaner(token)
    current = token[0]
    for digit in token[1:]:
        if digit < current:
            return False
        current = digit    
    return True

def isfalling(token):
    token = cleaner(token)
    reverse_token = token[::-1]
    return isrising(reverse_token)


counter = {}
for item in ['pal', 'mini', 'rising', 'falling']:
    counter[item] = 0
    

with open ('rsa_token_values_I.txt') as fin:
    for line in fin:
        token = line.strip()
        if ispalindromic(token):
            counter['pal'] += 1
            print('pal:', token)
        if isminipalindromic(token):
            counter['mini'] += 1
            print('min:', token)
        if isrising(token):
            counter['rising'] += 1
            print('ris:', token)
        if isfalling(token):
            counter['falling'] += 1
            print('fal:', token)            
print(counter)
        
        