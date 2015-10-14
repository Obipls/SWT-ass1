#usr/bin/python3.4

from progressbar import ProgressBar

def main():
	dutchfile = open('valuelookup.txt', 'r')
	englishfile = open('valuereference.txt', 'r')

	dutchlines = []
	englishlines = []

	for line in dutchfile:
		dutchlines.append(line.strip().split())
	for line in englishfile:
		englishlines.append(line.strip().split())

	propertyList = []
	propertySet = set()
	pbar = ProgressBar()
	for linelistD in pbar(dutchlines):
		for linelistE in englishlines:
			if linelistD[0] == linelistE[0]:
				if linelistD[2] == linelistE[2]:
					value = '{:<60} dbpedia-owl:sameAs {}'.format(linelistD[1], linelistE[1])
					#print(value)
					#print('{:<60} dbpedia-owl:sameAs {}'.format(linelistD[1], linelistE[1]))
					#if value not in propertyList:
					#	propertyList.append(value)
					propertySet.add(value)
	#print(propertyList)
	for triple in propertySet:
		print(triple)


if __name__ == '__main__':
	main()