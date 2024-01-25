from collections import Counter

known_product_records = ['ios subscription', 'iPhone', 'apple news', 'air pod', 'apple music', 'apple subscription',
                             'mac', 'apple watch', 'iPad', 'apple tv', 'iTunes', 'ios subscription']
print('COUNTER FROM LIST')
counter_from_list = Counter(known_product_records)
print(counter_from_list)
print(f'iPhone: {counter_from_list["iPhone"]}')

print('STANDARD COUNTER')
std_counter = Counter(iphone=2, mac=1)
print(std_counter)
print(f'iPhone: {std_counter["iphone"]}')
print(f'iPad: {std_counter["ipad"]}')

print('COUNTER FROM DICTIONARY')
known_products_dict = {'iPhone': 2, 'mac': 1, 'iPad': 4}
counter_from_dict = Counter(known_products_dict)
print(counter_from_dict)
print(f'iPhone: {counter_from_dict["iPhone"]}')
print(counter_from_dict.most_common())
print(counter_from_dict.most_common(1))
reversed_common = counter_from_dict.most_common()
reversed_common.reverse()
print(reversed_common)
print(reversed_common[0:2])

print('COUNTER FROM SCRATCH')
counter_from_scratch = Counter()
counter_from_scratch.update(['iPhone'])  # like .append in lists
counter_from_scratch.update(['iPhone'])
counter_from_scratch.update(['iPhone'])
counter_from_scratch.update(['iPad'])
most_common = counter_from_scratch.most_common(1)
print(f'most common: {most_common}')
print(counter_from_scratch)
print(f'iPhone: {counter_from_scratch["iPhone"]}')
print(sorted(counter_from_scratch.elements()))
