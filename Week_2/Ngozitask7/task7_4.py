#4 Unique Member Registration
name1 = input("Enter name(seperated by comma):")
name2 = input("Enter name(seperated by comma):")
name3 = input("Enter name(seperated by comma):")
names = {name1,name2,name3}
set_of_names =set()
for name_list in names :
    set_of_names.update(n.strip()for n in name_list.split(",")if n.strip())

name_length_dict = {name:len(name)for name in set_of_names}
print(name_length_dict)
