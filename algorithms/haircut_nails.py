print('Welcome to our salon!')


def select_salon_services():
    print('Enter a service that you\'d like: haircut, hair coloring, manicure, head massage? '
          'Type stop to finish an order:')
    giving_service = True
    services = list()
    while giving_service:
        chosen_service = input()
        if chosen_service == 'stop':
            giving_service = False
        else:
            services.append(chosen_service)
    return services


def service_confirmation(services):
    print('Your service is: ' + str(services))


def haircut_tutorial():
    haircut_type = input('How would you like to cut your hair? Long or short:')
    if haircut_type == 'short':
        print('1. Shorten the hair on the sides.')
        print('2. Spray the upper hair with water and cut it with scissors and comb.')
        print('3. Wash the head and style the hair.')
    if haircut_type == 'long':
        print('1. Brush the hair and spray it with water.')
        print('2. Thoroughly cut the ends of hair.')
        print('3. Dry the hair and style it.')
    return haircut_type + ' haircut'


def coloring_tutorial():
    print('What color would you like to dye your hair in: blond, red or black?')
    hair_color = input()
    if input == 'blond':
        print('1. Bleach the hair for 30 minutes.')
        print('2. Rinse the hair properly.')
        print('3. Put the' + str(input) + 'toner on the hair and keep it for 10 minutes.')
        print('4. Rinse the hair, dry, and style it.')
    if input == 'red':
        print('1. Bleach the hair for 30 minutes.')
        print('2. Rinse the hair properly.')
        print('3. Put the' + str(input) + 'toner on the hair and keep it for 10 minutes.')
        print('4. Rinse the hair, dry, and style it.')
    if input == 'black':
        print('1. Bleach the hair for 30 minutes.')
        print('2. Rinse the hair properly.')
        print('3. Put the' + str(input) + 'toner on the hair and keep it for 10 minutes.')
        print('4. Rinse the hair, dry, and style it.')
    print('Here you are! Now your hair is' + str(input))
    return hair_color


def manicure_tutorial():
    print('How would you like your nails: long or short?')
    nails_length = input()
    print('What color would you like your nails to be?')
    polish_color = input()
    print('1. Cut the nails ' + nails_length + '.')
    print('2. Cover them with ' + polish_color + ' polish.')
    return str(nails_length) + ' ' + str(polish_color) + ' manicure.'


def giving_service(service_list):
    given_service = list()
    for chosen_service in service_list:
        given_service.append(giving_chosen_service(chosen_service))
    return given_service


def giving_chosen_service(chosen_service):
    if chosen_service == 'haircut':
        return haircut_tutorial()
    elif chosen_service == 'hair coloring':
        return coloring_tutorial()
    elif chosen_service == 'manicure':
        return manicure_tutorial()
    elif chosen_service == 'head massage':
        print('Giving head massage.')
        return chosen_service
    else:
        print('Sorry we don\'t provide such service as ' + chosen_service)


def chosen_service_price():
    total_price = 0
    for service in ordered_services:
        if service == 'haircut':
            print('haircut price is 40 CHF')
            total_price = total_price + 40
        elif service == 'manicure':
            print('manicure price is 80 CHF')
            total_price = total_price + 80
        elif service == 'hair coloring':
            print('hair coloring price is 120 CHF')
            total_price = total_price + 120
        elif service == 'head massage':
            print('head massage price is 10 CHF')
            total_price = total_price + 10
    print('Total: ' + str(total_price))


ordered_services = select_salon_services()
service_confirmation(ordered_services)
results = giving_service(ordered_services)
print('Here is your order ' + str(results))
chosen_service_price()
