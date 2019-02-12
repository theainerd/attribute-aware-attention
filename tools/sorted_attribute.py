#coding=utf-8

import re
import numpy as np

attribute_name_file = '../data/Anno/list_category_img_small.txt'
f1 = open(attribute_name_file, 'rb')
i = 0
for line in f1.readlines():
	if i < 10000:
		f.write(line)
		i = i+1
	else:
		break
