from collections import namedtuple

# Define the namedtuple for each department/function
ActivatedDepartment = namedtuple("ActivatedDepartment", "function head total_employees activated_employees")

# List of departments with data
departments = [
    # finance
    # ActivatedDepartment('Accounting & Reporting', 'Ramos Rui Pedro Varela', 103, 17),
    # ActivatedDepartment('Treasury, Pension & Insurance', 'Lee Sheridan Edwards', 57, 24),
    # ActivatedDepartment('Internal Audit', 'Henrik Gotterbarm', 31, 29),
    # ActivatedDepartment('Tax', 'James Parent', 20, 18),
    # ActivatedDepartment('Business Services Finance', 'Elvira Orlova', 1, 1),
    # ActivatedDepartment('Corporate Talent', 'Barbara Arimont', 35, 24),
    # ActivatedDepartment('Diversity, Equity & Inclusion', 'Fridah Muchina', 1, 1),
    # ActivatedDepartment('HR SBU, F&C, Center', 'Philippe Vossen', 47, 7),
    # zone europe
    ActivatedDepartment('Head of Zone EUR', 'Le Cunff Guillaume', 2098, 301),
    ActivatedDepartment('Market Head Switzerland', 'Simioni Eugenio', 1530, 101),
    ActivatedDepartment('Zone Business Head Purina EUR', 'Hamilton Jeffrey', 150, 67),
    ActivatedDepartment('Head of Food Zone EUR', 'Fagnoni Paolo', 61, 29),
    ActivatedDepartment('Head of Confectionery Zone EUR', 'Agostini Stefano', 95, 27),
    ActivatedDepartment('Head of Coffee, Z-EUR', 'Mikhailova Yana', 52, 23),
    ActivatedDepartment('Head of Nutrition Z-EUR', 'Jalal Sophia', 88, 11),
    ActivatedDepartment('Zone EUR Head of HR', 'Reber Jacques', 12, 8),
    ActivatedDepartment('Head of NP Zone EUR', 'de Clippele Vincent', 61, 7),
    ActivatedDepartment('Head of Operations Zone Europe', 'Albanese Tiziana', 13, 7),
    ActivatedDepartment('Zone EUR Head of F&C', 'Helfer Olivier', 15, 5),
    ActivatedDepartment('Head of Sales & Customer for Zone EUR', 'Stefano Borghi', 3, 3),
    ActivatedDepartment('Head of Sustainability Zone EUR', 'Seidenschnur Katja', 3, 3),
    ActivatedDepartment('Regional Manager ZEUR', 'Frei Roger', 2, 2),
    ActivatedDepartment('Zone EUR Head of Digital', 'Ovaert Mathieu', 3, 2),
    ActivatedDepartment('Zone Europe Head of Marketing and Consum', 'Brinbaum Melanie', 5, 2),
    ActivatedDepartment('Zone EUR Executive Assistant', 'Bruns Alexia', 1, 1),
    ActivatedDepartment('Zone EUR Executive Assistant', 'Cretton Hélène', 1, 1),
    ActivatedDepartment('Zone EUR Head of Strategy', 'Eliseeva Natalia', 2, 1),
    # legal & compliance
    ActivatedDepartment('Accounting & Reporting', 'Stefan Helfenstein', 0, 0),
    # strategy & business development
    ActivatedDepartment('Acquisitions & BizDev', 'Four People', 4, 2),
    ActivatedDepartment('Partnership & Integration', 'Maxence Eric de Royer', 3, 1),
ActivatedDepartment('Portfolio Strategy', 'Blaise Revillard', 4, 0),
    # Add other departments as necessary...
]


# Function to calculate the percentage
def calculate_percentage(total_employees, activated_employees):
    if total_employees == 0:
        return 0  # Avoid division by zero
    return (activated_employees / total_employees) * 100


# Loop through the departments and calculate the percentage for each
for dept in departments:
    percentage = calculate_percentage(dept.total_employees, dept.activated_employees)
    print(f"Department: {dept.function} ({dept.head}) - {percentage:.2f}% of employees activated on Copilot")
