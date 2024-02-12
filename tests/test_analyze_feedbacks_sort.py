from algorithms.kv_data.analyze_feedbacks_sort import find_most_popular_products, find_least_popular_products


initial_dict = {'apple music': 4, 'ios subscription': 45, 'iPhone': 10, 'apple news': 6, 'air pod': 4,
                    'apple subscription': 4, 'mac': 1, 'apple watch': 3, 'iPad': 1, 'apple tv': 4}


def test_most_popular_products():
    expected = {'ios subscription': 45, 'iPhone': 10, 'apple news': 6}
    actual = find_most_popular_products(initial_dict)
    assert actual == expected


def test_2_popular_products():
    expected = {'ios subscription': 45, 'iPhone': 10}
    actual = find_most_popular_products(initial_dict, top_count=2)
    assert actual == expected


def test_find_least_popular_products():
    expected = {'apple watch': 3, 'iPad': 1, 'mac': 1}
    # command + click on function name шоб посмотреть в каком файле импортим:
    actual = find_least_popular_products(initial_dict)
    assert actual == expected



