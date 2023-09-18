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

for news in all_short_news[0:3:2]:
    print(news)

joiner = '\n'


def append_new_line(text):
    return text + joiner


# print(
#     append_new_line(all_short_news[0]) +
#     append_new_line(all_short_news[1]) +
#     append_new_line(all_short_news[2])
# )
# print(joiner.join(all_short_news))
