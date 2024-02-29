from collections import namedtuple

TravelEstimate = namedtuple("TravelEstimate", "brand model time")


# time in hours


def time_to_travel(distance_km, vehicles):
    """
   The function should iterate through each transport
   Calculate how much time would it take to travel the given distance (in km).
   Time = distance/speed
   :param distance_km:
   :param vehicles:
   :return: [TravelEstimate...]
   """
    if distance_km <= 0:
        return 'Error: distance must be above 0'

    yobneshsya = []
    for vhc in vehicles:
        time = distance_km / vhc.speed
        yobneshsya.append(TravelEstimate(vhc.brand, vhc.model, time))
    return yobneshsya


def can_park_transport(parking_space, vehicle):
    """
   The task of this function is to answer whether I can park this vehicle in this parking_space?
   And return True/False
    """
    return ((vehicle.type == 'car' and parking_space in ['car parking'])
            or (vehicle.type == 'bicycle' and parking_space in ['park area', 'car parking', 'street parking'])
            or (vehicle.type == 'motorcycle' and parking_space in ['park area', 'car parking', 'street parking'])
            or (vehicle.type == 'boat' and parking_space in ['seaport'])
            or (vehicle.type == 'airplane' and parking_space in ['airport hangar'])
            or (vehicle.type == 'e_scooter' and parking_space in ['park area', 'car parking', 'street parking'])
            or (vehicle.type == 'helicopter' and parking_space in ['park area', 'airport hangar']))


def can_cross(terrain, vehicle):
    return ((vehicle.type == 'car' and terrain in ['grass', 'asphalt road'])
            or (vehicle.type == 'bicycle' and terrain in ['grass', 'pavement', 'asphalt road'])
            or (vehicle.type == 'motorcycle' and terrain in ['grass', 'asphalt road'])
            or (vehicle.type == 'boat' and terrain in ['ocean'])
            or (vehicle.type == 'airplane' and terrain in ['ocean', 'mountain'])
            or (vehicle.type == 'e_scooter' and terrain in ['pavement', 'asphalt road'])
            or (vehicle.type == 'helicopter' and terrain in ['ocean', 'mountain']))


def print_name(vehicle):
    """
    Prints and returns 'brand model' string
    """
    names = f'{vehicle.brand.upper()} {vehicle.model.capitalize()}'
    print(names)
    return names


def tire_pressure_maintenance_price(vehicle):
    """
    Return maintenance price, assuming that it takes $2 per wheel to maintain tire pressure.
    Bicycle maintenance price is $0.5 per wheel. Airplane maintenance price is $50.
    :param vehicle:
    :return: maintenance price:
    """
    if vehicle.type == 'car':
        maintenance_price = vehicle.wheels * 2
        return maintenance_price
    elif vehicle.type in ['bicycle', 'e_scooter']:
        maintenance_price = vehicle.wheels * 0.5
        return maintenance_price
    elif vehicle.type == 'airplane':
        maintenance_price = vehicle.wheels * 50
        return maintenance_price
    else:
        error = 'A vehicle must have wheels to calculate maintenance'
        return error
