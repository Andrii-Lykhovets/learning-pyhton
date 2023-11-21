def swap_des_lettres(first_letter, second_letter, list_of_letters):
    new_list = list_of_letters.copy()
    first_index = new_list.index(first_letter)
    second_index = new_list.index(second_letter)
    new_list[first_index] = second_letter
    new_list[second_index] = first_letter
    return new_list


swap_letters = ['a', 'b', 'c', 'd', 'e', 'g', 'f']
new_letters = swap_des_lettres('g', 'f', swap_letters)
print(new_letters)
print(swap_letters)
