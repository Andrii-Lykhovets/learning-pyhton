def list_numbers_as_text(start, stop):
    """
    If we use range and provide it with 0, 3 then it will generate us the list
    0, 1, 2
    But for this function we need to get number 3 in the end.
    Thus, we can always give a range function incremented stop argument
    """
    if start < 0 or start > 9:
        return 'start parameter is out of range(0, 9)'
    text_numbers = list()
    range_stop = stop + 1
    for number in range(start, range_stop):
        text_number = number_to_word(number)
        text_numbers.append(text_number)
    return text_numbers


def number_to_word(number):
    if number == 0:
        return 'zero'
    elif number == 1:
        return 'one'
    elif number == 2:
        return 'two'
    elif number == 3:
        return 'three'


def test_a_single_number():
	assert list_numbers_as_text(9, 9) == ['nine']


def test_a_sequance():
	assert list_numbers_as_text(0, 3) == ['zero', 'one', 'two', 'three']


def test_start_is_too_small():
	assert list_numbers_as_text(-1, 3) == 'start parameter is out of range(0, 9)'


def test_start_is_too_big():
	assert list_numbers_as_text(10, 3) == 'start parameter is out of range(0, 9)'
