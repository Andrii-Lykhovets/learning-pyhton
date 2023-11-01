from algorithms.sep_oct.only_first_letters_are_capitalized import only_first_letters_are_capitalized


def test_no_changes():
    journal_text = 'This Perfect Sentence Will Not Change'
    actual = only_first_letters_are_capitalized(text=journal_text)
    assert actual == journal_text


def test_capitalized():
    song = 'oLD MacDonald HAD a farm'
    expected = "Old Macdonald Had A Farm"
    actual = only_first_letters_are_capitalized(text=song)
    assert actual == expected
