range_stop = 5
print('insertion sort loop')
for i in range(1, range_stop):
    for j in range(i, 0, -1):
        print(f'i = {i}, j = {j}')
print('bubble sort loop')
for i in range(range_stop - 1):
    for j in range(0, range_stop - i - 1):
        print(f'i = {i}, j = {j}')
