from deep_dive.caffe_functions import boil_eggs, cook_an_order, sandwich_recipe


def test_one_hard_egg():
    actual = boil_eggs(yolk_state='hard', eggs_quantity='1')
    expected = '1 hard egg(s)'
    assert actual == expected, 'should boil "1 hard egg"'


def test_4_soft_eggs():
    actual = boil_eggs(yolk_state='soft', eggs_quantity='4')
    expected = '4 soft egg(s)'
    assert actual == expected


def test_4_liquid_eggs():
    actual = boil_eggs(yolk_state='liquid', eggs_quantity='4')
    expected = '4 liquid egg(s)'
    assert actual == expected


def test_negative_quantity():
    actual = boil_eggs(yolk_state='liquid', eggs_quantity='-2')
    expected = 'error, eggs quantity should be a positive number'
    assert actual == expected


def test_zero_eggs():
    actual = boil_eggs(yolk_state='liquid', eggs_quantity='0')
    expected = '0 liquid egg(s)'
    assert actual == expected


def test_cooking_function():
    actual = cook_an_order('boiled egg')
    expected = '3 hard egg(s)'
    assert actual == expected


def test_sandwich_function():
    actual = sandwich_recipe(amount_of_sandwiches='2', stuffing='tuna', pickles_quantity='4')
    expected = '2 sandwich(es) with tuna and 4 pickles'
    assert actual == expected
