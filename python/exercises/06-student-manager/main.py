# ==========================================
# Student Manager
# A simple menu-driven program to add,
# remove, search, and display students.
# ==========================================

students = []  # each student is a dict: {"name": ..., "grade": ...}

while True:
    print("\n===== Student Manager =====")
    print("1. Add student")
    print("2. Remove student")
    print("3. Search student")
    print("4. Show all students")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    # ------------------------------------------
    # 1. Add a student
    # ------------------------------------------
    if choice == "1":
        name = input("Enter student name: ")

        while True:
            grade = input("Enter student grade (0-20): ")

            if not grade.replace(".", "", 1).isdigit():
                print("Please enter a valid number.\n")
                continue

            grade = float(grade)

            if grade < 0 or grade > 20:
                print("Grade must be between 0 and 20.\n")
                continue

            break

        students.append({"name": name, "grade": grade})
        print(f"'{name}' was added.")

    # ------------------------------------------
    # 2. Remove a student by name
    # ------------------------------------------
    elif choice == "2":
        name = input("Enter the name of the student to remove: ")
        found = False

        for student in students:
            if student["name"].lower() == name.lower():
                students.remove(student)
                found = True
                print(f"'{name}' was removed.")
                break

        if not found:
            print(f"No student named '{name}' found.")

    # ------------------------------------------
    # 3. Search for a student by name
    # ------------------------------------------
    elif choice == "3":
        name = input("Enter the name to search: ")
        found = False

        for student in students:
            if student["name"].lower() == name.lower():
                print(f"Found: {student['name']} - Grade: {student['grade']}")
                found = True
                break

        if not found:
            print(f"No student named '{name}' found.")

    # ------------------------------------------
    # 4. Show all students
    # ------------------------------------------
    elif choice == "4":
        print("\n===== All Students =====")

        if students:
            for i, student in enumerate(students, start=1):
                print(f"{i}. {student['name']} - Grade: {student['grade']}")
        else:
            print("No students added yet.")

    # ------------------------------------------
    # 5. Exit the program
    # ------------------------------------------
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option, please choose 1-5.")