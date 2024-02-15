from collections import namedtuple

from deep_dive.kv_data.transport_nt import time_to_travel, can_park_transport, can_cross

# мы создали namedtuple чтоб присудить каждому элементу field_names значения.
# namedtuple требует конкретное количество значений, потому что он immutable.
# таким образом мы как программисты помогаем себе сделать меньше ошибок.

Vehicle = namedtuple('Vehicle', 'brand model type wheels power speed')
bugatti = Vehicle('Bugatti', 'Veyron', 'car', 4, 1001, 431)
ford = Vehicle('Ford', 'Ks', 'car', 4, 93, 155)
brompton = Vehicle('Brompton', 'Line A', 'bicycle', 2, 1, 40)
bmw = Vehicle('BMW', 'R Ninet', 'motorcycle', 2, 109, 200)
boesch = Vehicle('Boesch', '620 Bimini', 'boat', 0, 320, 50)
honda_jet = Vehicle('HondaJet', 'Echelon', 'airplane', 3, None, 833)
transport = [bugatti, ford, brompton, bmw, boesch, honda_jet]

def test_result_not_empty():
    estimate = time_to_travel(10, vehicles=transport)
    assert len(estimate) > 0


def test_zero_km():
    estimate = time_to_travel(0, vehicles=transport)
    assert estimate == 'Error: distance must be above 0'


def test_negative_km():
    estimate = time_to_travel(-10, vehicles=transport)
    assert estimate == 'Error: distance must be above 0'


def test_car_parking():
    estimate = can_park_transport(parking_space='car parking', vehicle=bugatti)
    expected = True
    assert estimate == expected


def test_car_vs_asphalt():
    estimate = can_cross(terrain='asphalt_road', vehicle='car')
    expected = True
    assert estimate == expected


