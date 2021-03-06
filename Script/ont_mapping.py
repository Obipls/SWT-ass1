#usr/bin/python3.4

import sys
from progressbar import ProgressBar
from collections import defaultdict

def main(argv):
	dutchfile = open('valuelookup.txt', 'r')
	englishfile = open('valuereference.txt', 'r')
	infoboxtypefile = open('instance-types_nl.nq', 'r')
	resultfile = open(argv[1], 'a')
	print("Opening files: complete!", file=sys.stderr)

	dutchlines = defaultdict(list)
	englishlines = defaultdict(list)
	infoboxtypelines = defaultdict()

	for line in infoboxtypefile:
		typesplitline = line.split()
		infoboxtypelines[typesplitline[0]] = str(typesplitline[2][29:-1])
	infoboxtypefile.close()

	for dutchline in dutchfile:
		splitlineDut = dutchline.split()
		if splitlineDut[0] in infoboxtypelines.keys():
			dutchlines[splitlineDut[0] + str(infoboxtypelines[splitlineDut[0]])].append((splitlineDut[1], splitlineDut[2]))
	dutchfile.close()

	
	for engline in englishfile:
		splitlineEng = engline.split()
		if splitlineEng[0] in infoboxtypelines.keys():
			englishlines[splitlineEng[0] + str(infoboxtypelines[splitlineEng[0]])].append((splitlineEng[1], splitlineEng[2]))	
	englishfile.close()
	print("Creating dictionaries: complete!", file=sys.stderr)

	propertySet = set()
	pbar = ProgressBar()

	for keyD in pbar(dutchlines.keys()):
		for keyE in englishlines.keys():
			if keyD == keyE:
				#print(dutchlines[keyD])
				for tuplesD in dutchlines[keyD]:
					#print(keyD, tuplesD)
					for tuplesE in englishlines[keyD]:
						if tuplesD[1] == tuplesE[1]:
							#print(tuplesD[0], 'dbpedia-owl:sameAs', tuplesE[0])
							#value = tuplesD[0] + ' dbpedia-owl:sameAs ' + tuplesE[0]
							#print(str(keyD).split()[1])
							value = '{},{},{}'.format(tuplesD[0], tuplesE[0], str(keyD).split()[1])
							propertySet.add(value)
							#propertyCounter.update(value)

	for triple in propertySet:
		resultfile.write(triple + "\n")
		#print(triple)

	#print(propertyCounter)
	


if __name__ == '__main__':
	main(sys.argv)