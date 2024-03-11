detailed_list = [
    '\tThe Sun Has Risen Earlier Today'
    '\nEvery 11 years, the sun completes a solar cycle of calm and stormy activity and begins a new one.'
    'The new solar cycle, Solar Cycle 25, officially began in December 2019',
    '\tIt Was Rainy Yesterday Evening'
    '\nAs mentioned earlier, the official beginning of fall is the 21 of September we are approaching the cold season.'
    'The temperatures will be getting lower and the days start getting shorter. Make sure you get your warm clothes.',
    '\tUkraine Won the War.'
    '\nThis is indeed a very happy day for people of Ukraine and for the free world. It is hard to overestimate the '
    'implications of victory of Ukraine which will definitely change the modern history.',
    '\tBirds Are Singing Less.'
    '\nYou might hear birds singing but it is their last days of doing so. As colder days are approaching the birds '
    'tend to get calmer. Additionally, many kinds of birds migrate further south for winter.',
    '\tputin Died.'
    'Even though it might sound cynic, this is good news for masses of people as his office as the president of russia '
    'has resulted in negative dynamic on both russian economy and its international affairs.',
    '\tOne More Piece of News.'
    'As mentioned previously the victory of Ukraine and death of putin would have profound impact on modern politics.'
    'Given that we are facing something that well may result in the civil war in russia.',
    '\tBonus News'
    '\nIn Switzerland it is grape harvest season. During this time shepherds det their cattle down the valley from the'
    ' mountains, vineyards are being harvested and children are sent on holidays for a week.',
    '\tFinal Peace of News'
    '\nThe founder of The Osiris Project Andrew Targaryen has announced the all the final preparations are being made '
    'to present the worlds first flying disc vehicle. As announced it will be in 2024.',
    '\tUnexpected Presentation'
    '\nReferring to the previous piece of news the founder of Osiris Project Andrew Targaryen has started the invasion '
    'of russia with unclear purpose. As reported the flying discs are able to shoot with laser weapons.',
    '\tShocking Coup in russia Yesterday'
    '\nNow it has become clear that Andrew Targaryen was giving unclear announcements about the presentation because '
    'apparently lis target was russia after all. Now it has become aware that Andrew took control of moscow.',
]


def print_summary_if_longer_than_5_words(text):
    # The function takes elements of the detailed_list variable one by one and prints first 5 words of the passage.
    # If the text is shorter it will print Short enough: + text
    parts = text.split()[:5]
    if len(parts) < 5:
        short_enough = True
    else:
        short_enough = False
    result = ' '.join(parts)
    if short_enough:
        result = 'Short enough: ' + result
    print(result)


print_summary_if_longer_than_5_words(text=detailed_list[0])
print_summary_if_longer_than_5_words(text=detailed_list[1])
print_summary_if_longer_than_5_words(text=detailed_list[2])
print_summary_if_longer_than_5_words(text=detailed_list[3])
print_summary_if_longer_than_5_words(text=detailed_list[4])
print_summary_if_longer_than_5_words(text=detailed_list[5])
print_summary_if_longer_than_5_words(text=detailed_list[6])
print_summary_if_longer_than_5_words(text=detailed_list[7])
print_summary_if_longer_than_5_words(text=detailed_list[8])
print_summary_if_longer_than_5_words(text=detailed_list[9])

print_summary_if_longer_than_5_words(text='Hello, World!')


def print_summary_if_longer_than_5_words_v2(text):
    # The function takes elements of the detailed_list variable one by one and prints first 5 words of the passage.
    # If the text is shorter it will print Short enough: + text
    parts = text.split()[:5]
    short_enough = len(parts) < 5

    result = ' '.join(parts)
    if short_enough:
        result = 'Short enough: ' + result
    print(result)


print_summary_if_longer_than_5_words_v2(text=detailed_list[9])
print_summary_if_longer_than_5_words_v2(text='Hello, World!')


def print_summary_if_longer_than_5_words_v_orange(text):
    # The function takes elements of the detailed_list variable one by one and prints first 5 words of the passage.
    # If the text is shorter it will print Short enough: + text
    parts = text.split()[:5]
    result = ' '.join(parts)
    result_len = len(parts)
    if result_len < 5:
        result = 'Short enough: ' + result
    print(result)


print_summary_if_longer_than_5_words_v_orange(text=detailed_list[9])
print_summary_if_longer_than_5_words_v_orange(text='Hello, World!')


def print_summary_if_longer_than_5_words_v3(text):
    # The function takes elements of the detailed_list variable one by one and prints first 5 words of the passage.
    # If the text is shorter it will print Short enough: + text
    # Самый каеф
    parts = text.split()[:5]
    result = ' '.join(parts)
    if len(parts) < 5:
        result = 'Short enough: ' + result
    print(result)


print_summary_if_longer_than_5_words_v3(text=detailed_list[9])
print_summary_if_longer_than_5_words_v3(text='Hello, World!')
