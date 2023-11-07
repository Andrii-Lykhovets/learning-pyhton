def load_admin_page():
    print("please enter your login and password")
    credentials = [
        ("user_andrew", "qwe123"),
        ("user_kevin", "asd456"),
        ("user_julia", "zxc789"),
        ("user_alex", "poi098"),
        ("user_helen", "lkj765"),
    ]

    login = input("Enter your login:")
    password = input("Enter your password:")
    print("login = " + login + " password = " + password)

    def login_password_check(log, pas):
        return login == log and password == pas

    correct_login = False
    for cre_login, cre_password in credentials:
        if login_password_check(cre_login, cre_password):
            correct_login = True

    if correct_login:
        print('Welcome to admin page ' + login)
    else:
        print("Wrong login or password")
    print("surprise")
