#usr/bin/python3.4

#from progressbar import ProgressBar
from collections import defaultdict

def main():
	dutchfile = open('valuelookup.txt', 'r')
	englishfile = open('valuereference.txt', 'r')

	dutchlines = defaultdict(list)
	englishlines = defaultdict(list)

	for line in dutchfile:
		splitline=line.split()
		dutchlines[splitline[0]].append((splitline[1],splitline[2]))
		
	for line in englishfile:
		splitline=line.split()
		englishlines[splitline[0]].append((splitline[1],splitline[2]))
			
	dutchfile.close()
	englishfile.close()

	propertyList = []
	propertySet = set()
#	pbar = ProgressBar()

	for keyD, linelistD in dutchlines.items(): #pbar(dutchlines):
		for keyE,linelistE in englishlines.items():
			for tuplesD in dutchlines.get(keyD):
				for tuplesE in englishlines.get(keyE):
					print(tuplesE)
			
				value = '{:<60} dbpedia-owl:sameAs {}'.format()
				propertySet.add(value)

	for triple in propertySet:
		print(triple)


if __name__ == '__main__':
	main()
