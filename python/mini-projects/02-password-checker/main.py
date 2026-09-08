import re


# A small list of commonly used passwords that should never be accepted.
# In a real-world application, this list would be much larger and
# would usually come from a leaked-password database.
COMMON_PASSWORDS = [
    "123456",
    "password",
    "123456789",
    "12345678",
    "12345",
    "qwerty",
    "abc123",
    "111111",
    "1234567",
    "iloveyou",
]


def check_length(password):
    """Check whether the password contains at least 8 characters."""
    return len(password) >= 8


def check_uppercase(password):
    """Check whether the password contains at least one uppercase letter."""
    return bool(re.search(r"[A-Z]", password))


def check_lowercase(password):
    """Check whether the password contains at least one lowercase letter."""
    return bool(re.search(r"[a-z]", password))


def check_digit(password):
    """Check whether the password contains at least one number."""
    return bool(re.search(r"[0-9]", password))


def check_special_char(password):
    """Check whether the password contains at least one special character."""
    return bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))


def is_common_password(password):
    """
    Check whether the password is present in the common password list.

    lower() makes the comparison case-insensitive, so values such as
    'Password' and 'PASSWORD' are treated as the same password.
    """
    return password.lower() in COMMON_PASSWORDS


def check_password_strength(password):
    """
    Calculate the password strength score.

    The password can receive a maximum score of 5:
        +1  Minimum length
        +1  Uppercase letter
        +1  Lowercase letter
        +1  Number
        +1  Special character

    Returns:
        tuple: (score, feedback)
    """

    # Common passwords should be rejected immediately.
    if is_common_password(password):
        return 0, [
            "This password is extremely common or compromised. "
            "Do not use it."
        ]

    score = 0
    feedback = []

    # Check password length.
    if check_length(password):
        score += 1
    else:
        feedback.append(
            "Password must contain at least 8 characters."
        )

    # Check for uppercase letters.
    if check_uppercase(password):
        score += 1
    else:
        feedback.append(
            "Add at least one uppercase letter."
        )

    # Check for lowercase letters.
    if check_lowercase(password):
        score += 1
    else:
        feedback.append(
            "Add at least one lowercase letter."
        )

    # Check for numbers.
    if check_digit(password):
        score += 1
    else:
        feedback.append(
            "Add at least one number."
        )

    # Check for special characters.
    if check_special_char(password):
        score += 1
    else:
        feedback.append(
            "Add at least one special character, such as !@#$."
        )

    return score, feedback


def score_to_label(score):
    """Convert a numerical score into a human-readable strength label."""

    if score <= 1:
        return "Weak"
    elif score <= 3:
        return "Medium"
    elif score == 4:
        return "Strong"
    else:
        return "Very Strong"


def main():
    """Run the password strength checker CLI."""

    print("=== Password Strength Checker ===")
    print("Type 'exit' to quit.\n")

    while True:
        password = input("Enter your password: ")

        # Allow the user to safely exit the program.
        if password.lower() == "exit":
            print("Goodbye!")
            break

        score, feedback = check_password_strength(password)
        label = score_to_label(score)

        print(f"\nScore: {score}/5 | Strength: {label}")

        # Display suggestions if the password fails any checks.
        if feedback:
            print("Suggestions:")

            for item in feedback:
                print(f" - {item}")

        print("-" * 40)


# Run the program only when this file is executed directly.
if __name__ == "__main__":
    main()
