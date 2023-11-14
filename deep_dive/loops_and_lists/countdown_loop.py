def count_down_loop_v1(start_from):
    """
    The functions counts down from a given number
    While number is greater than 0 it prints it
    At the end of the countdown the function prints call to action
    """
    loop_list = [start_from]
    while start_from > 1:
        start_from -= 1
        loop_list.append(start_from)
    return loop_list


def count_down_loop_v2(start_from):
    """
    The functions counts down from a given number
    While number is greater than 0 it prints it
    At the end of the countdown the function prints call to action
    """
    loop_list = []
    while start_from > 0:
        loop_list.append(start_from)
        start_from -= 1
    return loop_list


def count_down_loop_v3(start_from):
    """
    The functions counts down from a given number
    While number is greater than 0 it prints it
    At the end of the countdown the function prints call to action
    """
    loop_list = []
    for i in range(start_from, 0, -1):
        loop_list.append(i)
    return loop_list


def count_down_recursion(number, recursive_list=None):
    """
    The function counts from a given number down to zero
    The base case occurs when n is zero, at which point recursion stops
    In the recursive call, the argument is one less than the current value of n,
    so each recursion moves closer to the base case
    """
    if recursive_list is None:
        recursive_list = []
    if number > 0:
        recursive_list.append(number)
        return count_down_recursion(number - 1, recursive_list)
    else:
        print(recursive_list)
        return recursive_list


def test_a_single_number():
    start_from = 1
    expected_result = [1]

    assert count_down_loop_v1(start_from) == expected_result
    assert count_down_loop_v2(start_from) == expected_result
    assert count_down_loop_v3(start_from) == expected_result
    assert count_down_recursion(start_from) == expected_result
    assert count_down_loop_v1(start_from) == count_down_recursion(start_from)


def test_from_five():
    start_from = 5
    expected_result = [5, 4, 3, 2, 1]

    assert count_down_loop_v1(start_from) == expected_result
    assert count_down_loop_v2(start_from) == expected_result
    assert count_down_loop_v3(start_from) == expected_result
    assert count_down_recursion(start_from) == expected_result
    assert count_down_loop_v1(start_from) == count_down_recursion(start_from)


def test_from_nine():
    start_from = 9
    expected_result = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    assert count_down_loop_v1(start_from) == expected_result
    assert count_down_loop_v2(start_from) == expected_result
    assert count_down_loop_v3(start_from) == expected_result
    assert count_down_recursion(start_from) == expected_result
    assert count_down_loop_v1(start_from) == count_down_recursion(start_from)
