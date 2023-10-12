from admin_page import load_admin_page
from news_page import load_news_page
from subscribe_page import load_subscribe_page

if __name__ == '__main__':
    page_choice = input('Please choose the page to load (admin, news, subscribe):')
    if page_choice == 'admin':
        load_admin_page()
    elif page_choice == 'subscribe':
        load_subscribe_page()
    elif page_choice == 'news':
        load_news_page()
    else:
        print('Page ' + page_choice + ' not found')

