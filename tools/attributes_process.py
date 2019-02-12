#coding=utf-8

import re
import numpy as np

# get attribute cluster idx
attribute_name_file = '../data/Anno/list_attr_cloth.txt'
f1 = open(attribute_name_file, 'rb')
start_idxs = []
last_attr = ''

i = 0
for line in f1.readlines():
	line = line.decode("utf-8")
	line = line.strip().replace('\n', '')
	while line.replace('   ','  ') != line:
		line = line.replace('   ', '  ')
	strs = re.split('  ', line)
	if(strs[1]=='1'):
		start_idxs.append(i)
	if(strs[1]=='2'):
		start_idxs.append(i)
	if(strs[1]=='3'):
		start_idxs.append(i)
	if(strs[1]=='4'):
		start_idxs.append(i)
	if(strs[1]=='5'):
		start_idxs.append(i)
	i+= 1

start_idxs.append(i+1)
print(start_idxs)
# a = np.array(start_idxs)
# nums = a[1:]-a[:-1]+1
# print(np.sum(nums))
# print(nums.tolist())

# # transform binary attribute to clustered attribute
# nb_attr = len(start_idxs)-1
# A_all = np.zeros((289222,nb_attr))
# image_attribute_file = 'attributes/list_attribute_image.txt'
# f2 = open(image_attribute_file,'rb')
# for line in f2.readlines():
# 	strs = re.split(' ', line)
# 	img_id = int(strs[0])-1
# 	attr_id = int(strs[1])
# 	is_present = int(strs[2])
# 	for i in range(len(start_idxs)):
# 		if(attr_id<start_idxs[i]):
# 			break
# 		A_all[img_id][i-1] = attr_id-start_idxs[i-1]+1 # 0 mean no attr
# print(A_all[1])

# new_attr_file = 'processed_attributes.txt'
# np.savetxt(new_attr_file,A_all,fmt='%d')
