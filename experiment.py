#usr/bin/python3.4

import sys
from progressbar import ProgressBar
from collections import defaultdict, Counter

def main(argv):
	dutchfile = open('valuelookup.txt', 'r')
	englishfile = open('valuereference.txt', 'r')
	infoboxtypefile = open('instance-types_nl.nq', 'r')
	resultfile = open(argv[1], 'a')
	print("Opening files: complete!")

	matchDict = defaultdict(list)
	matchList = []

	for dutchline in dutchfile:
		splitlineDut = dutchline.split()
		matchDict[splitlineDut[0] + ' ' + splitlineDut[2]].append(splitlineDut[1])
	dutchfile.close()

	for engline in englishfile:
		splitlineEng = engline.split()
		matchDict[splitlineEng[0] + ' ' + splitlineEng[2]].append(splitlineEng[1])
	englishfile.close()
	print("Creating dictionaries: complete!")


	for value in matchDict.values():
		if len(value) > 1:
			triple = '{:<60} dbpedia-owl:sameAs {:<60}'.format(value[0],value[1])
			matchList.append(triple)

	matchCounts = Counter(matchList)
	for item in matchList:
		if matchCounts[item] == 1:
			pass
			#del matchCounts[item]
	propertySet = set(matchCounts)
	for triple in propertySet:
		resultfile.write(triple + "\n")





	# dutchlines = defaultdict(list)
	# englishlines = defaultdict(list)
	# infoboxtypelines = defaultdict()

	# for line in infoboxtypefile:
	# 	typesplitline = line.split()
	# 	infoboxtypelines[typesplitline[0]] = str(typesplitline[2][29:-1])
	# infoboxtypefile.close()

	# for dutchline in dutchfile:
	# 	splitlineDut = dutchline.split()
	# 	if splitlineDut[0] in infoboxtypelines.keys():
	# 		dutchlines[splitlineDut[0] + ' type:' + str(infoboxtypelines[splitlineDut[0]])].append((splitlineDut[1], splitlineDut[2]))
	# dutchfile.close()

	
	# for engline in englishfile:
	# 	splitlineEng = engline.split()
	# 	if splitlineEng[0] in infoboxtypelines.keys():
	# 		englishlines[splitlineEng[0] + ' type:' + str(infoboxtypelines[splitlineEng[0]])].append((splitlineEng[1], splitlineEng[2]))	
	# englishfile.close()
	# print("Creating dictionaries: complete!")

	# propertySet = set()
	# propertyCounter = Counter()
	# pbar = ProgressBar()

	# for keyD in pbar(dutchlines.keys()):
	# 	for keyE in englishlines.keys():
	# 		if keyD == keyE:
	# 			#print(dutchlines[keyD])
	# 			for tuplesD in dutchlines[keyD]:
	# 				#print(keyD, tuplesD)
	# 				for tuplesE in englishlines[keyD]:
	# 					if tuplesD[1] == tuplesE[1]:
	# 						#print(tuplesD[0], 'dbpedia-owl:sameAs', tuplesE[0])
	# 						#value = tuplesD[0] + ' dbpedia-owl:sameAs ' + tuplesE[0]
	# 						#print(str(keyD).split()[1])
	# 						value = '{:<60} dbpedia-owl:sameAs {:<60} {}'.format(tuplesD[0], tuplesE[0], str(keyD).split()[1])
	# 						#propertySet.add(value)
	# 						propertyCounter.update(value)

	# #for triple in propertySet:
	# #	resultfile.write(triple + "\n")
	# 	#print(triple)

	# print(propertyCounter)
	


if __name__ == '__main__':
	main(sys.argv)
