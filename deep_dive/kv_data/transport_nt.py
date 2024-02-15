from collections import namedtuple

Parking_Space = namedtuple('Parking_Space', 'type')
park_area = Parking_Space('park area')
car_parking = Parking_Space('car parking')
street_parking = Parking_Space('street parking')
airport_hangar = Parking_Space('airport hangar')
seaport = Parking_Space('seaport')

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
    if vehicle.type == 'car' and parking_space == 'car parking':
        return True
    if vehicle.type == 'bicycle' in vehicle and parking_space.type == 'park area' in parking_space:
        return True
    if vehicle.type == 'motorcycle' in vehicle and parking_space.type == 'street parking' in parking_space:
        return True
    if vehicle.type == 'boat' in vehicle and parking_space.type == 'seaport' in parking_space:
        return True
    if vehicle.type == 'airplane' in vehicle and parking_space.type == 'airport hangar' in parking_space:
        return True
    else:
        return False


Terrain = namedtuple('Terrain', 'grass water pavement asphalt_road ocean mountain')


def can_cross(terrain, vehicle):
    while terrain[3]:
        if vehicle.type[2]:
            return True
        else:
            return False


PrintName = namedtuple('PrintName', 'brand model')


def print_name(vehicle):
    """
    Prints and returns 'brand model' string
    """
    names = []
    for vhc in vehicle:
        name_pair = f'{vhc.brand} + {vhc.model}'
        names.append(PrintName(name_pair))
    # return names
    print(names)


print_name(vehicle=Vehicle)
