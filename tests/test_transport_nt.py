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
sikorsky = Vehicle('Sikorsky', 'R-4', 'helicopter', 3, None, 121)
yamaha = Vehicle('Yamaha', 'GRIZZLY 700 EPS', 'quad_bike', 4, None, 104)
rossignol = Vehicle('Rossignol', 'EXPERIENCE 86 TI', 'skis', 0, 0.1, 100)
polaris = Vehicle('Polaris', '650 INDY XCR 128', 'snowmobile', 0, None, 150)
transport = [bugatti, ford, brompton, bmw, boesch, honda_jet, xiaomi, eurocopter, panamera, model_s, sikorsky, yamaha, rossignol, polaris]


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
    (sikorsky, False),
    (yamaha, False),
    (rossignol, False),
    (polaris, False),
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
    (sikorsky, False),
    (yamaha, False),
    (rossignol, False),
    (polaris, False),
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
    (sikorsky, False),
    (yamaha, False),
    (rossignol, False),
    (polaris, False),
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
    (sikorsky, False),
    (yamaha, False),
    (rossignol, False),
    (polaris, False),
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
    (sikorsky, True),
    (yamaha, False),
    (rossignol, False),
    (polaris, False),
])
def test_can_park_transport_function(vehicle, expected):
    can_park = can_park_transport(parking_space='park area', vehicle=vehicle)
    assert can_park == expected


@pytest.mark.parametrize('vehicle,expected', [
    (bugatti, True),
    (ford, True),
    (brompton, False),
    (bmw, True),
    (boesch, False),
    (honda_jet, False),
    (xiaomi, False),
    (eurocopter, False),
    (panamera, True),
    (model_s, True),
    (sikorsky, False),
    (yamaha, True),
    (rossignol, True),
    (polaris, True),
])
def test_can_park_transport_function(vehicle, expected):
    can_park = can_park_transport(parking_space='garage', vehicle=vehicle)
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
    (sikorsky, False),
    (yamaha, True),
    (rossignol, False),
    (polaris, False),
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
    (sikorsky, False),
    (yamaha, True),
    (rossignol, False),
    (polaris, False),
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
    (sikorsky, False),
    (yamaha, False),
    (rossignol, False),
    (polaris, False),
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
    (sikorsky, True),
    (yamaha, False),
    (rossignol, False),
    (polaris, False),
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
    (sikorsky, True),
    (yamaha, True),
    (rossignol, True),
    (polaris, True),
])
def test_can_cross_function(vehicle, expected):
    crosses = can_cross(terrain='mountain', vehicle=vehicle)
    assert crosses == expected


# tests for print_name function
@pytest.mark.parametrize('vehicle,expected', [
    (honda_jet, 'HONDAJET Echelon'),
    (bugatti, 'BUGATTI Veyron'),
    (ford,'FORD Ks'),
    (brompton, 'BROMPTON Line a'),
    (bmw, 'BMW R ninet'),
    (boesch, 'BOESCH 620 bimini'),
    (sikorsky, 'SIKORSKY R-4'),
    (xiaomi, 'XIAOMI Mi 1s'),
    (eurocopter, 'EUROCOPTER As350 b3'),
    (panamera, 'PORCHE Panamera'),
    (model_s, 'TESLA Model s'),
    (yamaha, 'YAMAHA Grizzly 700 eps'),
    (rossignol, 'ROSSIGNOL Experience 86 ti'),
    (polaris, 'POLARIS 650 indy xcr 128'),
])
def test_print_name_honda_jet(vehicle, expected):
    assert print_name(vehicle) == expected


# tests for tire_pressure_maintenance_price function
@pytest.mark.parametrize('vehicle, expected', [
    (honda_jet, 150),
    (bugatti, 8),
    (ford, 8),
    (brompton, 1),
    (bmw, 1),
    (boesch, 'A vehicle must have wheels to calculate maintenance'),
    (sikorsky, 150),
    (xiaomi, 1),
    (eurocopter, 'A vehicle must have wheels to calculate maintenance'),
    (panamera, 8),
    (model_s, 8),
    (yamaha, 2),
    (rossignol, 'A vehicle must have wheels to calculate maintenance'),
    (polaris, 'A vehicle must have wheels to calculate maintenance'),
])
def test_tire_pressure_model_s(vehicle, expected):
    actual = tire_pressure_maintenance_price(vehicle=vehicle)
    expected = expected
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

vehicles1 = [
    Vehicle('Ford', 'Fiesta', 'Compact', 4, 120, 60),
    Vehicle('Toyota', 'Corolla', 'Sedan', 4, 140, 70),
    Vehicle('Porche', 'Panamera', 'car', 4, 348, 315),
    Vehicle('Honda', 'Civic', 'Hatchback', 4, 130, 1000),
]


def test_get_slowest_median_fastest():
    actual = get_slowest_median_fastest(vehicles=vehicles)
    expected = [Vehicle(brand='Ford', model='Fiesta', type='Compact', wheels=4, power=120, speed=60),
                Vehicle(brand='Toyota', model='Corolla', type='Sedan', wheels=4, power=140, speed=70),
                Vehicle(brand='Honda', model='Civic', type='Hatchback', wheels=4, power=130, speed=1000)]

    assert actual == expected


def test_get_slowest_median_fastest1():
    actual = get_slowest_median_fastest(vehicles=vehicles1)
    expected = [Vehicle(brand='Ford', model='Fiesta', type='Compact', wheels=4, power=120, speed=60),
                Vehicle(brand='Toyota', model='Corolla', type='Sedan', wheels=4, power=140, speed=70),
                Vehicle(brand='Porche', model='Panamera', type='car', wheels=4, power=348, speed=315),
                Vehicle(brand='Honda', model='Civic', type='Hatchback', wheels=4, power=130, speed=1000)]

    assert actual == expected
