# Using file 113809of.fic identify how many words have:
# 1. a consonant-vowel pattern
#     for any number of consonants and vowels (i.e. cv OR cvcv OR cvcvcv OR cvcvcvcv, etc)
# 2. identify the longest such word(s)

fin = open('113809of.fic').readlines()


def pattern_test(word):
    vowels = 'aeiou'

    # test the length of the word: only lengths that are even can match
    #     the cv, cvcv, cvcvcv criteria
    if len(word) % 2 != 0:
        # IF the word is not even, return False
        #    this short circuits out of the function
        return False

    # use slices with a step to pull out just even letters
    #     and to pull out just odd letters
    evens = word[::2]
    odds = word[1::2]

    # test each subset to see if they are only vowels
    #     OR only consonants
    for letter in odds:
        if letter not in vowels:
            # IF any letter in odds is not in vowels, then return False
            #     to short circuit out of the function
            return False
    for letter in evens:
        if letter in vowels:
            # IF any letter in evens is in vowels, then return False
            #     to short circuit out of the function
            return False
    # IF both the vowel and consonant tests pass, the return
    #     the word.
    return word


counter = 0
for line in fin:
    word = line.strip()
    if pattern_test(word):
        counter += 1
        print(word)

print('There are ' + str(counter) + ' words that match a cv... pattern')
