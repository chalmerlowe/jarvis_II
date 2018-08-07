# This problem is based on the same scenario as our previous problem
# but the data is stored in a json file: rsa_token_values_II.json 

# As before, there are several main categories associated with 
#     patterns potentially found in the tokens:

#     * 123 321     - CATEGORY 1: a palindrome if you consider all six numbers
#     * 121 454     - CATEGORY 2: two mini palindromes, one in each group of three
#                     (they do not need to be identical)
#     * 123 669     - CATEGORY 3: rising numbers (each subsequent number is equal to 
#                     or larger than the previous number)
#     * 654 421     - CATEGORY 4: falling numbers (each subsequent number is
#                     equal to or smaller than the previous number)    
#     * 235 156     - CATEGORY 5: none of the above

# The json file contains a sequence of records
#     with four fields per record:
#     * uid: user id
#     * cat: category (1-5)
#     * score: confidence score (0 (zero confidence) to 10 (high confidence))
#     * token: the RSA token value
# 
#     * An example of the data looks like this:
#     [{uid: 0000, cat: 1, score: 4, token: '123 321'},
#      {uid: 0015, cat: 4, score: 5, token: '121 454'},
#      {uid: 0015, cat: 3, score: 7, token: '123 669'},
#      {uid: 0010, cat: 4, score: 3, token: '654 421'},
#      {uid: 0010, cat: 5, score: 9, token: '235 156'},
#      etc...]
#
#      Notice, that in the above sample, the first cat value (1) matches
#      the token category of type 1, but the second cat value (4) does 
#      note match the token category of type 2.


# The objective is to read in the json and answer the following questions:
#     * for each of the five token categories described above, how many
#           were found?
#     * in how many cases does the given token category match
#           the actual token category?

# For our example data, each of the five token categories is found once 
#     but only four of the actual categories match the given cat value.

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