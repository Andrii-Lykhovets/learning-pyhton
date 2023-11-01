def load_news_page():
    print("Welcome to the news blog")
    all_short_news = [
        "\tfirst news: the sun has risen.",
        "\tsecond news: it was rainy yesterday.",
        "\tUkraine won the war.",
        '\tBirds are singing.',
        '\tputin died.',
        '\tOne more piece of news.',
        '\tBonus news',
        '\tFinal peace of news',
    ]

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

    for news in all_short_news[0:3:2]:
        print(news)

    joiner = '\n'

    def append_new_line(text):
        return text + joiner


    def print_summary_if_longer_than_5_words(text):
        # The function takes elements of the detailed_list variable one by one and prints first 5 words of the passage.
        # If the text is shorter it will print Short enough: + text
        parts = text.split()[:5]
        result = ' '.join(parts)
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
    print_summary_if_longer_than_5_words(text=detailed_list[10])


    def print_first_2_parts(text, delimiter):
        # The function accepts any text, splits it into parts by delimiter and prints the first 2 parts in a single line
        delimiter = ' '
        parts = text.split()[:2]
        result = delimiter.join(parts)
        print(result)


    print_first_2_parts(text=detailed_list[0], delimiter=' ')


    def only_first_letters_are_capitalized(text):
        # The function accepts any text and ensures that all first letters are capitalized and the rest is not
        if text == detailed_list[0]:
            return text.upper()
        print(text.upper())


    only_first_letters_are_capitalized()

    # print(
    #     append_new_line(all_short_news[0]) +
    #     append_new_line(all_short_news[1]) +
    #     append_new_line(all_short_news[2])
    # )
    # print(joiner.join(all_short_news))
