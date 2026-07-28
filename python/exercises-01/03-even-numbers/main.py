# ==========================================
# Even Number Filter
# A simple program that separates even and
# odd numbers entered by the user.
# ==========================================

# Ask the user how many numbers they want to enter
count = int(input("Enter how many numbers: "))

# Create lists to store numbers
numbers = []
even_numbers = []
odd_numbers = []

# Collect numbers from the user
for i in range(count):
    number = int(input(f"Enter number #{i + 1}: "))
    numbers.append(number)

    # Check whether the number is even or odd
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# Display even numbers
print("\n===== Even Numbers =====")

if even_numbers:
    for i, number in enumerate(even_numbers, start=1):
        print(f"{i}. {number}")
else:
    print("No even numbers found.")

# Display odd numbers

print("\n===== Odd Numbers =====")

if odd_numbers:
    for i, number in enumerate(odd_numbers, start=1):
        print(f"{i}. {number}")
else:
    print("No odd numbers found.")

# Display statistics
print("\n===== Summary =====")
print(f"Total Numbers : {len(numbers)}")
print(f"Even Numbers  : {len(even_numbers)}")
print(f"Odd Numbers   : {len(odd_numbers)}")