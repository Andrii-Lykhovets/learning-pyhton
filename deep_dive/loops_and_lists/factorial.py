# Factorial
# f1 = 1! = 1
# f2 = 2! = 1*2 = 2
# f3 = 3! = 1*2*3 = 6
# f4 = 4! = 1*2*3*4 = 24
# f5 = 5! = 1*2*3*4*5 = 120


def factorial_recursion(number):
    if number == 1:
        return 1
    else:
        return number * factorial_recursion(number - 1)


def factorial_loop(number):
    result = 1
    for number in range(1, number + 1):
        result = number * result
    return result


def test_factorial_of_1():
    assert factorial_recursion(1) == 1
    assert factorial_loop(1) == 1


def test_factorial_of_2():
    assert factorial_recursion(2) == 2
    assert factorial_loop(2) == 2


def test_factorial_of_3():
    assert factorial_recursion(3) == 6
    assert factorial_loop(3) == 6


def test_factorial_of_4():
    assert factorial_recursion(4) == 24
    assert factorial_loop(4) == 24
