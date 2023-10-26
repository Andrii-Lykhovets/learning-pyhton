from deep_dive.caffe_functions import make_orders, confirm_orders, cook_orders, prepare_the_bill


print('Welcome to the caffe!')
orders = make_orders()
confirm_orders(orders)
results = cook_orders(orders)
print('Here is your order ' + str(results))
prepare_the_bill(orders)
