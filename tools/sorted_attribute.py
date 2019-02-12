import pandas as pd 

data = pd.read_csv("list_attr_cloth_new.txt",sep = " ",error_bad_lines=False,header=None)
data.columns = ["attr_subclass",'attr_class']
print(data[:4])

