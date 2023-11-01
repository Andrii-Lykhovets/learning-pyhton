def sandwich_recipe(amount_of_sandwiches, stuffing, pickles_quantity):
    print('Take ' + amount_of_sandwiches + ' piece(s) of bread.')
    print('Put your ' + stuffing + ' on the bread.')
    if int(pickles_quantity) > 0:
        print('Put ' + pickles_quantity + ' pickles on your ' + stuffing + '.')
    print('Cover it with another piece of bread.')
    if int(pickles_quantity) > 0:
        return amount_of_sandwiches + ' sandwich(es) with ' + stuffing + ' and ' + pickles_quantity + ' pickles'
    else:
        return amount_of_sandwiches + ' sandwich(es) with ' + stuffing


sandwiches = list()
print('Meat Sandwich:')
result = sandwich_recipe('3', 'meat', '4')
sandwiches.append(result)

print('Fish Sandwich:')
result = sandwich_recipe('1', 'fish', '2')
sandwiches.append(result)

print('No Pickles Sandwich')
result = sandwich_recipe('1', 'fish', '0')
sandwiches.append(result)

print('Sandwiches Made: ' + str(sandwiches))
