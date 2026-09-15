# Day 1 — TryHackMe: Offensive Security Intro

## Learned

### Offensive vs Defensive Security

* **Offensive Security:** Simulating attacker behavior to find vulnerabilities before real attackers can exploit them.
* **Defensive Security:** Protecting systems, networks, and applications from attacks.
* This course focuses on the **Offensive Security** path, including **Penetration Testing** and **Red Teaming**.

### Directory Brute-Forcing with Gobuster

* Some websites have hidden directories or pages that are not linked from the main page but can still be accessed.
* **Gobuster** is a command-line tool that can find these directories by testing names from a **wordlist**.
* This is called **directory brute-forcing**.

### Basic Command

```bash
gobuster dir -u http://target.com -w wordlist.txt
```

* `dir` → search for directories
* `-u` → target URL
* `-w` → wordlist

> **Note:** Only perform directory enumeration on systems you own or have permission to test.

---

# Day 2 — Python Practice

## Learned

* Started doing Python exercises from easy to harder problems.
* Practiced basic logic and user input.
* Built a **Rock, Paper, Scissors** game.
* Built a **BMI Calculator**.
* Built a **Bingo Game**.
* Built a **Password Generator**.
* Built a **File Organizer**.
* Built a **Weather Client**.
* Practiced using Python modules and external libraries.
* Started learning OOP, including classes, inheritance, and abstract classes.

## Problems

* I was not familiar with the `pathlib` library.
* I had difficulty understanding how **Abstract Base Classes (ABC)** work in the Password Generator.

### Key Takeaway

I learned more by building small projects instead of only doing simple exercises. I also started getting more familiar with modules and OOP.

---

# Day 3 — Python Practice 2

## Learned

* Built a **Palindrome** checker.
* Built a **Matrix Row and Column** exercise.

## Problems

* I got stuck on the loops for the matrix exercise.
* I had some difficulty understanding how rows and columns work in a matrix.

---

# Day 4 — Python Practice 3

## Learned

* Learned how to use **Tkinter**.
* Built a **longest_word** exercise.
* Completed **Chapter 1** and started **Chapter 2** of the Python GUI exercises.
* Built an **Alarm_clock**.

---

# Day 5 — Python Practice 4

## Learned

* Learned how to use **PyQt6**.
* Built a **BMI Calculator V2**.

---

# Day 6 — Python Practice 5

## Learned

* Learned how to use **PySide6**.
* Built a **Note_app_V2**.

---

# Day 7 — Python Practice 6

## Learned

* Learned how to use **Kivy**.
* Learned how to use **pyenv** to manage different Python versions.
* Learned how to create a Python virtual environment with **venv**.
* Built **13_weather_app_v2**.

## Problems

* The Kivy project needed an older Python version, but my system was using **Python 3.14**.
* I couldn't install Python 3.12 directly with `apt` because it was not available in my Ubuntu repositories.
* I used **pyenv** to install Python **3.12.11** without changing my system Python.
* Created a `.venv` for the project and installed **Kivy 2.3.1** inside it.
* At first, `pyenv` was not available after opening a new terminal, so I had to fix its shell configuration.

### Key Takeaway

Today I learned that I don't need to change my system Python just because one project needs another version. I can use **pyenv** for different Python versions and **venv** to keep each project's packages separate.
