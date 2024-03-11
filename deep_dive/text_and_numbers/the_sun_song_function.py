def third_and_fourth_words(text):
    """
    the function splits a given text by ' '
    then it looks for 3rd and 4th word and prints them
    :return: words
    """
    # split_text = str(text.split(' '))
    # print(str(split_text[2, 3]))
    words = text.split()
    if len(words) < 3:
        return f'The {text} is too short'
    parts = words[2:4]
    result = ' '.join(parts)
    print(result)
    return result
