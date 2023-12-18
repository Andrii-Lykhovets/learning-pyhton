def list_numbers_as_text(start, stop):
    """
    If we use range and provide it with 0, 3 then it will generate us the list
    0, 1, 2
    But for this function we need to get number 3 in the end.
    Thus, we can always give a range function incremented stop argument
    """
    if start < 0 or start > 9:
        return 'start parameter is out of range(0, 9)'
    if stop > 9:
        return 'stop parameter must be not greater than 9'
    if start > stop:
        return 'stop parameter is smaller than start parameter'
    text_numbers = list()
    range_stop = stop + 1
    for number in range(start, range_stop):
        text_number = number_to_word(number)
        text_numbers.append(text_number)
    return text_numbers


def number_to_word(number):
    definitions = [
        {'number': 0, 'word': 'zero'},
        {'number': 1, 'word': 'one'},
        {'number': 2, 'word': 'two'},
        {'number': 3, 'word': 'three'},
        {'number': 4, 'word': 'four'},
        {'number': 5, 'word': 'five'},
        {'number': 6, 'word': 'six'},
        {'number': 7, 'word': 'seven'},
        {'number': 8, 'word': 'eight'},
        {'number': 9, 'word': 'nine'},
    ]
    if number in definitions == ['number']:
        return ['word']


def test_a_single_number():
    assert list_numbers_as_text(9, 9) == ['nine']


def test_a_sequence():
    assert list_numbers_as_text(0, 3) == ['zero', 'one', 'two', 'three']


def test_start_is_too_small():
    assert list_numbers_as_text(-1, 3) == 'start parameter is out of range(0, 9)'


def test_start_is_too_big():
    assert list_numbers_as_text(10, 3) == 'start parameter is out of range(0, 9)'


def test_stop_is_too_big():
    assert list_numbers_as_text(0, 10) == 'stop parameter must be not greater than 9'


def test_stop_is_negative():
    assert list_numbers_as_text(0, stop=-9) == 'stop parameter is smaller than start parameter'


def test_stop_is_smaller_than_start():
    assert list_numbers_as_text(5, 4) == 'stop parameter is smaller than start parameter'
