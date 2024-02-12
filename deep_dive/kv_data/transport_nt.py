from collections import namedtuple

Vehicle = namedtuple('Vehicle', 'brand model type wheels power speed')
transport = [
    Vehicle('Bugatti', 'Veyron', 'car', 4, 1001, 431),
    Vehicle('Ford', 'Ks', 'car', 4, 93, 155),
    Vehicle('Brompton', 'Line A', 'bicycle', 2, 1, 40),
    Vehicle('BMW', 'R Ninet', 'motorcycle', 2, 109, 200),
    Vehicle('Boesch', '620 Bimini', 'boat', 0, 320, 50),
    Vehicle('HondaJet', 'Echelon', 'airplane', 3, None, 833),
]

TravelEstimate = namedtuple("TravelEstimate", "brand model time")
# time in hours

def time_to_travel(distance_km, vehicles):
    """
   The function should iterate through each transport
   Calculate how much time would it take to travel the given distance (in km).
   Time = distance/speed
   :param distance_km:
   :param vehicle_nt:
   :return: [TravelEstimate...]
   """
    time = distance_km/Vehicle.speed


estimate = time_to_travel(10, vehicle)
print(estimate)
# TravelEstimate(brand='Bugatti', model='Veyron', time=0.025...
