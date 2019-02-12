#coding=utf-8

import re
import numpy as np

attribute_name_file = 'list_attr_cloth.txt'
f1 = open(attribute_name_file, 'rb')
f = open("list_attr_cloth_new.txt",'wb')
i = 0
for line in f1.readlines():
	line = line.decode("utf-8")
	while line.replace('  ',' ') != line:
		line = line.replace('   ',' ')
		line = line.replace('  ',' ')
		line = line.replace('  ',' ')
	print(line.strip().split(' '))
	line = str.encode(line)	
	f.write(line)
	i = i+1