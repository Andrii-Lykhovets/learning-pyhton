def good_order_discount(orders):
    """
    The function gives a 5% discount to all orders equal or above 1000.
    Then it prints a list of orders with discounts when applicable.
    """
    orders_with_discount = list()
    for price in orders:
        discount = price - (price * 0.05)
        if price >= 1000:
            orders_with_discount.append(discount)
        else:
            orders_with_discount.append(price)
    print(orders_with_discount)


day1_orders = [999, 2000, 10, 1005]
day2_orders = [250, 1200, 100, 1000]

good_order_discount(day1_orders)
# prints: [999, 1900.0, 10, 954.75]

good_order_discount(day2_orders)
# prints: [250, 1140.0, 100, 950.0]
