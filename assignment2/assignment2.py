# Task 2
import csv
import os
import custom_module
from datetime import datetime

employees = None
employee_id_column = None
minutes_list = None


def read_employees():
    global employees

    employees = {
        "fields": [],
        "rows": []
    }

    with open("employees.csv", "r") as file:
        reader = csv.reader(file)

        employees["fields"] = next(reader)

        for row in reader:
            employees["rows"].append(row)

    return employees


# Task 3 
import csv

employees = None
employee_id_column = None


def read_employees():
    global employees
    global employee_id_column

    employees = {
        "fields": [],
        "rows": []
    }

    with open("employees.csv", "r") as file:
        reader = csv.reader(file)

        employees["fields"] = next(reader)

        for row in reader:
            employees["rows"].append(row)

    employee_id_column = column_index("employee_id")

    return employees


def column_index(column_name):
    return employees["fields"].index(column_name)


read_employees()


# Task 4
def column_index(column_name):
    return employees["fields"].index(column_name)


def first_name(row_number):
    first_name_column = column_index("first_name")
    return employees["rows"][row_number][first_name_column]


# Task 5
def first_name(row_number):
    first_name_column = column_index("first_name")
    return employees["rows"][row_number][first_name_column]


def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))

    return matches


# Task 6
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))

    return matches


def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches


# Task 7
def sort_by_last_name():
    last_name_column = column_index("last_name")

    employees["rows"].sort(key=lambda row: row[last_name_column])

    return employees["rows"]


# Task 8
def employee_dict(row):
    employee = {}

    for field, value in zip(employees["fields"], row):
        if field != "employee_id":
            employee[field] = value

    return employee


# Task 9
def all_employees_dict():
    all_employees = {}

    for row in employees["rows"]:
        employee_id = row[employee_id_column]

        all_employees[employee_id] = employee_dict(row)

    return all_employees


# Task 10
def get_this_value():
    return os.getenv("THISVALUE")


# Task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)


# Task 12
minutes1 = None
minutes2 = None


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
    minutes1 = read_csv_file("minutes1.csv")
    minutes2 = read_csv_file("minutes2.csv")

    return minutes1, minutes2


minutes1, minutes2 = read_minutes()


# Task 13
minutes_set = None


def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])

    return set1.union(set2)


minutes1, minutes2 = read_minutes()
minutes_set = create_minutes_set()


# Task 14
def create_minutes_list():
    minutes = list(minutes_set)

    minutes = list(map(
        lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),
        minutes
    ))

    return minutes


minutes1, minutes2 = read_minutes()
minutes_set = create_minutes_set()
minutes_list = create_minutes_list()


print(minutes_list)


# Task 15
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])

    converted_list = list(map(
        lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")),
        minutes_list
    ))

    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(minutes1["fields"])

        for row in converted_list:
            writer.writerow(row)

    return converted_list


minutes1, minutes2 = read_minutes()
minutes_set = create_minutes_set()
minutes_list = create_minutes_list()
write_sorted_list()