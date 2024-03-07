my_list = []
my_list.extend([10,20,30,40])
print(my_list)

my_list.insert(1,15)
print(my_list)
my_list_2 = [50,60,70]
my_list.extend(my_list_2)
print(my_list)
my_list.pop()
print(my_list)
my_list.sort()
print(my_list)
print(my_list.index(30))
