print("Welcome to the news blog")
all_short_news = [
    "\tfirst news: the sun has risen.",
    "\tsecond news: it was rainy yesterday.",
    "\tUkraine won the war.",
]
joiner = '\n'


def print_with_new_line(text):
    return text + joiner


print(
    print_with_new_line(all_short_news[0]) +
    print_with_new_line(all_short_news[1]) +
    print_with_new_line(all_short_news[2])
)
# print(joiner.join(all_short_news))
