# NOTE: due to the inclusion of several key features,
#       this script requires Python version x.x to run

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

import json
from collections import defaultdict


def cleaner(token):
    return token.replace(" ", "")


def ispalindromic(token):
    return token == token[::-1]


def isminipalindromic(token):
    return ispalindromic(token[:3]) and ispalindromic(token[3:])


def isrising(token):
    current = token[0]
    for digit in token[1:]:
        if digit < current:
            return False
        current = digit
    return True


def isfalling(token):
    return isrising(token[::-1])


token_types = ["pal", "mini", "rising", "falling", "normal"]
counter = defaultdict(int)
matches = 0
normal = 0

with open("rsa_token_values_II.json") as fin:
    data = json.load(fin)
    for item in data:
        token = cleaner(item["token"])
        cat = item["cat"]

        if ispalindromic(token):
            counter["pal"] += 1
            normal += 1
            if cat == 1:
                matches += 1

        if isminipalindromic(token):
            counter["mini"] += 1
            normal += 1
            if cat == 2:
                matches += 1

        if isrising(token):
            counter["rising"] += 1
            normal += 1
            if cat == 3:
                matches += 1

        if isfalling(token):
            counter["falling"] += 1
            normal += 1
            if cat == 4:
                matches += 1

        if normal == 0:
            counter["normal"] += 1
            if cat == 5:
                matches += 1

        normal = 0

print("Token Type\tCount")
for key, value in counter.items():
    print(f"{key:16}{value:>5}")

print(f"Matches: {matches}")
