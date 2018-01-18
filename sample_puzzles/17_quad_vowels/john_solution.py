wordcount=0
wordset=set()
with open('words.txt', 'r') as fp:
	for line in fp:
		if line not in wordset and ( line.count('a')+line.count('e')+line.count('i')+line.count('o')+line.count('u') ) > 4:
			wordcount+=1
		wordset.add(line)
print( str(wordcount)+' words have more than 4 vowels and our deduplicated list contains '+str(len(wordset))+' entries.' )
