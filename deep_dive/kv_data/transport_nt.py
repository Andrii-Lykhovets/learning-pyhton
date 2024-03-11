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
    return ((vehicle.type == 'car' and parking_space in ['car parking', 'garage'])
            or (vehicle.type == 'bicycle' and parking_space in ['park area', 'car parking', 'street parking'])
            or (vehicle.type == 'motorcycle' and parking_space in ['park area', 'car parking', 'street parking', 'garage'])
            or (vehicle.type == 'boat' and parking_space in ['seaport'])
            or (vehicle.type == 'airplane' and parking_space in ['airport hangar'])
            or (vehicle.type == 'e_scooter' and parking_space in ['park area', 'car parking', 'street parking'])
            or (vehicle.type == 'helicopter' and parking_space in ['park area', 'airport hangar'])
            or (vehicle.type == 'quad_bike' and parking_space in ['garage'])
            or (vehicle.type == 'skis' and parking_space in ['garage'])
            or (vehicle.type == 'snowmobile' and parking_space in ['garage']))


def can_cross(terrain, vehicle):
    return ((vehicle.type == 'car' and terrain in ['grass', 'asphalt road'])
            or (vehicle.type == 'bicycle' and terrain in ['grass', 'pavement', 'asphalt road'])
            or (vehicle.type == 'motorcycle' and terrain in ['grass', 'asphalt road'])
            or (vehicle.type == 'boat' and terrain in ['ocean'])
            or (vehicle.type == 'airplane' and terrain in ['ocean', 'mountain'])
            or (vehicle.type == 'e_scooter' and terrain in ['pavement', 'asphalt road'])
            or (vehicle.type == 'helicopter' and terrain in ['ocean', 'mountain'])
            or (vehicle.type == 'quad_bike' and terrain in ['mountain', 'asphalt road', 'grass'])
            or (vehicle.type == 'skis' and terrain in ['mountain'])
            or (vehicle.type == 'snowmobile' and terrain in ['mountain']))


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
    elif vehicle.type in ['bicycle', 'e_scooter', 'motorcycle', 'quad_bike']:
        maintenance_price = vehicle.wheels * 0.5
        return maintenance_price
    elif vehicle.type == 'airplane':
        maintenance_price = vehicle.wheels * 50
        return maintenance_price
    elif vehicle.type == 'helicopter' and vehicle.wheels > 0:
        maintenance_price = vehicle.wheels * 50
        return maintenance_price
    else:
        error = 'A vehicle must have wheels to calculate maintenance'
        return error


# Define a named tuple for Vehicle
Vehicle = namedtuple('Vehicle', ['brand', 'model', 'type', 'wheels', 'power', 'speed'])


def get_slowest_median_fastest(vehicles):
    # Sort the list of vehicles based on speed
    sorted_vehicles = sorted(vehicles, key=lambda x: x.speed)

    # Calculate the median index
    median = len(sorted_vehicles)
    median_index = median // 2

    # Get the median speed
    if median % 2 == 0:
        # median_vehicle = (sorted_vehicles[median_index - 1] + sorted_vehicles[median_index]) / 2
        median_vehicle = None # these 2 lines are wrong - need to rethink (там 105 удали и решение на экране)
    else:
        median_vehicle = sorted_vehicles[median_index]

    # Retrieve the slowest, median, and fastest vehicles
    slowest = sorted_vehicles[0]
    median = median_vehicle
    fastest = sorted_vehicles[-1]

    # Return the list of named tuples
    return [slowest, median, fastest]

# Example usage:
vehicles = [
    Vehicle('Toyota', 'Corolla', 'Sedan', 4, 140, 70),
    Vehicle('Honda', 'Civic', 'Hatchback', 4, 130, 1000),
    Vehicle('Ford', 'Fiesta', 'Compact', 4, 120, 60)
]

vehicles1 = [
    Vehicle('Ford', 'Fiesta', 'Compact', 4, 120, 60),
    Vehicle('Toyota', 'Corolla', 'Sedan', 4, 140, 70),
    Vehicle('Porche', 'Panamera', 'car', 4, 348, 315),
    Vehicle('Honda', 'Civic', 'Hatchback', 4, 130, 1000),
]

result = get_slowest_median_fastest(vehicles)
for vehicle in result:
    print(vehicle)

results = get_slowest_median_fastest(vehicles1)
for vehicle in results:
    print(vehicle)
