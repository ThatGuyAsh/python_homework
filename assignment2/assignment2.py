import csv
import os
import custom_module
from datetime import datetime

employees = None
employee_id_column = None
minutes1 = None
minutes2 = None
minutes_set = None
minutes_list = None


# Task 2 - Read a CSV File
def read_employees():
    global employees
    global employee_id_column

    employees = {
        "fields": [],
        "rows": []
    }

    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)

            employees["fields"] = next(reader)

            for row in reader:
                employees["rows"].append(row)

    except FileNotFoundError:
        print("employees.csv not found")

    employee_id_column = column_index("employee_id")

    return employees


# Task 3 - Find the Column Index
def column_index(column_name):
    return employees["fields"].index(column_name)


# Task 4 - Find the Employee First Name
def first_name(row_number):
    first_name_column = column_index("first_name")
    return employees["rows"][row_number][first_name_column]


# Task 5 - Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))

    return matches


# Task 6 - Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id,
                          employees["rows"]))
    return matches


# Task 7 -  Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    last_name_column = column_index("last_name")

    employees["rows"].sort(key=lambda row: row[last_name_column])

    return employees["rows"]


# Task 8 - Create a dict for an Employee
def employee_dict(row):
    employee = {}

    for field, value in zip(employees["fields"], row):
        if field != "employee_id":
            employee[field] = value

    return employee


# Task 9 -  A dict of dicts, for All Employees
def all_employees_dict():
    all_employees = {}

    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        all_employees[employee_id] = employee_dict(row)

    return all_employees


# Task 10 - Use the os Module
def get_this_value():
    return os.getenv("THISVALUE")


# Task 11 - Creating Your Own Module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)


# Task 12 - Read minutes1.csv and minutes2.csv
def read_csv_file(filename):
    data = {
        "fields": [],
        "rows": []
    }

    with open(filename, "r") as file:
        reader = csv.reader(file)

        data["fields"] = next(reader)

        for row in reader:
            data["rows"].append(tuple(row))

    return data


def read_minutes():
    minutes1 = read_csv_file("../csv/minutes1.csv")
    minutes2 = read_csv_file("../csv/minutes2.csv")

    return minutes1, minutes2


# Task 13 - Create minutes_set
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])

    return set1.union(set2)


# Task 14 - Convert to datetime
def create_minutes_list():
    minutes = list(minutes_set)

    minutes = list(map(
        lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),
        minutes
    ))

    return minutes


# Task 15 - Write Out Sorted List
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])

    converted_list = list(map(
        lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")),
        minutes_list
    ))

    with open("../csv/minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(minutes1["fields"])

        for row in converted_list:
            writer.writerow(row)

    return converted_list


# Global data 
read_employees()

minutes1, minutes2 = read_minutes()

minutes_set = create_minutes_set()

minutes_list = create_minutes_list()