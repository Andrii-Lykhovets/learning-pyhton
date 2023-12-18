# Name, ingredients, ordered today
today_orders = [
    {'Name': 'Espresso', 'ingredients': ('espresso'),'amount': 10},
    {'Name': 'Americano', 'ingredients': ('espresso', 'hot water'), 'amount': 7},
    {'Name': 'Latte', 'ingredients': ('espresso', 'steamed milk', 'steamed milk'), 'amount': 5},
    {'Name': 'Cappuccino', 'ingredients': ('espresso', 'steamed milk', 'milk foam'), 'amount': 15}
]
ordered_less_than_10 = []
for coffee in today_orders:
    if coffee['amount'] < 10:  # coffee[2] is ordered_today
        ordered_less_than_10.append(coffee['Name'])  # coffee[0] is Name
print(ordered_less_than_10)

list_has_3_ingredients = []
for coffee in today_orders:
    if len(coffee['ingredients']) == 3:
        list_has_3_ingredients.append(coffee['Name'])
print(list_has_3_ingredients)
