def good_flat_price(
   rental1, daily_transport1, rental2, daily_transport2
):
    """
    The function compares 2 options and calculates their budget.
    """


good_flat_price(1700, 15, 1500, 17)
# Prints: "The second flat is a better deal"

good_flat_price(2023, 0, 1500, 17)
# Prints: "The first flat is a better deal"

good_flat_price(2023, 0, 1000, 33)
# Prints: "Both flats have the same cost"
