#usr/bin/python3.4

from progressbar import ProgressBar
from collections import defaultdict

def main():
	dutchfile = open('valuelookup.txt', 'r')
	englishfile = open('valuereference.txt', 'r')

	dutchlines = defaultdict(list)
	englishlines = defaultdict(list)

	for line in dutchfile:
		splitline = line.split()
		dutchlines[splitline[0]].append((splitline[1],splitline[2]))
		
	for line in englishfile:
		splitline = line.split()
		englishlines[splitline[0]].append((splitline[1],splitline[2]))
			
	dutchfile.close()
	englishfile.close()

	propertyList = []
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
