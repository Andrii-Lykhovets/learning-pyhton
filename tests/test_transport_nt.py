from collections import namedtuple

import pytest

from deep_dive.kv_data.transport_nt import (time_to_travel, can_park_transport, can_cross, print_name,
                                            tire_pressure_maintenance_price, get_slowest_median_fastest)

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
xiaomi = Vehicle('Xiaomi', 'Mi 1S', 'e_scooter', 2, 0.25, 25)
eurocopter = Vehicle('Eurocopter', 'AS350 B3', 'helicopter', 0, None, 287)
panamera = Vehicle('Porche', 'Panamera', 'car', 4, 348, 315)
model_s = Vehicle('Tesla', 'Model S', 'car', 4, 1000, 322)
transport = [bugatti, ford, brompton, bmw, boesch, honda_jet, xiaomi, eurocopter, panamera, model_s]


def test_result_not_empty():
    estimate = time_to_travel(10, vehicles=transport)
    assert len(estimate) > 0


def test_zero_km():
    estimate = time_to_travel(0, vehicles=transport)
    assert estimate == 'Error: distance must be above 0'


def test_negative_km():
    estimate = time_to_travel(-10, vehicles=transport)
    assert estimate == 'Error: distance must be above 0'


# tests for can_park_transport function:
@pytest.mark.parametrize('vehicle,expected', [
    (bugatti, True),
    (ford, True),
    (brompton, True),
    (bmw, True),
    (boesch, False),
    (honda_jet, False),
    (xiaomi, True),
    (eurocopter, False),
    (panamera, True),
    (model_s, True),
])
def test_car_parking(vehicle, expected):
    can_park = can_park_transport(parking_space='car parking', vehicle=vehicle)
    assert can_park == expected


@pytest.mark.parametrize('vehicle,expected', [
    (bugatti, False),
    (ford, False),
    (brompton, False),
    (bmw, False),
    (boesch, True),
    (honda_jet, False),
    (xiaomi, False),
    (eurocopter, False),
    (panamera, False),
    (model_s, False),
])
def test_can_park_transport_function(vehicle, expected):
    can_park = can_park_transport(parking_space='seaport', vehicle=vehicle)
    assert can_park == expected


@pytest.mark.parametrize('vehicle,expected', [
    (bugatti, False),
    (ford, False),
    (brompton, True),
    (bmw, True),
    (boesch, False),
    (honda_jet, False),
    (xiaomi, True),
    (eurocopter, False),
    (panamera, False),
    (model_s, False),
])
def test_can_park_transport_function(vehicle, expected):
    can_park = can_park_transport(parking_space='street parking', vehicle=vehicle)
    assert can_park == expected


@pytest.mark.parametrize('vehicle,expected', [
    (bugatti, False),
    (ford, False),
    (brompton, False),
    (bmw, False),
    (boesch, False),
    (honda_jet, True),
    (xiaomi, False),
    (eurocopter, True),
    (panamera, False),
    (model_s, False),
])
def test_can_park_transport_function(vehicle, expected):
    can_park = can_park_transport(parking_space='airport hangar', vehicle=vehicle)
    assert can_park == expected


@pytest.mark.parametrize('vehicle,expected', [
    (bugatti, False),
    (ford, False),
    (brompton, True),
    (bmw, True),
    (boesch, False),
    (honda_jet, False),
    (xiaomi, True),
    (eurocopter, True),
    (panamera, False),
    (model_s, False),
])
def test_can_park_transport_function(vehicle, expected):
    can_park = can_park_transport(parking_space='park area', vehicle=vehicle)
    assert can_park == expected


# u can delete it but not yet
@pytest.mark.parametrize('parking_space,vehicle,expected', [
    ('seaport', panamera, False),
    ('seaport', brompton, False),
    ('street parking', bmw, True),
    ('airport hangar', bmw, False),
    ('seaport', boesch, True),
    ('airport hangar', boesch, False),
    ('airport hangar', honda_jet, True),
    ('seaport', honda_jet, False),
    ('street parking', xiaomi, True),
    ('seaport', xiaomi, False),
    ('airport hangar', eurocopter, True),
    ('seaport', eurocopter, False),
])
def test_can_park_transport_function(parking_space, vehicle, expected):
    can_park = can_park_transport(parking_space=parking_space, vehicle=vehicle)
    assert can_park == expected


