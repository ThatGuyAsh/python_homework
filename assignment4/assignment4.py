import pandas as pd

# Task 1: Created a DataFrame from a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

task1_data_frame = pd.DataFrame(data)

print(task1_data_frame)


# Add a new Salary column
task1_with_salary = task1_data_frame.copy()

task1_with_salary["Salary"] = [70000, 80000, 90000]

print(task1_with_salary)


# Increment the Age column by 1
task1_older = task1_with_salary.copy()

task1_older["Age"] = task1_older["Age"] + 1

print(task1_older)


# Saved the DataFrame as a CSV file
task1_older.to_csv("employees.csv", index=False)



# Task 2: Read the CSV file into a DataFrame
task2_employees = pd.read_csv("employees.csv")

print(task2_employees)


# Read the JSON file into a DataFrame
json_employees = pd.read_json("additional_employees.json")

print(json_employees)


# Combine the CSV and JSON DataFrames
more_employees = pd.concat(
    [task2_employees, json_employees],
    ignore_index=True
)

print(more_employees)


# Task 3: Data Inspection

# Get the first three rows
first_three = more_employees.head(3)
print(first_three)


# Get the last two rows
last_two = more_employees.tail(2)
print(last_two)


# Get the shape of the DataFrame
employee_shape = more_employees.shape
print(employee_shape)


# Get information about the DataFrame
more_employees.info()


# Task 4: Data Cleaning

# Read dirty_data.csv
dirty_data = pd.read_csv("dirty_data.csv")
print(dirty_data)

# Make a copy
clean_data = dirty_data.copy()

# Remove duplicate rows
clean_data.drop_duplicates(inplace=True)
print(clean_data)

# Convert Age to numeric
clean_data["Age"] = pd.to_numeric(
    clean_data["Age"],
    errors="coerce"
)
print(clean_data)

# Replace salary placeholders with NaN
clean_data["Salary"] = clean_data["Salary"].replace(
    ["unknown", "n/a"],
    pd.NA
)

# Convert Salary to numeric
clean_data["Salary"] = pd.to_numeric(
    clean_data["Salary"],
    errors="coerce"
)
print(clean_data)

# Fill missing Age with the mean
clean_data["Age"] = clean_data["Age"].fillna(
    clean_data["Age"].mean()
)

# Fill missing Salary with the median
clean_data["Salary"] = clean_data["Salary"].fillna(
    clean_data["Salary"].median()
)
print(clean_data)

# Convert Hire Date to datetime
clean_data["Hire Date"] = pd.to_datetime(
    clean_data["Hire Date"],
    format="mixed",
    errors="raise"
)
print(clean_data)

# Strip whitespace from Name
clean_data["Name"] = clean_data["Name"].str.strip()

# Strip whitespace and uppercase Department
clean_data["Department"] = (
    clean_data["Department"]
    .str.strip()
    .str.upper()
)
print(clean_data)