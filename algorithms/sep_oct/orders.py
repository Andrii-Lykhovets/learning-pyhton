orders = ['burger with sides', 'beer', 'beer', 'burger', 'burger', 'burger', 'beer', 'beer', 'beer']
order_price = list()
for element in orders:
    if element == 'burger':
        order_price.append(12)
    elif element == 'beer':
        order_price.append(6)
    else:
        order_price.append(16)
print('prices: ' + str(order_price))
result = 0
for summ_element in order_price:
    result = result + summ_element
print('result: ' + str(result))
