inputs = ['c', 'e', 'p', 'n']
print('Welcome to the subscription page! \n'
      'Select which personal data would you like to share: email, phone, both or nothing')
inputs[0] = input('Enter your choice:')


def input_and_check_email():
    inputs[1] = input('Enter your email:')
    if '@' in inputs[1]:
        print('Welcome!')
        print('choice:' + inputs[0])
        print('email:' + inputs[1])
    else:
        print('Error! Email has to have @ character')


if inputs[0] == 'email':
    input_and_check_email()


def input_and_check_phone():
    inputs[2] = input('Enter your phone:')
    if inputs[2].startswith('41') or inputs[2].startswith('38'):
        print('Welcome!')
        print('choice:' + inputs[0])
        print('phone:' + inputs[2])
    else:
        print('Error! Phone has to start with 41 or 38')


if inputs[0] == 'phone':
    input_and_check_phone()

elif inputs[0] == 'both':
    input_and_check_email()
    input_and_check_phone()

elif inputs[0] == 'none':
    print('Ok!')
    print('choice:' + inputs[0])
