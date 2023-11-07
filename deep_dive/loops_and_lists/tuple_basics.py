fruits_list = ['apple', 'banana', 'pineapple']
print(fruits_list)
first, second, third = fruits_list
print(second)
print(fruits_list[1])
fruits_list[1] = 'orange'
print(fruits_list)
fruits_tuple = ('apple', 'banana', 'pineapple')
print(fruits_tuple)
first, second, third = fruits_tuple
print(second)
print(fruits_tuple[1])
# fruits_tuple[1] = 'orange' # This line of code will throw an error cause tuple is immutable


def returns_packed_tuple():
    return 1, 2, 3


function_result = returns_packed_tuple()
print(function_result)
print(type(function_result))
first, second, third = returns_packed_tuple()
print(first)
