#usr/bin/python3.4

import sys
from progressbar import ProgressBar
from collections import defaultdict, Counter

def main(argv):
	dutchfile = open('valuelookup.txt', 'r')
	englishfile = open('valuereference.txt', 'r')
	infoboxtypefile = open('instance-types_nl.nt', 'r')
	resultfile = open(argv[1], 'a')
	print("Opening files: complete!")

	matchDict = defaultdict(list)
	infoboxDict = {}
	matchList = []

	for line in infoboxtypefile:
		splitlineType = line.split()
		infoboxDict[splitlineType[0]] = splitlineType[2]
	infoboxtypefile.close()

	for dutchline in dutchfile:
		splitlineDut = dutchline.split()
		matchDict[splitlineDut[0] + ' ' + splitlineDut[2]].append([infoboxDict.get(splitlineDut[0]), splitlineDut[1]])
	dutchfile.close()

	for engline in englishfile:
		splitlineEng = engline.split()
		matchDict[splitlineEng[0] + ' ' + splitlineEng[2]].append([splitlineEng[1]])
	englishfile.close()
	print("Creating dictionaries: complete!")

	for value in matchDict.values():
		if len(value) == 2 and len(value[1]) == 1 and len(value[0]) == 2:
			triple = '{}	{:<60}	dbpedia-owl:sameAs	{:<60}'.format(value[0][0], value[0][1], value[1][0])
			matchList.append(triple)
		

	matchCounts = Counter(matchList)
	for item in matchList:
		if matchCounts[item] == 1:
			pass
			#del matchCounts[item]
	propertySet = set(matchCounts)
	for triple in propertySet:
		resultfile.write(triple + "\n")


if __name__ == '__main__':
	main(sys.argv)
