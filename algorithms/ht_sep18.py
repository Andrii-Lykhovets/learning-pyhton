def print_first_three_even(given_list):
    """
    We will slice given_list from 1 to 6th element(excluding)
    with the step 2
    We will print the sliced elements
    """
    for element in given_list[1:6:2]:
        print(element)


chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print_first_three_even(chars)

text_numbers = ['one', 'two', 'three', 'four']
print_first_three_even(text_numbers)
