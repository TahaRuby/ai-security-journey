# ----------------------------------------
# Project: Write & Read File
# Goal:
# - Get notes from the user
# - Save them into a text file
# - Read the file again
# - Display saved notes
# ----------------------------------------


# File name where we store our notes
filename = "notes.txt"


# ----------------------------------------
# Part 1: Get input from user
# ----------------------------------------

# Ask the user how many notes they want to add
number_of_notes = int(input("How many notes do you want to add? "))


# ----------------------------------------
# Part 2: Write data into file
# ----------------------------------------

# "a" means append
# It adds new content at the end of the file.
#
# Difference:
# "w" -> write from the beginning and removes old content
# "a" -> keeps old content and adds new content

with open(filename, "a") as file:

    # Repeat based on the number of notes
    for i in range(number_of_notes):

        # Get note from user
        note = input(f"Write note {i + 1}: ")

        # Write note into file
        # \n means move to the next line
        file.write(note + "\n")


# ----------------------------------------
# Part 3: Read file content
# ----------------------------------------

# Open file in read mode
# "r" means read

with open(filename, "r") as file:

    # Read all content from file
    data = file.read()


# ----------------------------------------
# Part 4: Display result
# ----------------------------------------

print("\nYour notes:")
print("----------------")

print(data)