# tests for can_cross function:
@pytest.mark.parametrize('vehicle,expected', [
    (bugatti, True),
    (ford, True),
    (brompton, True),
    (bmw, True),
    (boesch, False),
    (honda_jet, False),
    (xiaomi, True),
    (eurocopter, False),
    (panamera, True),
    (model_s, True),
])
def test_can_cross_function(vehicle, expected):
    crosses = can_cross(terrain='asphalt road', vehicle=vehicle)
    assert crosses == expected


@pytest.mark.parametrize('vehicle,expected', [
    (bugatti, True),
    (ford, True),
    (brompton, True),
    (bmw, True),
    (boesch, False),
    (honda_jet, False),
    (xiaomi, False),
    (eurocopter, False),
    (panamera, True),
    (model_s, True),
])
def test_can_cross_function(vehicle, expected):
    crosses = can_cross(terrain='grass', vehicle=vehicle)
    assert crosses == expected


@pytest.mark.parametrize('vehicle,expected', [
    (bugatti, False),
    (ford, False),
    (brompton, True),
    (bmw, False),
    (boesch, False),
    (honda_jet, False),
    (xiaomi, True),
    (eurocopter, False),
    (panamera, False),
    (model_s, False),
])
def test_can_cross_function(vehicle, expected):
    crosses = can_cross(terrain='pavement', vehicle=vehicle)
    assert crosses == expected


@pytest.mark.parametrize('vehicle,expected', [
    (bugatti, False),
    (ford, False),
    (brompton, False),
    (bmw, False),
    (boesch, True),
    (honda_jet, True),
    (xiaomi, False),
    (eurocopter, True),
    (panamera, False),
    (model_s, False),
])
def test_can_cross_function(vehicle, expected):
    crosses = can_cross(terrain='ocean', vehicle=vehicle)
    assert crosses == expected


@pytest.mark.parametrize('vehicle,expected', [
    (bugatti, False),
    (ford, False),
    (brompton, False),
    (bmw, False),
    (boesch, False),
    (honda_jet, True),
    (xiaomi, False),
    (eurocopter, True),
    (panamera, False),
    (model_s, False),
])
def test_can_cross_function(vehicle, expected):
    crosses = can_cross(terrain='mountain', vehicle=vehicle)
    assert crosses == expected


def test_car_vs_asphalt():
    crosses = can_cross(terrain='asphalt road', vehicle=ford)
    assert crosses


def test_car_vs_mountain():
    crosses = can_cross(terrain='mountain', vehicle=ford)
    assert not crosses


def test_car_vs_asphalt_road():
    crosses = can_cross(terrain='asphalt road', vehicle=model_s)
    assert crosses


def test_car_vs_ocean():
    crosses = can_cross(terrain='ocean', vehicle=model_s)
    assert not crosses


def test_bicycle_vs_asphalt():
    crosses = can_cross(terrain='asphalt road', vehicle=brompton)
    assert crosses


def test_bicycle_vs_mountain():
    crosses = can_cross(terrain='mountain', vehicle=brompton)
    assert not crosses


def test_motorcycle_vs_grass():
    crosses = can_cross(terrain='grass', vehicle=bmw)
    assert crosses


def test_motorcycle_vs_ocean():
    crosses = can_cross(terrain='ocean', vehicle=bmw)
    assert not crosses


def test_boat_vs_ocean():
    crosses = can_cross(terrain='ocean', vehicle=boesch)
    assert crosses


def test_boat_vs_grass():
    crosses = can_cross(terrain='grass', vehicle=boesch)
    assert not crosses


def test_airplane_vs_ocean():
    crosses = can_cross(terrain='ocean', vehicle=honda_jet)
    assert crosses


def test_airplane_vs_grass():
    crosses = can_cross(terrain='grass', vehicle=honda_jet)
    assert not crosses


