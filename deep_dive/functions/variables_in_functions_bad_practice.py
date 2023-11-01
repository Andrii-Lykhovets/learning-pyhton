text = 'hi there'
number = 42
example_list = [1, 2, 3]


def print_variables():
    text = 'inside function'
    extra_text = 'this is a bonus'
    print(text)
    print(number)
    print(extra_text)
    example_list.append(4)
    print(example_list)


print_variables()
print(text)
print(number)
print(example_list)
example_list.append(4)
print(example_list)
