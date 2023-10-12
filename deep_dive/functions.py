def ask_to_boil_an_egg():
    print('1. Take an egg')
    print('2. Put an egg and cold water in a pot')
    print('3. Put a pot on fire')
    print('4. Wait until it boils')
    yolk_state = input('How do you want your yolk: hard or soft?')
    if yolk_state == 'hard':
        print('5. Boil for 5 minutes')
    else:
        print('5. Boil for 3 minutes')
    print('6. Take the egg out')


def boil_eggs(yolk_state, eggs_quantity='1'):
    print('1. Take ' + eggs_quantity + ' egg(s)')
    print('2. Put ' + eggs_quantity + ' egg(s) and cold water in a pot')
    print('3. Put a pot on fire')
    print('4. Wait until it boils')
    if yolk_state == 'hard':
        print('5. Boil for 5 minutes')
    else:
        print('5. Boil for 3 minutes')
    print('6. Take the egg(s) out')
    return eggs_quantity + ' ' + yolk_state + ' egg(s)'


boiled_eggs = list()

result = boil_eggs(yolk_state='soft')
boiled_eggs.append(result)
print('I need more eggs')
result = boil_eggs(yolk_state='hard', eggs_quantity='3')
boiled_eggs.append(result)
print('Out of order')
result = boil_eggs(eggs_quantity='2', yolk_state='soft')
boiled_eggs.append(result)

print('Boiled eggs: ' + str(boiled_eggs))
