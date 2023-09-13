# test
print("please enter your login and password")

login = input("Enter your login:")
password = input("Enter your password:")
print("login = " + login + " password = " + password)


def login_password_check(log, pas):
    return login == log and password == pas


# user 1
if (login_password_check("user_andrew", "qwe123")
        or login_password_check("user_kevin", "asd456")
        or login_password_check("user_julia", "zxc789")
        or login_password_check("user_alex", "poi098")
        or login_password_check("user_helen", "lkj765")):
    print('Welcome to admin page ' + login)
else:
    print("Wrong login or password")
print("surprise")
