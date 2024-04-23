class CoffeeOrder:
    # init is a class constructor, it is called always when a new object is created
    def __init__(self, name, ingredients, amount):
        self.name = name
        self.ingredients = ingredients
        self.amount = amount

    # method is a function in a class:
    def ingredients_number(self):
        return len(self.ingredients)


class CoffeeAccount(CoffeeOrder):
    all_amount = 0

    def __init__(self, name, ingredients, amount):
        super().__init__(name, ingredients, amount) # super is parent (like root thing) and now it's referring to line 3
        CoffeeAccount.all_amount += amount


# here we created objects for class CoffeeOrder
today_orders = [
    CoffeeOrder('Espresso', ('espresso'), 10),
    CoffeeAccount('Americano', ('espresso', 'hot water'), 7),
    CoffeeAccount('Latte', ('espresso', 'steamed milk', 'steamed milk'), 5),
    CoffeeAccount('Cappuccino', ('espresso', 'steamed milk', 'milk foam'), 15),
]

ordered_less_than_10 = []
for coffee in today_orders:
    if coffee.amount < 10:
        ordered_less_than_10.append(coffee.name)
print(ordered_less_than_10)

list_has_3_ingredients = []
for coffee in today_orders:
    if coffee.ingredients_number() == 3:
        list_has_3_ingredients.append(coffee.name)
print(list_has_3_ingredients)

print(f'all coffee amount is {CoffeeAccount.all_amount}')
