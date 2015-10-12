#usr/bin/python3.4

def main():
	dutchfile = open('valuelookup.txt', 'r')
	englishfile = open('valuereference.txt', 'r')

	dutchlines = dutchfile.readlines()
	englishlines = englishfile.readlines()

	print(dutchlines)

if __name__ == '__main__':
	main()