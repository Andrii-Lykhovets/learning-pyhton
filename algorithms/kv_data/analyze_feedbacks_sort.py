# 1. magine that you analyze feedbacks for products in the Apple company
# 2. Calculate how many feedbacks are actually for Apple products. What are the unique products?
# 3. Exclude non Apple products. How many non apple products were there?
# 4. What are the top 3 most popular products?*
# 5. What are the top 3 least popular products?*
# 6. Given list (300):


def print_filter_results(all_product_records, unique_product_records, list_of_products):
    print(f'All products({len(all_product_records)}):')
    print(all_product_records)
    print(f'Unique products({len(unique_product_records)}):')
    print(unique_product_records)
    print(f'Non apple products: {len(list_of_products) - len(all_product_records)}')


def filter_known_products(list_of_products):
    known_product_records = ['ios subscription', 'iPhone', 'apple news', 'air pod', 'apple music', 'apple subscription',
                             'mac', 'apple watch', 'iPad', 'apple tv', 'iTunes']
    all_product_records = []
    unique_product_records = set()

    for record in list_of_products:
        if record in known_product_records:
            all_product_records.append(record)
            unique_product_records.add(record)

    print_filter_results(all_product_records, unique_product_records, list_of_products)
    return all_product_records


def count_product_mentions(all_product_records):
    mentions = dict()
    for item in all_product_records:
        mentions[item] = mentions.get(item, 0) + 1

    print(f'mentions: {mentions}')
    return mentions


def find_most_popular_products(mentions, top_count=3):
    most_popular = dict(sorted(mentions.items(), key=lambda item: item[1], reverse=True)[0:top_count])  # а можно [0:-2]
    print(f'most popular products: {most_popular}')
    return most_popular


def find_least_popular_products(mentions, min_count=3):
    least_popular = dict(sorted(mentions.items(), key=lambda item: item[1])[0:min_count])
    print(f'least popular products: {least_popular}')
    return least_popular


def analyze_feedbacks(list_of_products):
    all_product_records = filter_known_products(list_of_products)
    mentions = count_product_mentions(all_product_records)
    find_most_popular_products(mentions)
    find_least_popular_products(mentions)


