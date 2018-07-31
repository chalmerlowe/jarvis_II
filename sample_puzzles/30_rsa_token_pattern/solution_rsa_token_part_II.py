import json

#     * 123 321     - category 1: a palindrome if you consider all six numbers
#     * 121 454     - category 2: two mini palindromes, one in each group of three
#                     (they do not need to be identical)
#     * 123 679     - category 3: rising numbers (each subsequent number is equal to 
#                     or larger than the previous number)
#     * 654 321     - category 4: falling numbers (each subsequent number is
#                     equal to or smaller than the previous number)    
#     * 235 156     - category 5: none of the above



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
for item in ['pal', 'mini', 'rising', 'falling', 'normal']:
    counter[item] = 0
    
matches = 0
normal = 0
with open ('rsa_token_values_II.json') as fin:
    data = json.load(fin)
    for item in data:
        token = item['token']
        cat = item['cat']
                
        if ispalindromic(token):
            counter['pal'] += 1
            normal += 1
            if cat == 1:
                matches += 1
        if isminipalindromic(token):
            counter['mini'] += 1
            normal += 1
            if cat == 2:
                matches += 1
        if isrising(token):
            counter['rising'] += 1
            normal += 1
            if cat == 3:
                matches += 1
        if isfalling(token):
            counter['falling'] += 1
            normal += 1
            if cat == 4:
                matches += 1
        if normal == 0:
            counter['normal'] += 1
            if cat == 5:
                matches += 1
            
        normal = 0    
print(counter)
print('Matches: ', matches)        
        