import pandas as pd 

data = pd.read_csv("list_attr_cloth_new.txt",sep = " ",error_bad_lines=False,header=None)
data.columns = ["attr_subclass",'attr_class']
data1 = data.sort_values(by='attr_class', ascending=True)
data1 = data1[["attr_class","attr_subclass"]]
data1 = data1.reset_index(drop=True)
print(data1[:4])
data1.to_csv('list_attr_cloth_new_sorted.txt',sep=' ', index=True, header=False)