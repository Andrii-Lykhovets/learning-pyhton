def print_a_name(dog):
    print(f'{dog["name"]} is {dog["age"]} years old.')


def compare_the_age(dog1, dog2):
    if dog1['age'] == dog2['age']:
        print('Same age')
    else:
        print('Different age')


def print_an_owner(dog):
    print(f'{dog["name"]}\'s owner is {dog.get("owner", "unknown")}.')


german_shepherd_Elsa = {
    'breed': 'german shepherd',
    'name': 'Elsa',
    'age': 2,
}

german_shepherd_Rex = {
    'breed': 'german shepherd',
    'name': 'Rex',
    'age': 2,
}

print_a_name(german_shepherd_Elsa)
print_a_name(german_shepherd_Rex)
compare_the_age(german_shepherd_Elsa, german_shepherd_Rex)

german_shepherd_Elsa['owner'] = 'Andrew'
print(german_shepherd_Elsa)

fox_terrier_Jessy = german_shepherd_Elsa.copy()
fox_terrier_Jessy['breed'] = 'fox terrier'
fox_terrier_Jessy['name'] = 'Jessy'
print(fox_terrier_Jessy)
print_an_owner(fox_terrier_Jessy)
print_an_owner(german_shepherd_Rex)