feedbacks = [
    'apple music', 'ios subscription', 'Fish and chips', 'trololo', 'Fish and chips', 'Fish and chips', 'iPhone',
    'Big Mac', 'iPhone',
    'ios subscription', 'Fish and chips', 'apple news', 'Fish and chips', 'Fish and chips', 'air pod',
    'ios subscription', 'Fish and chips', 'Fish and chips', 'Fish and chips', 'ios subscription', 'Fish and chips',
    'ios subscription', 'iPhone', 'Fish and chips', 'ios subscription', 'apple music', 'Big Mac', 'ios subscription',
    'Fish and chips', 'Big Mac', 'ios subscription', 'Big Mac', 'apple subscription', 'mac', 'trololo',
    'Fish and chips', 'Big Mac', 'Fish and chips', 'ios subscription', 'ps5', 'Fish and chips', 'apple news', 'trololo',
    'Big Mac', 'apple subscription', 'Big Mac', 'ps5', 'ios subscription', 'apple watch',
    'Fish and chips', 'ios subscription', 'Fish and chips', 'Fish and chips', 'Fish and chips', 'trololo', 'apple news',
    'ios subscription', 'Fish and chips', 'ps5', 'ios subscription', 'Fish and chips', 'Big Mac', 'Fish and chips',
    'Big Mac', 'Fish and chips', 'Fish and chips', 'Fish and chips', 'Fish and chips', 'Big Mac', 'Fish and chips',
    'Fish and chips', 'ps5', 'ios subscription', 'Fish and chips', 'Fish and chips', 'Big Mac', 'Fish and chips',
    'Fish and chips', 'Big Mac', 'iPhone', 'apple news', 'trololo', 'Fish and chips', 'Fish and chips', 'Big Mac',
    'Fish and chips', 'trololo', 'Fish and chips', 'Fish and chips', 'ios subscription', 'ios subscription',
    'Fish and chips', 'ios subscription', 'Fish and chips', 'Big Mac', 'ios subscription', 'Fish and chips', 'air pod',
    'Fish and chips', 'Big Mac', 'Big Mac', 'Fish and chips', 'apple music', 'Big Mac', 'Fish and chips',
    'Fish and chips', 'ps5', 'Big Mac', 'Fish and chips', 'Fish and chips', 'Fish and chips', 'Fish and chips',
    'Fish and chips', 'ios subscription', 'Big Mac', 'ios subscription', 'ios subscription', 'apple music',
    'ios subscription', 'Fish and chips', 'iPad', 'Fish and chips', 'Fish and chips', 'apple subscription',
    'apple news', 'Fish and chips', 'Big Mac', 'Fish and chips', 'apple tv', 'Big Mac', 'Fish and chips',
    'Fish and chips', 'Fish and chips', 'Fish and chips', 'Big Mac', 'Fish and chips', 'ios subscription', 'Big Mac',
    'Fish and chips', 'Fish and chips', 'Fish and chips', 'Fish and chips', 'Fish and chips', 'Fish and chips',
    'Fish and chips', 'Fish and chips', 'ios subscription', 'ios subscription', 'Big Mac', 'Fish and chips',
    'ios subscription', 'Big Mac', 'ios subscription', 'Fish and chips', 'bmw', 'Fish and chips', 'Fish and chips',
    'ps5', 'Big Mac', 'Fish and chips', 'ios subscription', 'Fish and chips', 'Fish and chips', 'Fish and chips',
    'Fish and chips', 'iPhone', 'apple watch', 'Fish and chips', 'Fish and chips', 'Fish and chips', 'Fish and chips',
    'Fish and chips', 'air pod', 'ios subscription', 'Fish and chips', 'Fish and chips', 'trololo', 'Fish and chips',
    'ios subscription', 'Fish and chips', 'Fish and chips', 'Fish and chips', 'trololo', 'Fish and chips', 'Big Mac',
    'apple watch', 'Fish and chips', 'Big Mac', 'iPhone', 'ps5', 'Fish and chips', 'Fish and chips', 'Fish and chips',
    'Big Mac', 'Fish and chips', 'Fish and chips', 'Fish and chips', 'apple subscription', 'Big Mac', 'Fish and chips',
    'Fish and chips', 'Big Mac', 'ios subscription', 'iPhone', 'apple tv', 'ps5', 'ios subscription', 'Big Mac',
    'ios subscription', 'ios subscription', 'Fish and chips', 'Fish and chips', 'ios subscription', 'blueberry',
    'iPhone', 'Big Mac', 'Fish and chips', 'ios subscription', 'Fish and chips', 'Fish and chips', 'Fish and chips',
    'Fish and chips', 'Fish and chips', 'Fish and chips', 'Fish and chips', 'Fish and chips', 'Fish and chips',
    'trololo', 'apple news', 'ios subscription', 'Fish and chips', 'Fish and chips', 'Fish and chips', 'Fish and chips',
    'Big Mac', 'Fish and chips', 'iPhone', 'ios subscription', 'Fish and chips', 'Fish and chips', 'ios subscription',
    'Big Mac', 'Big Mac', 'Fish and chips', 'Big Mac', 'air pod', 'Fish and chips', 'Fish and chips', 'Fish and chips',
    'ios subscription', 'Big Mac', 'Fish and chips', 'Big Mac', 'blueberry', 'Fish and chips', 'Fish and chips',
    'Fish and chips', 'Fish and chips', 'Fish and chips', 'Fish and chips', 'Fish and chips', 'ps5', 'Big Mac',
    'ios subscription', 'Fish and chips', 'ios subscription', 'iPhone', 'Fish and chips', 'Big Mac', 'Big Mac',
    'ios subscription', 'Fish and chips', 'Fish and chips', 'Fish and chips', 'Fish and chips', 'Fish and chips', 'ps5',
    'Fish and chips', 'ios subscription', 'Fish and chips', 'Big Mac', 'Fish and chips', 'Fish and chips',
    'ios subscription', 'trololo', 'Fish and chips', 'Big Mac', 'apple tv', 'Fish and chips', 'apple tv',
    'Fish and chips', 'Fish and chips', 'Fish and chips', 'Fish and chips', 'Fish and chips', 'Big Mac',
    'Fish and chips', 'Fish and chips', 'Fish and chips', 'Fish and chips'
]
analyze_feedbacks(feedbacks)
