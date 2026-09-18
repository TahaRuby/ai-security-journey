import subprocess
import sys

packages = [
    "PySide6",
    "PyQt6",
    "kivy"
]

print("Installing required packages...\n")

for package in packages:
    print(f"Installing {package}...")
    subprocess.check_call([
        sys.executable,
        "-m",
        "pip",
        "install",
        package
    ])

print("\nAll packages installed successfully!")