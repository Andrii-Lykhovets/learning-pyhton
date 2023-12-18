def load_admin_page():
    print("please enter your login and password")
    credentials = [
        {'login': 'user_andrew', 'pass': 'qwe123'},
        {'login': 'user_kevin', 'pass': 'asd456'},
        {'login': 'user_julia', 'pass': 'zxc789'},
        {'login': 'user_alex', 'pass': 'poi098'},
        {'login': 'user_helen', 'pass': 'lkj765'},
    ]

    login = input("Enter your login:")
    password = input("Enter your password:")
    print("login = " + login + " password = " + password)

    def login_password_check(log, pas):
        return login == log and password == pas

    correct_login = False
    for user in credentials:
        if login_password_check(user['login'], user['pass']):
            correct_login = True

    if correct_login:
        print('Welcome to admin page ' + login)
    else:
        print("Wrong login or password")
    print("surprise")
