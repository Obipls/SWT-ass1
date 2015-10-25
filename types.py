from collections import Counter
s=set()
dutchfile = open('valuelookup.txt', 'r')
for line in dutchfile:
	s.add(line.split()[1])
print(len(s))