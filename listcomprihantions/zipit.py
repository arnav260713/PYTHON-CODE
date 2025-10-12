list1 = [1, 2, 3, 4]
list2 = ['A', 'B', 'C', 'D']
zipped_list = list(zip(list1, lis2))
print("1. Zipped list:", zipped_list)
reversed_list = list2[::-1]
zipped_reversed = list(zip(list1, zipped_reversed))
print("2. Zipped with second list reversed:", zipped_reversed)
zipped_dict = dict(zip(list1, list2))
print("3. Zipped dictionary:", zipped_dict)