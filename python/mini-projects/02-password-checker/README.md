# Password Strength Checker

A simple command-line tool that checks how strong a password is and gives suggestions to improve it.

## Features
- Checks minimum length (8+ characters)
- Checks for uppercase, lowercase, digits, and special characters
- Rejects common/leaked passwords (e.g. `123456`, `password`)
- Scores the password from 0–5 and labels it: Weak / Medium / Strong / Very Strong

## Usage
```bash
python password_checker.py
```
Enter a password when prompted, or type `exit` to quit.

## Example
```
Enter your password: pass123
Score: 2/5 | Strength: Medium
Suggestions:
 - Add at least one uppercase letter.
 - Add at least one special character, such as !@#$.
```