# First, I create lists
names = ['Billy', 'Kyle', 'Emily', 'Mark', 'Mohammed', 'Aziz', 'Andrew']

text_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']


def print_first_three_even(names):
    return '1. ' + names

# Second, loop through the list
for names in names[1:6:2]:
    print(names)
for text in text_numbers[1:6:2]:
    print(text)

print(print_first_three_even(names))