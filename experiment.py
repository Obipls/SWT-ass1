#usr/bin/python3.4

from progressbar import ProgressBar
from collections import defaultdict

def main():
	dutchfile = open('valuelookup.txt', 'r')
	englishfile = open('valuereference.txt', 'r')
	infoboxtypefile = open('instance-types_nl.nq', 'r')

	dutchlines = defaultdict(list)
	englishlines = defaultdict(list)

	for dutchline in dutchfile:
		splitlineDut = dutchline.split()
		for line in infoboxtypefile:
			typeline = line.split()
			if typeline[0] == splitlineDut[0]:
				dutchlines[splitlineDut[0] + ', ' + typeline[2]].append((splitlineDut[1],splitlineDut[2]))
	
	infoboxtypefile.close()
	infoboxtypefile = open('instance-types_nl.nq', 'r')
	for engline in englishfile:
		splitlineEng = engline.split()
		for line in infoboxtypefile:
			typeline = line.split()
			if typeline[0] == splitlineEng[0]:
				englishlines[splitlineEng[0] + ', ' + typeline[2]].append((splitlineEng[1],splitlineEng[2]))
			
	dutchfile.close()
	englishfile.close()
	infoboxtypefile.close()

	print(dutchlines)
	print(englishlines)

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
