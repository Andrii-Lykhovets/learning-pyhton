def only_first_letters_are_capitalized(text):
    """
    The function accepts any text and ensures that all first letters are capitalized and the rest is not:
    1. It slices a text parameter, makes it all lower case and capitalizes the first letter of each element;
    2. Then it makes it a string and concatenates all the elements.
    """
    words = text.split()
    capitalized_list = list()
    for word in words:
        capitalized_list.append(word.capitalize())
    result = ' '.join(capitalized_list)
    print(result)
