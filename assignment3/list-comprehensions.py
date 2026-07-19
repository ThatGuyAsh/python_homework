# Task 3

import csv

# Read employees.csv into a list of lists
employees = []

with open("../csv/employees.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        employees.append(row)


# Create list of employee names using list comprehension
# Skip the header row
names = [
    f"{employee[1]} {employee[2]}"
    for employee in employees[1:]
]

print(names)


# Create a list containing only names with the letter "e"
names_with_e = [
    name
    for name in names
    if "e" in name
]

print(names_with_e)