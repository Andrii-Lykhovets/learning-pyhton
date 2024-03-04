from deep_dive.text_and_numbers.the_sun_song_function import third_and_fourth_words


def test_third_and_fourth_words():
    text = 'Here comes the sun; And I say, it\'s alright'
    third_and_fourth_word = third_and_fourth_words(text)
    assert third_and_fourth_word == 'the sun;'


def test_hello_world():
    text = 'Hello, World!'
    third_and_fourth_word = third_and_fourth_words(text)
    assert third_and_fourth_word == f'The {text} is too short'
