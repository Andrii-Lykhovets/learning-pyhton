import copy


example_list = ['fruits', 'tea', 4, 'tea']
example_list.append(2)
print(example_list)
example_list2 = example_list.copy()
print(example_list2)
example_list3 = copy.deepcopy(example_list)
print(example_list3)
example_list3.clear()
print(example_list3)
print(example_list.count('tea'))
print(example_list.count(4))
example_list2.extend(example_list)
print(example_list2)
example_list4 = example_list.copy()
example_list4.append(example_list)
print(example_list4)
print(example_list2[5])
print(example_list4[5])
print(example_list.index('tea'))
example_list.insert(3, 'juice')
print(example_list)
example_list[2] = 5
print(example_list)
example_list.pop(2)
print(example_list)
example_list.remove('fruits')
print(example_list)
print('tea' in example_list)
print('coffee' in example_list)
print(len(example_list2))
print(len(example_list4))