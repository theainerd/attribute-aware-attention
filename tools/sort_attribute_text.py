lines = open('../data/Anno/list_attr_cloth.txt', 'r').readlines()
output = open("../data/Anno/list_attr_cloth.txt", 'w')

for line in sorted(lines, key=lambda line: line.split()[1]):
	print(line)


