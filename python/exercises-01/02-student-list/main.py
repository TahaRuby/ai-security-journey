# ==========================================
# Student List
# A simple program to store and display
# student names.
# ==========================================

students = [] 

# Collect student names until the user exits 

while True:
    name = input("Enter student name (or type 'exit' to finish): ")

    if name.lower() == "exit":
        break

    students.append(name)

print("\n===== Class List =====")

# ------------------------------------------
# Method 1: Using range() and list indexing
# ------------------------------------------
for i in range(len(students)):
    print(f"{i + 1}. {students[i]}")

# ------------------------------------------
# Method 2: Using enumerate() (Pythonic way)
# Uncomment the code below to use this method.
# ------------------------------------------

# for i, student in enumerate(students, start=1):
#     print(f"{i}. {student}")