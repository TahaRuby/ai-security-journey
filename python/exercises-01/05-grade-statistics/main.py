# ==========================================
# Grade Statistics
# A simple program that collects student
# grades and calculates class statistics.
# ==========================================

# Ask the user how many grades they want to enter
while True:
    count = input("Enter how many grades: ")

    if not count.isdigit() or int(count) <= 0:
        print("Please enter a positive number.\n")
    else:
        count = int(count)
        break

grades = []

# Collect grades from the user (0 to 20)
for i in range(count):
    while True:
        grade = input(f"Enter grade #{i + 1} (0-20): ")

        if not grade.replace(".", "", 1).isdigit():
            print("Please enter a valid number.\n")
            continue

        grade = float(grade)

        if grade < 0 or grade > 20:
            print("Grade must be between 0 and 20.\n")
            continue

        grades.append(grade)
        break

# ------------------------------------------
# Calculate statistics using built-in functions
# ------------------------------------------
average = sum(grades) / len(grades)
highest = max(grades)
lowest = min(grades)

# ------------------------------------------
# Calculate the same max/min manually (for practice)
# ------------------------------------------
manual_highest = grades[0]
manual_lowest = grades[0]

for grade in grades:
    if grade > manual_highest:
        manual_highest = grade

    if grade < manual_lowest:
        manual_lowest = grade

# Count how many passed (>=10) and failed (<10)
passed = 0
failed = 0

for grade in grades:
    if grade >= 10:
        passed += 1
    else:
        failed += 1

# Display the results
print("\n========== Grade Statistics ==========")
print(f"Grades            : {grades}")
print(f"Average           : {average:.2f}")
print(f"Highest (built-in): {highest}")
print(f"Lowest  (built-in): {lowest}")
print(f"Highest (manual)  : {manual_highest}")
print(f"Lowest  (manual)  : {manual_lowest}")
print(f"Passed            : {passed}")
print(f"Failed            : {failed}")