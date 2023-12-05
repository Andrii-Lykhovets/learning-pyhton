# 1. magine that you analyze feedbacks for products in the Apple company
# 2. Calculate how many feedbacks are actually for Apple products. What are the unique products?
# 3. Exclude non Apple products. How many non apple products were there?
# 4. What are the top 3 most popular products?*
# 5. What are the top 3 least popular products?*
# 6. Given list (300):


def analyze_feedbacks(list_of_products):
    all_product_records = []
    unique_product_records = set()
    known_product_records = ['ios subscription', 'iPhone', 'apple news', 'air pod', 'apple music', 'apple subscription',
                             'mac', 'apple watch', 'iPad', 'apple tv', 'iTunes']

    for record in list_of_products:
        if record in known_product_records:
            all_product_records.append(record)
            unique_product_records.add(record)

    print(f'All products({len(all_product_records)}):')
    print(all_product_records)
    print(f'Unique products({len(unique_product_records)}):')
    print(unique_product_records)
    print(f'Non apple products: {len(list_of_products) - len(all_product_records)}')
    ios_subscription_count = 0
    iphone_count = 0
    apple_news_count = 0
    for item in all_product_records:
        if item == 'ios subscription':
            ios_subscription_count = ios_subscription_count + 1
        elif item == 'iPhone':
            iphone_count = iphone_count + 1
        elif item == 'apple news':
            apple_news_count = apple_news_count + 1
    print('ios subscription occurrence: ', ios_subscription_count)
    print('iPhone: ', iphone_count)
    print('apple news: ', apple_news_count)


feedbacks = [
    'ios subscription', 'Fish and chips', 'trololo', 'Fish and chips', 'Fish and chips', 'iPhone', 'Big Mac', 'iPhone',
    'ios subscription', 'Fish and chips', 'apple news', 'Fish and chips', 'Fish and chips', 'air pod',
    'ios subscription', 'Fish and chips', 'Fish and chips', 'Fish and chips', 'ios subscription', 'Fish and chips',
    'ios subscription', 'iPhone', 'Fish and chips', 'ios subscription', 'apple music', 'Big Mac', 'ios subscription',
    'Fish and chips', 'Big Mac', 'ios subscription', 'Big Mac', 'apple subscription', 'mac', 'trololo',
    'Fish and chips', 'Big Mac', 'Fish and chips', 'ios subscription', 'ps5', 'Fish and chips', 'apple news', 'trololo',
    'Big Mac', 'apple subscription', 'Big Mac', 'ps5', 'ios subscription', 'apple music', 'apple watch',
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
