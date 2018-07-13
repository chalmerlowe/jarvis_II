# TODO
# it is possible that 'normal' tokens might
#     be accidentally created with one of the
#     four patterns... and then we could
#     end up with a pattern category and pattern 
#     that are out of sync.


from random import randint, choice 
from math import ceil
import json
from gen_utilities import (palindrome, rising_falling, 
                           generic, stitcher, create_user_id,
                           create_score)
NUM_LINES = 1000

# Part II
# Let's take this puzzle to a higher level of difficulty.
# The general principle is the same... we want to categorize and count the 
#     five types of token patterns
#     * However, this time we will read in data stored in a json file that
#       includes additional metadata associated with each of the token values
#     * The metadata will include a UserID (uid), Categorization (cat),
#     *     Confidence_Score (score) and Token (token)
#     * The data will look like this:
#     [{uid: 0000, cat: 1, score: 4, token: '123 321'},
#      {uid: 0001, cat: 2, score: 5, token: '121 434'},
#      {},
#      {}]
#
# Main goal is to read in the json AND count each of the patterns
# 
# Count how many times each pattern occurs and identify the smallest and 
# largest counts (ignore count of items that don't match any category).


with open('rsa_token_values_II.json', 'w') as fout:
    options = {'pal': 1,
               'mini': 2,
               'rising': 3,
               'falling': 4,
               'normal': 5,
              }
    
    output = []
    for item in range(NUM_LINES):
        uid = create_user_id()
        
        category_name, cat = choice(list(options.items()))
        
        if category_name == 'pal':
            token = stitcher(palindrome(), new_line=False)    
        elif category_name == 'mini':
            token = palindrome(3) + palindrome(3)
            token = stitcher(token, new_line=False)
        elif category_name == 'rising':
            token = stitcher(rising_falling(), new_line=False)
        elif category_name == 'falling':
            token = stitcher(rising_falling(rising=False), new_line=False)
        elif category_name == 'normal':
            token = stitcher(generic(), new_line=False)
      
        score = create_score()
        record = {'uid': uid,
                  'cat': cat,
                  'score': score,
                  'token': token,
                 }

        output.append(record)

    json.dump(output, fout)