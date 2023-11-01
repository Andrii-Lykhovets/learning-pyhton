def good_flat_price(
   rental1, daily_transport1, rental2, daily_transport2
):
    """
    The function compares 2 options and calculates their budget.
    """
    deal1 = rental1 + daily_transport1*30
    deal2 = rental2 + daily_transport2*30
    if deal1 < deal2:
        result = 'The first flat is a better deal.'
    elif deal2 < deal1:
        result = 'The second flat is a better deal.'
    else:
        result = 'Both flats have the same cost.'
    print(result)
    return result


good_flat_price(1700, 15, 1500, 17)
# Prints: "The second flat is a better deal"

good_flat_price(1500, 17, 1700, 15)
# Prints: "The first flat is a better deal"

good_flat_price(1000, 33, 1000, 33)
# Prints: "Both flats have the same cost"
