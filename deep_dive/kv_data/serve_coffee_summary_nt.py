from collections import namedtuple
Order = namedtuple('Order', 'name ingredients amount')
today_orders = [
    Order('Espresso', ('espresso'), 10),
    Order('Americano', ('espresso', 'hot water'), 7),
    Order('Latte', ('espresso', 'steamed milk', 'steamed milk'), 5),
    Order('Cappuccino', ('espresso', 'steamed milk', 'milk foam'), 15),
]

ordered_less_than_10 = []
for coffee in today_orders:
    if coffee.amount < 10:
        ordered_less_than_10.append(coffee.name)
print(ordered_less_than_10)

list_has_3_ingredients = []
for coffee in today_orders:
    if len(coffee.ingredients) == 3:
        list_has_3_ingredients.append(coffee.name)
print(list_has_3_ingredients)
