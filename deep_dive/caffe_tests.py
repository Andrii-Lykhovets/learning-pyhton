from deep_dive.caffe_functions import boil_eggs


def check_equal(actual_result, expected_result):
    if actual_result == expected_result:
        print('passed, ' + expected_result)
    else:
        print('failed, expected "' + expected_result + '", but received "' + actual_result + '"')


test1 = boil_eggs(yolk_state='hard', eggs_quantity='1')
expected1 = '1 hard egg(s)'
check_equal(test1, expected1)

test2 = boil_eggs(yolk_state='soft', eggs_quantity='4')
expected2 = '4 soft egg(s)'
check_equal(test2, expected2)

test3 = boil_eggs(yolk_state='liquid', eggs_quantity='4')
expected3 = '4 liquid egg(s)'
check_equal(test3, expected3)

test4 = boil_eggs(yolk_state='liquid', eggs_quantity='-2')
expected4 = 'error, eggs quantity should be a positive number'
check_equal(test4, expected4)

test5 = boil_eggs(yolk_state='liquid', eggs_quantity='0')
expected5 = '0 liquid egg(s)'
check_equal(test5, expected5)
