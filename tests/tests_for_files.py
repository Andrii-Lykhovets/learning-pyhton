from algorithms.sep_oct.only_first_letters_are_capitalized import only_first_letters_are_capitalized
from algorithms.sep_oct.print_first_2_parts import print_first_2_parts
from algorithms.sep_oct.good_flat_price import good_flat_price
from algorithms.sep_oct.calculator import calculate

# Tests for only_first_letters_are_capitalized


def test_no_changes():
    journal_text = 'This Perfect Sentence Will Not Change'
    actual = only_first_letters_are_capitalized(text=journal_text)
    assert actual == journal_text


def test_capitalized():
    song = 'oLD MacDonald HAD a farm'
    expected = "Old Macdonald Had A Farm"
    actual = only_first_letters_are_capitalized(text=song)
    assert actual == expected

# Tests for print_first_2_parts


def test_song():
    song = 'Old MacDonald had a farm Ee i ee i o'
    expected = "Old MacDonald"
    actual = print_first_2_parts(text=song, delimiter=' ')
    assert actual == expected


def test_journal_text():
    journal_text = 'On October 3, 2015, Jeff Smith, marketing director at Intel, traveled to 14 Appian Way in Rome, Italy.'
    expected = "On October 3 2015"
    actual = print_first_2_parts(text=journal_text, delimiter=',')
    assert actual == expected


# Tests for good_flat_price


def test_deal1():
    actual = good_flat_price(1700, 15, 1500, 17)
    expected = "The second flat is a better deal."
    assert actual == expected


def test_deal2():
    actual = good_flat_price(1500, 17, 1700, 15)
    expected = "The first flat is a better deal."
    assert actual == expected


def test_deal3():
    actual = good_flat_price(1000, 33, 1000, 33)
    expected = "Both flats have the same cost."
    assert actual == expected


# Tests for calculator


def test_add():
    actual = calculate(number1=10, number2=2, operation='add')
    expected = 12
    assert actual == expected


def test_subtract():
    actual = calculate(number1=10, number2=2, operation='subtract')
    expected = 8
    assert actual == expected


def test_multiply():
    actual = calculate(number1=10, number2=2, operation='multiply')
    expected = 20
    assert actual == expected


def test_divide():
    actual = calculate(number1=10, number2=2, operation='divide')
    expected = 5
    assert actual == expected
