attribute_name_file = '../data/Anno/list_attr_cloth.txt'
f = open(attribute_name_file, 'rb')
f1 = open('list_attr_cloth.txt', 'w')
i = 0
for line in f.readlines():
	if i<10000:
		f1.write(line)
		i = i+1