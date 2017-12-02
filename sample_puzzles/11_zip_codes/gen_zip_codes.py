# Title: zip_code generator
# Author: Chalmer Lowe
# Filename: gen_zip_code.py
# Usage: gen_zip_code.py
#
# Date: 20171202
# Revision: 0.5
# Python Version: 3.x
# Description:

# TODO:
#     1) create a zip code generator (five and plus four)
#     2) create a distractor generator
#     3) create a content generator
#     4) define an 'answer'
#     5)
#
'''
* count number of zips
* with plus-four
* without plus four
* take the ratio?
* sum all plus fours > average plus fours
* variants
'''

# ===========================================================================

from random import randint, choice, sample, shuffle
import sys
num_lines = int(sys.argv[1])
target_zips = int(num_lines * 0.02) - 5
spacing = int(num_lines / target_zips)


with open('../data/1138090f.fic') as fin:
    words = [word.rstrip().lower() for word in fin.readlines()]

def zip_gen(hyphen=None):
    '''Create a zip code that meets the following criteria:
    * SS nnnnn
    * SS nnnnn-nnnn
    '''

    state_digraphs = '''AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA
        KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK
        OR PA RI SC SD TN TX UT VT VA WA WV WI WY'''.split()

    state = choice(state_digraphs)

    if not hyphen:
        hyphen = choice(['-', ''])

    if hyphen:
        return ''.join([state, ' ', str(randint(10000, 99999)),
                        hyphen, str(randint(1000, 9999))])
    return ''.join([state, ' ', str(randint(10000, 99999))])


def distractor_gen():
    '''Create a distractor that looks like a zip code.
    Examples:
    * 1 > nnnn: four digits but no state and no five digits
    * 2 > nnnnn: five digits but no state
    * 3 > nnnnn-nnnn: five-four digits with hyphen but no state
    * 4 > SS nnnn: states with four digits
    * 5 > SS nnnnnn: states with six digits
    * 6 > SS nnnnn-nnn: states with five digits and hyphen and three digits
    * 7 > SS nnnnn nnnn: states with five digits and four digits, but no hyphen
    '''

    option = str(randint(1, 6))

    options = {'1': str(randint(1000, 9999)),
               '2': str(randint(10000, 99999)),
               '3': zip_gen()[3:],
               '4': zip_gen()[:7],
               '5': zip_gen(hyphen='-')[:8] + str(randint(0, 9)),
               '6': zip_gen()[:-1],
               }

    return options[option]

def line_content_gen(words=words):
    '''Create a sequence of content with fairly random data of all
    sorts.

    numlines = number of lines in the file
    '''

    return sample(words, 8)


with open('output.txt', 'w') as fout:
    text = []
    target_line = spacing
    for x in range(num_lines):
        if x == target_line:
            if 1 == randint(1, 10):
                text.append(zip_gen())
                # print('FOR REALS:', text[0])
            else:
                text.append(distractor_gen())
                # print(text[0])
            target_line += spacing

        text.extend(line_content_gen())
        shuffle(text)
        output = ' '.join(text) + '\n'

        fout.write(output)
        text = []
