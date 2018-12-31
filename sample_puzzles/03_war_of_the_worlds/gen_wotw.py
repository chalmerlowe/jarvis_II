import hashlib

fin = open('war_of_the_worlds.txt')

keywords = 'brave courageous daring heroism resolve'.split()

for index, line in enumerate(fin, 1):
    words = line.strip().split()
    for word in words:
        if word in keywords:
            keywords.remove(word)
            hash_object = hashlib.sha256(line.strip().encode())
            print((words.index(word), hash_object.hexdigest()))