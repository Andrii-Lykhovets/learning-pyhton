# One solution
from collections import namedtuple

Vehicle = namedtuple('Vehicle', 'brand model type wheels power speed')
bugatti = Vehicle('Bugatti', 'Veyron', 'car', 4, 1001, 431)
ford = Vehicle('Ford', 'Ks', 'car', 4, 93, 155)
brompton = Vehicle('Brompton', 'Line A', 'bicycle', 2, 1, 40)
bmw = Vehicle('BMW', 'R Ninet', 'motorcycle', 2, 109, 200)
boesch = Vehicle('Boesch', '620 Bimini', 'boat', 0, 320, 50)
honda_jet = Vehicle('HondaJet', 'Echelon', 'airplane', 3, None, 833)
xiaomi = Vehicle('Xiaomi', 'Mi 1S', 'e_scooter', 2, 0.25, 25)
eurocopter = Vehicle('Eurocopter', 'AS350 B3', 'helicopter', 0, None, 287)
panamera = Vehicle('Porche', 'Panamera', 'car', 4, 348, 315)
model_s = Vehicle('Tesla', 'Model S', 'car', 4, 1000, 322)
sikorsky = Vehicle('Sikorsky', 'R-4', 'helicopter', 3, None, 121)
yamaha = Vehicle('Yamaha', 'GRIZZLY 700 EPS', 'quad_bike', 4, None, 104)
rossignol = Vehicle('Rossignol', 'EXPERIENCE 86 TI', 'skis', 0, 0.1, 100)
polaris = Vehicle('Polaris', '650 INDY XCR 128', 'snowmobile', 0, None, 150)

# Define a named tuple for Vehicle
Vehicle = namedtuple('Vehicle', ['brand', 'model', 'type', 'wheels', 'power', 'speed'])


def get_slowest_median_fastest(vehicles):
    # Sort the list of vehicles based on speed
    sorted_vehicles = sorted(vehicles, key=lambda vehicle: vehicle.speed)

    # Calculate the median index
    median = len(sorted_vehicles)
    median_index = median // 2

    # Get the median speed
    median_vehicle = sorted_vehicles[median_index]

    # Retrieve the slowest, median, and fastest vehicles
    slowest = sorted_vehicles[0]
    median = median_vehicle
    fastest = sorted_vehicles[-1]

    # for sorted_vehicle in sorted_vehicles:
    # if sorted_vehicle.speed == median_speed:
    # median = sorted_vehicle
    # break

    # Return the list of named tuples
    return [slowest, median, fastest]  # if median else [slowest, fastest]


# Example usage:
vehicles = [
    Vehicle('Toyota', 'Corolla', 'Sedan', 4, 140, 70),
    Vehicle('Honda', 'Civic', 'Hatchback', 4, 130, 1000),
    Vehicle('Ford', 'Fiesta', 'Compact', 4, 120, 60),
]
vehicles_2 = [
    Vehicle('Ford', 'Fiesta', 'Compact', 4, 120, 60),
    Vehicle('Toyota', 'Corolla', 'Sedan', 4, 140, 70),
    Vehicle('Porche', 'Panamera', 'car', 4, 348, 315),
    Vehicle('Honda', 'Civic', 'Hatchback', 4, 130, 1000),
]

five_vehicles = [
    Vehicle('Tesla', 'Model S', 'car', 4, 1000, 322),
    Vehicle('Sikorsky', 'R-4', 'helicopter', 3, None, 121),
    Vehicle('Yamaha', 'GRIZZLY 700 EPS', 'quad_bike', 4, None, 104),
    Vehicle('Rossignol', 'EXPERIENCE 86 TI', 'skis', 0, 0.1, 100),
    Vehicle('Polaris', '650 INDY XCR 128', 'snowmobile', 0, None, 150),
]

transport = [bugatti, ford, brompton, bmw, boesch, honda_jet, xiaomi, eurocopter, panamera, model_s, sikorsky, yamaha, rossignol, polaris]

result = get_slowest_median_fastest(vehicles)
# for vehicle in result:
#    print(vehicle)
print(result)

print('B R E A K   P O I N T')

results = get_slowest_median_fastest(vehicles_2)
# for vehicle in results:
#     print(vehicle)
print(results)

print('B R E A K   P O I N T')

all_transport_test = get_slowest_median_fastest(transport)
print(all_transport_test)

print('B R E A K   P O I N T')

five_vehicles_test = get_slowest_median_fastest(five_vehicles)
print(five_vehicles_test)
