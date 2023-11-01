transport = ['car', 'bicycle', 'train', 'plane']
transport_length = len(transport)

print('using range')
for index in range(transport_length):
    value = transport[index]
    print(str(index) + ' ' + value)

print('using enumerate')
for i, v in enumerate(transport):
    print(str(i) + ' ' + v)

