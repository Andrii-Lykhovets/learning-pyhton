def third_and_fourth_words(text):
    """
    the function splits a given text by ' '
    then it looks for 3rd and 4th word and prints them
    :return: words
    """
    # split_text = str(text.split(' '))
    # print(str(split_text[2, 3]))

    parts = text.split()[2:4]
    result = ' '.join(parts)
    if len(text) > 3:
        result = f'The {text} is too short'
    print(result)
    return result
