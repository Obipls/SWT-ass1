#usr/bin/python3.4

from progressbar import ProgressBar
from collections import defaultdict

def main():
	dutchfile = open('valuelookup.txt', 'r')
	englishfile = open('valuereference.txt', 'r')
	infoboxtypefile = open('instance-types_nl.nq', 'r')

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
			dutchlines[splitlineDut[0] + ' type:' + str(infoboxtypelines[splitlineDut[0]])].append((splitlineDut[1], splitlineDut[2]))
	dutchfile.close()
	
	for engline in englishfile:
		splitlineEng = engline.split()
		if splitlineEng[0] in infoboxtypelines.keys():
			englishlines[splitlineEng[0] + ' type:' + str(infoboxtypelines[splitlineEng[0]])].append((splitlineEng[1], splitlineEng[2]))	
	englishfile.close()

	propertySet = set()
	pbar = ProgressBar()
	
	for keyD, linelistD in pbar(dutchlines.items()):
		for keyE,linelistE in englishlines.items():
			if keyD == keyE:
				#print(dutchlines[keyD])
				for tuplesD in dutchlines[keyD]:
					#print(keyD, tuplesD)
					for tuplesE in englishlines[keyE]:
						if tuplesD[1] == tuplesE[1]:
							#print(tuplesD[0], 'dbpedia-owl:sameAs', tuplesE[0])
							value = tuplesD[0] + ' dbpedia-owl:sameAs ' + tuplesE[0]
							#value = '{:<60} dbpedia-owl:sameAs {}'.format(tuplesD, tuplesE)
							propertySet.add(value)

	for triple in propertySet:
		print(triple)
	


if __name__ == '__main__':
	main()
