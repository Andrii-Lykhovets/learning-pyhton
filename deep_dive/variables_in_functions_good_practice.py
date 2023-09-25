from copy import deepcopy

text = 'hi there'
number = 42
example_list = [1, 2, 3]


def print_variables(given_text, given_number, given_list):
    # given_list = list(given_list)
    # given_list = given_list[:]
    # given_list = given_list.copy()
    given_list = deepcopy(given_list)
    inner_text = 'inside function'
    print(inner_text)
    print(given_number)
    print(given_list)
    given_list.append(4)
    print(given_list)
    print(given_text)


print_variables(given_text=text, given_number=number, given_list=example_list)
print(text)
print(number)
print(example_list)
example_list.append(4)
print(example_list)
