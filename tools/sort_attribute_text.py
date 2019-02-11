attribute_name_file = '../data/Anno/list_attr_cloth.txt'
f = open(attribute_name_file, 'rb')
f1 = open('list_attr_cloth_new.txt', 'w')
with open("in.txt") as f:
    lines = f.readlines()
    with open("list_attr_cloth_new.txt", "w") as f1:
        f1.writelines(lines)