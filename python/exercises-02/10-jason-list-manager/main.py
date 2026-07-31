# ----------------------------------------
# Project: JSON List Manager
#
# Goal:
# - Store multiple items in JSON
# - Read existing data
# - Add new items
# - Save updated data
# ----------------------------------------


import json


# File name
filename = "tasks.json"


# ----------------------------------------
# Part 1: Create initial tasks
# ----------------------------------------

tasks = [
    {
        "title": "Learn Python",
        "done": False
    },
    {
        "title": "Practice Git",
        "done": True
    }
]


# ----------------------------------------
# Part 2: Save tasks into JSON file
# ----------------------------------------

with open(filename, "w") as file:
    json.dump(tasks, file, indent=4)



# ----------------------------------------
# Part 3: Read tasks from JSON file
# ----------------------------------------

with open(filename, "r") as file:
    tasks = json.load(file)



# ----------------------------------------
# Part 4: Add new task
# ----------------------------------------

new_task = {
    "title": "Learn JSON",
    "done": False
}


tasks.append(new_task)



# ----------------------------------------
# Part 5: Save updated tasks
# ----------------------------------------

with open(filename, "w") as file:
    json.dump(tasks, file, indent=4)



# ----------------------------------------
# Part 6: Display tasks
# ----------------------------------------

for task in tasks:
    print(task["title"], "-", task["done"])