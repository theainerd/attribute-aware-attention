lines = open('../data/Anno/list_attr_cloth.txt', 'r').readlines()
output = open("../data/Anno/list_attr_cloth.txt", 'w')

for line in sorted(lines, key=itemgetter(0)):
	print(line)


