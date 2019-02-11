attribute_name_file = '../data/Anno/list_attr_cloth.txt'
with open('../data/Anno/list_attr_cloth.txt') as f:
    lines = f.readlines()
    print(lines)
    with open("list_attr_cloth_new.txt", "w") as f1:
        f1.writelines(lines)