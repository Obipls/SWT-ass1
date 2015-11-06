#usr/bin/python3.4

import sys
from progressbar import ProgressBar

def main(argv):
	oldfile = open(argv[1], 'r')
	newfile = open(argv[2], 'a')

	pbar = ProgressBar()
	for line in oldfile:
		triple = line.split()
		if 'XMLSchema#date' in triple[2]:
			newfile.write(line)

if __name__ == '__main__':
	main(sys.argv)