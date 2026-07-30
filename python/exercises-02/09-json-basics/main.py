# ----------------------------------------
# Project: JSON Basics
#
# Goal:
# - Create Python dictionary
# - Save Python data into JSON file
# - Read JSON file
# - Convert JSON data back to Python
# ----------------------------------------


# Import JSON module
# Python has a built-in module for working with JSON files
import json


# ----------------------------------------
# Part 1: Create Python data
# ----------------------------------------

# Create a dictionary
# Dictionary stores data as key-value pairs

student = {
    "name": "Ruby",
    "age": 16,
    "course": "Python",
    "grades": [18, 20, 15]
}


# ----------------------------------------
# Part 2: Write data into JSON file
# ----------------------------------------

# Open a file named student.json
#
# "w" means write mode
# If the file does not exist, Python creates it
# If the file exists, old data will be replaced

with open("student.json", "w") as file:

    # Convert Python dictionary into JSON format
    # and save it inside the file
    #
    # dump() -> Python object to JSON file

    json.dump(student, file, indent=4)



# ----------------------------------------
# Part 3: Read data from JSON file
# ----------------------------------------

# Open JSON file in read mode
#
# "r" means read mode

with open("student.json", "r") as file:

    # Read JSON data
    #
    # load() -> JSON file to Python object

    data = json.load(file)



# ----------------------------------------
# Part 4: Display data
# ----------------------------------------

print("Student Information")
print("-------------------")

print(data)


# Access specific values from dictionary

print("\nName:", data["name"])
print("Age:", data["age"])
print("Course:", data["course"])
print("Grades:", data["grades"])