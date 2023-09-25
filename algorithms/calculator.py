def calculate(number1, number2, operation):
      if operation == 'add':
            result = number1 + number2
      elif operation == 'subtract':
            result = number1 - number2
      elif operation == 'divide':
            result = number1 / number2
      elif operation == 'multiply':
            result = number1 * number2
      return result


print('Hello! \n'
      'I am your calculator.'
      )
number1 = int(input('\tPlease enter a digit:'))
operation = input('\tPlease select your operation \n \tadd, subtract, divide, multiply:')
number2 = int(input('\tPlease enter another digit:'))
calc_result = calculate(number1, number2, operation)

print(str(calc_result))
