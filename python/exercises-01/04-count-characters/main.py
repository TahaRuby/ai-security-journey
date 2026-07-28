# ==========================================
# Username Analyzer
# Analyze a username by counting letters,
# digits, symbols, and total characters.
# ==========================================

while True:
    username = input("Enter your username: ")

    # Validate user input
    if username == "":
        print("Username cannot be empty.\n")
    elif len(username) < 4:
        print("Username is too short.\n")
    elif len(username) > 15:
        print("Username is too long.\n")
    else:
        break

# Initialize counters
character_count = 0
letter_count = 0
digit_count = 0
symbol_count = 0

# Analyze every character in the username
for character in username:
    character_count += 1

    if character.isalpha():
        letter_count += 1

    elif character.isdigit():
        digit_count += 1

    else:
        symbol_count += 1

# Display the results
print("\n========== Username Analysis ==========")
print(f"Username          : {username}")
print(f"Total Characters  : {character_count}")
print(f"Letters           : {letter_count}")
print(f"Digits            : {digit_count}")
print(f"Symbols           : {symbol_count}")