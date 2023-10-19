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


def sandwich_recipe(amount_of_sandwiches, stuffing, pickles_quantity):
    print('Take ' + amount_of_sandwiches + ' piece(s) of bread.')
    print('Put your ' + stuffing + ' on the bread.')
    if int(pickles_quantity) > 0:
        print('Put ' + pickles_quantity + ' pickles on your ' + stuffing + '.')
    print('Cover it with another piece of bread.')
    if int(pickles_quantity) > 0:
        return amount_of_sandwiches + ' sandwich(es) with ' + stuffing + ' and ' + pickles_quantity + ' pickles'
    else:
        return amount_of_sandwiches + ' sandwich(es) with ' + stuffing


def make_orders():
    print('What would you like to order: boiled egg, sandwich or coffee? Type stop to finish an order:')
    making_order = True
    orders = []

    while making_order:
        an_order = input()
        if an_order == 'stop':
            making_order = False
        else:
            orders.append(an_order)

    return orders


def confirm_orders(an_order):
    print('Your order is: ' + str(an_order))


def cook_orders(orders_list):
    cooked_orders = []
    for an_order in orders_list:
        cooked_orders.append(cook_an_order(an_order))
    return cooked_orders


def cook_an_order(an_order):
    if an_order == 'boiled egg':
        return boil_eggs(yolk_state='hard', eggs_quantity='3')
    elif an_order == 'sandwich':
        return sandwich_recipe('1', 'meat', '4')
    elif an_order == 'coffee':
        print('Making coffee')
        return 'Cup of coffee'
    else:
        print('I\'m sorry we don\'t serve ' + an_order)
        exit()


def prepare_the_bill(orders_list):
    total_price = 0
    for an_order in orders_list:
        if an_order == 'boiled egg':
            print('boiled egg price is 6 CHF')
            total_price = total_price + 6
        elif an_order == 'sandwich':
            print('sandwich price is 4 CHF')
            total_price = total_price + 4
        elif an_order == 'coffee':
            print('coffee price is 3 CHF')
            total_price = total_price + 3
    print('Total: ' + str(total_price))


print('Welcome to the caffe!')
orders = make_orders()
confirm_orders(orders)
results = cook_orders(orders)
print('Here is your order ' + str(results))
prepare_the_bill(orders)
