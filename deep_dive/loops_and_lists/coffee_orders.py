# Given: a list of orders for 3 days
# 1. Merge all data into a single set/tuple/list
# To do:
# 1. Return all the coffee types that were ordered each day. Ignore the rest.
# 2. A `day4` list will be created during the homework
# review, thus be ready to quickly adjust the code to support it

day1 = ['Cortado', 'Americano', 'Doppio', 'Espresso', 'Macchiato']
day2 = ['Cortado', 'Espresso', 'Americano']
day3 = ['Americano', 'Espresso', 'Macchiato']
day4 = ['Doppio', 'Espresso']
all_days = [day1, day2, day3, day4]
# print(all_days)
# day1_set = set(day1)
# day2_set = set(day2)
# intersection_result = day1_set.intersection(day2_set)
# print(intersection_result)
# day3_set = set(day3)
# merging_result = intersection_result.intersection(day3_set)
# print(merging_result)
# print(day1_set.intersection(day1_set))


def get_everyday_coffee(days):
    """
    step 1. We tried to intersect first 2 days, but we couldn't bc there's only intersection between a set and sth
    iterable (everything that can be looped)
    step 2. We converted lists to sets
    step 3. We tried step 1 but with sets, and it worked
    step 4. We intersected step 3 result with day3 (there's no other way to intersect more than 2 days at once)
    step 5. We intersected the same element with self to make sure the method we chose works
    step 6. We were thinking how to avoid step repetition and decided to use a list of days
    step 7. We decided day1 as a countdown point. It was accessed with index and immediately cast (changed data type)
    to the set
    step 8. We iterated (ran) all days on the loop
    step 9. We intersected temporary result with each day from the iteration
    step 10. We returned the final result
    :param days: they are the lists (day1 etc.) within a list (all_days)
    :return: intersection of every single day (each list within all_days list)
    """
    result = set(days[0])
    for current_day in all_days:
        result = result.intersection(current_day)
    return result


everyday_coffee = get_everyday_coffee(days=all_days)
print(everyday_coffee)

# day1.extend(day2)
# day1.extend(day3)
# print(f'All days\' orders: {day1}')


def analyze_daily_orders(list_of_orders):
    unique_coffee_orders = set()
    known_coffee_orders = ['Espresso', 'Americano', 'Capuccino', 'Latte', 'Doppio', 'Cortado', 'Macchiato', 'Lungo',
                           'Flat White']
    for order in list_of_orders:
        if order in known_coffee_orders:
            unique_coffee_orders.add(order)

    print(f'Coffee types ordered daily: {unique_coffee_orders}')


# analyze_daily_orders(day1)


# def merge_lists(**list_of_orders):
#     for orders in list_of_orders.items():
#         list_of_orders.add(list_of_orders)
#     print(list_of_orders)
#
#
# merge_lists(day1, day2, day3)


# merge_lists(day1)
