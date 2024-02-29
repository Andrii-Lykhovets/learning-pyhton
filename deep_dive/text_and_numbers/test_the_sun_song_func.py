from deep_dive.text_and_numbers.the_sun_song_function import third_and_fourth_words

text = 'Here comes the sun; And I say, it\'s alright'


def test_third_and_fourth_words():
    third_and_fourth_word = third_and_fourth_words(text)
    assert third_and_fourth_word == 'the sun'
