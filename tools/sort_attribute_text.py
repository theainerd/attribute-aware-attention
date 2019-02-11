attribute_name_file = '../data/Anno/list_attr_cloth.txt'
f1 = open(attribute_name_file, 'rb')
f = open("list_attr_cloth_new.txt",'wb')
for line in f1.readlines():
	f.writelines(line)