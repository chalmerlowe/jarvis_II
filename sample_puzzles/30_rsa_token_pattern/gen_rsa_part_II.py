# This problem is based on the same scenario as our previous problem
# but the data is stored in a json file: rsa_token_values_II.json 

# As before, there are five main categories associated with 
#     patterns potentially found in the tokens:

#     * 123 321     - category 1: a palindrome if you consider all six numbers
#     * 121 454     - category 2: two mini palindromes, one in each group of three
#                     (they do not need to be identical)
#     * 123 679     - category 3: rising numbers (each subsequent number is equal to 
#                     or larger than the previous number)
#     * 654 321     - category 4: falling numbers (each subsequent number is
#                     equal to or smaller than the previous number)    
#     * 235 156     - category 5: none of the above

# The json file contains a sequence of records
#     with four fields per record:
#     * uid: user id
#     * cat: category (1-5)
#     * score: confidence score (0 (zero confidence) to 10 (high confidence))
#     * token: the RSA token value
# 
#     * The data will look like this:
#     [{uid: 0000, cat: 1, score: 4, token: '123 321'},
#      {uid: 0001, cat: 2, score: 5, token: '121 434'}]

# The objective is to read in the json and answer the following questions:
#     * for each of the five token categories described above, how many
#           were found?
#     * in how many cases does the given token category match
#           the actual token category?

from random import randint, choice, sample 
import json
from gen_utilities import (stitcher, create_user_id,
                           create_score)
NUM_LINES = 1000

numbers = []
for num in range(1000000):
    numbers.append(list(str(num).rjust(6, '0')))

pre_tokens = sample(numbers, NUM_LINES)

with open('rsa_token_values_II.json', 'w') as fout:
    options = {'pal': 1,
               'mini': 2,
               'rising': 3,
               'falling': 4,
               'normal': 5,
              }

    output = []
    for token in pre_tokens:  
        uid = create_user_id()    
        category_name, cat = choice(list(options.items()))
        token = stitcher(token, new_line=False)
        score = create_score()
        record = {'uid': uid,
                  'cat': cat,
                  'score': score,
                  'token': token,
                 }
        output.append(record)
        
    json.dump(output, fout)