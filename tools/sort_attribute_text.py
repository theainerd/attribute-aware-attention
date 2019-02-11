#coding=utf-8

import re
import numpy as np

attribute_name_file = '../data/Anno/list_attr_cloth.txt'
f1 = open(attribute_name_file, 'rb')
f = open("list_attr_cloth_new.txt",'wb')
i = 0
for line in f1.readlines():
	print(line)
	f.writelines(line)