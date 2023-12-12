# Given: a list of orders for 3 days
# 1. Merge all data into a single set/tuple/list
# To do:
# 1. Return all the coffee types that were ordered each day. Ignore the rest.
# 2. A `day4` list will be created during the homework
# review, thus be ready to quickly adjust the code to support it

day1 = ['Cortado', 'Americano', 'Doppio', 'Espresso', 'Macchiato']
day2 = ['Cortado', 'Espresso', 'Americano']
day3 = ['Americano', 'Espresso', 'Macchiato']

day1.extend(day2)
day1.extend(day3)
print(f'All days\' orders: {day1}')


def analyze_daily_orders(list_of_orders):
    unique_coffee_orders = set()
    known_coffee_orders = ['Espresso', 'Americano', 'Capuccino', 'Latte', 'Doppio', 'Cortado', 'Macchiato', 'Lungo',
                           'Flat White']
    for order in list_of_orders:
        if order in known_coffee_orders:
            unique_coffee_orders.add(order)

    print(f'Coffee types ordered daily: {unique_coffee_orders}')


analyze_daily_orders(day1)


def merge_lists(**list_of_orders):
    for orders in list_of_orders.items():
        list_of_orders.add(list_of_orders)
    print(list_of_orders)


merge_lists(day1, day2, day3)


# merge_lists(day1)
