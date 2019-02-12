#coding=utf-8

import re
import numpy as np

attribute_name_file = '../data/Anno/list_category_img.txt'
f1 = open(attribute_name_file, 'rb')
f = open("list_category_img_small.txt",'wb')
i = 0
for line in f1.readlines():
	if i < 10000:
		line = line.decode("utf-8")
		while line.replace('   ','  ') != line:
			line = line.replace('   ', '  ')
		line = str.encode(line)
		f.write(line)
		i = i+1
	else:
		break

