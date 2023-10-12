numbers_list = [9, -8, 1, -2, 3, 0]
print(numbers_list)

elements = list()
print('initial elements: ' + str(elements))
for element in numbers_list:
    elements.append(element + 1)
    print('elements: ' + str(elements))
print('final elements: ' + str(elements))

summ = list()
for number in numbers_list:
    summ.append(number + number)
print('summ: ' + str(summ))

result = 0
for summ_element in summ:
    result = result + summ_element
print('result: ' + str(result))

# multiply number by 2. if result is more than 5 save 'much' otherwise save 'little'
simple_math = []
for number2 in numbers_list:
    result = number2 * 2
    if result > 5:
        simple_math.append('much: ' + str(result))
    else:
        simple_math.append('little: ' + str(result))
print('simple_math: ' + str(simple_math))

day_travels = [2, 8, 6, 3, 1, 6, 10]
# each trip is 1.5. each day limit is 9 pounds. you can never spend more than 9 pounds.
# if spent less than 9 pounds 'less' + summ.
# if spent exactly 9 pd 'match'.
# if more 'limit' + summ.
spendings = list()
for trips in day_travels:
    summ = trips * 1.5
    if summ > 9:
        spendings.append('limit: ' + str(summ))
    elif summ < 9:
        spendings.append('less: ' + str(summ))
    else:
        spendings.append('match')
print(spendings)


