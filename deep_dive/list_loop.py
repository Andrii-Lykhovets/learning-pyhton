numbers_list = [9, -8, 1, -2, 3, 0]
for element in numbers_list:
    print(element)

for number in numbers_list:
    print('number: ' + str(number))

for thing in numbers_list:
    print(thing + thing)

for stuff in numbers_list:
    print(str(stuff) + str(stuff))

print('using stuff2')
for stuff2 in numbers_list:
    print(str(stuff2)*2)

for stuff3 in numbers_list:
    if stuff3 >= 0:
        print('positive')
    else:
        print('negative')
