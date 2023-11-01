def print_first_2_parts(text, delimiter):
    """
    Description
    """
    pr_w_del = text.split(delimiter)[:2]
    new_list = list()
    for part in pr_w_del:
        new_list.append(part.strip())
    result = ' '.join(new_list)
    print(result)
    return result


if __name__ == '__main__':
    song = 'Old MacDonald had a farm Ee i ee i o'
    print_first_2_parts(text=song, delimiter=' ')
    # space in quotes
    # prints:
    # "Old MacDonald"

    journal_text = 'On October 3, 2015, Jeff Smith, marketing director at Intel, traveled to 14 Appian Way in Rome, Italy.'
    print_first_2_parts(text=journal_text, delimiter=',')
    # comma in quotes
    # prints:
    # "On October 3 2015"
