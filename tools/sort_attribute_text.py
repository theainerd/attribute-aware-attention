#coding=utf-8

import re
import numpy as np

attribute_name_file = 'list_attr_cloth.txt'
f1 = open(attribute_name_file, 'rb')
f = open("list_attr_cloth_new.txt",'w')
i = 0
for line in f1.readlines():
	line = line.decode("utf-8")
	while line.replace('  ',' ') != line:
		line = line.replace('    ',' ')
		line = line.replace('   ',' ')
		line = line.replace('  ',' ')
	final_list = line.strip().split(' ')
	sentence = ' '.join(final_list)
	print(sentence)
	# line = str.encode(sentence)	
	f.write(sentence)
	i = i+1