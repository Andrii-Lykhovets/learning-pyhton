# Name, ingredients, ordered today
today_orders = [
    ('Espresso', ('espresso'), 10),
    ('Americano', ('espresso', 'hot water'), 7),
    ('Latte', ('espresso', 'steamed milk', 'steamed milk'), 5),
    ('Cappuccino', ('espresso', 'steamed milk', 'milk foam'), 15),
]
ordered_less_than_10 = []
for coffee in today_orders:
    if coffee[2] < 10:  # coffee[2] is ordered_today
        ordered_less_than_10.append(coffee[0])  # coffee[0] is Name
print(ordered_less_than_10)

list_has_3_ingredients = []
for coffee in today_orders:
    if len(coffee[1]) == 3:
        list_has_3_ingredients.append(coffee[0])
print(list_has_3_ingredients)
