import random


def waiting_7(list_of_tries=None, tries=1):
    if list_of_tries is None:
        list_of_tries = []
    list_of_tries.append(tries)
    if random.randint(0, 9) == 7:
        return 7, tries, list_of_tries
    else:
        tries += 1
        return waiting_7(list_of_tries, tries)


def waiting_7_loop():
    tries = 1
    tries_list = [1]
    while random.randint(0, 9) != 7:
        tries += 1
        tries_list.append(tries)
    return 7, tries, tries_list


if __name__ == '__main__':
    result = waiting_7()
    result2 = waiting_7()
    result3 = waiting_7()
    result_loop = waiting_7_loop()
    result_loop2 = waiting_7_loop()
    result_loop3 = waiting_7_loop()
    print('debug point')