def test_e_scooter_vs_road():
    crosses = can_cross(terrain='asphalt road', vehicle=xiaomi)
    assert crosses


def test_e_scooter_vs_grass():
    crosses = can_cross(terrain='grass', vehicle=xiaomi)
    assert not crosses


def test_helicopter_vs_mountain():
    crosses = can_cross(terrain='mountain', vehicle=eurocopter)
    assert crosses


def test_helicopter_vs_grass():
    crosses = can_cross(terrain='grass', vehicle=eurocopter)
    assert not crosses


# tests for print_name function
def test_print_name_honda_jet():
    assert print_name(honda_jet) == 'HONDAJET Echelon'


def test_print_bugatti():
    actual = print_name(vehicle=bugatti)
    expected = 'BUGATTI Veyron'
    assert actual == expected


def test_print_ford():
    actual = print_name(vehicle=ford)
    expected = 'FORD Ks'
    assert actual == expected


def test_print_brompton():
    actual = print_name(vehicle=brompton)
    expected = 'BROMPTON Line a'
    assert actual == expected


def test_print_bmw():
    actual = print_name(vehicle=bmw)
    expected = 'BMW R ninet'
    assert actual == expected


def test_print_boesch():
    actual = print_name(vehicle=boesch)
    expected = 'BOESCH 620 bimini'
    assert actual == expected


def test_print_honda_jet():
    actual = print_name(vehicle=honda_jet)
    expected = 'HONDAJET Echelon'
    assert actual == expected


def test_print_xiaomi():
    actual = print_name(vehicle=xiaomi)
    expected = 'XIAOMI Mi 1s'
    assert actual == expected


def test_print_eurocopter():
    actual = print_name(vehicle=eurocopter)
    expected = 'EUROCOPTER As350 b3'
    assert actual == expected


def test_print_panamera():
    actual = print_name(vehicle=panamera)
    expected = 'PORCHE Panamera'
    assert actual == expected


def test_print_model_s():
    actual = print_name(vehicle=model_s)
    expected = 'TESLA Model s'
    assert actual == expected


# tests for tire_pressure_maintenance_price function
def test_tire_pressure_model_s():
    actual = tire_pressure_maintenance_price(vehicle=model_s)
    expected = 8
    assert actual == expected


def test_tire_pressure_bicycle():
    actual = tire_pressure_maintenance_price(vehicle=brompton)
    expected = 1
    assert actual == expected


def test_tire_pressure_airplane():
    actual = tire_pressure_maintenance_price(vehicle=honda_jet)
    expected = 150
    assert actual == expected


def test_tire_pressure_scooter():
    actual = tire_pressure_maintenance_price(vehicle=xiaomi)
    expected = 1
    assert actual == expected


def test_tire_pressure_boesch():
    actual = tire_pressure_maintenance_price(vehicle=boesch)
    expected = 'A vehicle must have wheels to calculate maintenance'
    assert actual == expected


@pytest.mark.parametrize('letter', ['a', 'b', 'c'])
def test_parameters(letter):
    print(letter)


@pytest.mark.parametrize('first,second,third', [
    ('a', 'b', 'c'),
    ('x', 'y', 'z'),
    ('q', 42, True)
])
def test_multiple_parameters(first, second, third):
    print(f'1: {first}, 2: {second}, 3: {third}')


# Tests for get_slowest_median_fastest Function:
vehicles = [
    Vehicle('Toyota', 'Corolla', 'Sedan', 4, 140, 70),
    Vehicle('Honda', 'Civic', 'Hatchback', 4, 130, 1000),
    Vehicle('Ford', 'Fiesta', 'Compact', 4, 120, 60)
]


def test_get_slowest_median_fastest():
    actual = get_slowest_median_fastest(vehicles=vehicles)
    expected = Vehicle(brand='Ford', model='Fiesta', type='Compact', wheels=4, power=120, speed=60)
            Vehicle(brand='Toyota', model='Corolla', type='Sedan', wheels=4, power=140, speed=70)
            Vehicle(brand='Honda', model='Civic', type='Hatchback', wheels=4, power=130, speed=1000)

    assert actual == expected
