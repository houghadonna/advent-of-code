import csv
from collections import Counter

validCntA = 0
validCntB = 0
validA = False
validB = False

def isAnagramUnique(phrase):
	anaPhrase = []
	for word in phrase:
		letters = list(word)	# Break letters of word into list of characters
		sortedWord = ''.join(sorted(letters, key=str.lower))	# sort list of characters then join them back into a "word" of sorted characters
		anaPhrase.append(sortedWord)	# add new sorted "word" to phrase array
	c = Counter(anaPhrase)
	k = c.most_common()
	if k[0][1] > 1:		# if most common "word" occurs more than once, fail
		return False
	else:
		return True



with open('4_passphrase.txt') as ssv:
	read = csv.reader(ssv, delimiter = " ")
	for phrase in read:
		if validA == True:
			validCntA += 1
		if validB == True:
			validCntB += 1
		validA = True
		validB = True
		c = Counter(phrase)
		k = c.most_common()
		if k[0][1] > 1:
			validA = False
		if isAnagramUnique(phrase) == False:
			validB = False

if validA == True:		# Don't forget to increment if the last phrase is valid dummy
	validCntA += 1
if validB == True:
	validCntB += 1

print(validCntA)
print(validCntB)