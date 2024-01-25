# Name, date found, number of employees
car_brands = [
    ('Audi', 1909, 90000),
    ('Mercedes', 1926, 172000),
    ('Peugeot', 1810, 200000),
    ('Morgan', 1910, 250)
]

# 2. Print the name of each brand that is older than 100 years
older_100_years = []
for company in car_brands:
    years_old = 2023 - company[1]
    if years_old >= 100:
        older_100_years.append(company[0])
print(older_100_years)

# 3. Print the name of each brand that has less than 100,000 employees
less_100000_employees = []
for employer in car_brands:
    if employer[2] < 100000:
        less_100000_employees.append(employer[0])
print(less_100000_employees)
