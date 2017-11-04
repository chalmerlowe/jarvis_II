with open('113809of.fic') as fin:
    words = []
    count = 1
    for word in fin.readlines():
        word = word.strip()
        if word.count('a') == 2 and 'e' not in word:
            words.append(word)
            print(count, word)
            count += 1
