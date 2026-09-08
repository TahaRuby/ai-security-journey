# Day 1 — TryHackMe: Offensive Security Intro

## Learned

### Offensive vs Defensive Security

* **Offensive Security:** Simulating attacker behavior to identify vulnerabilities before real attackers can exploit them.
* **Defensive Security:** Protecting systems, networks, and applications against attacks.
* This course focuses on the **Offensive Security** path, including **Penetration Testing** and **Red Teaming**.

### Directory Brute-Forcing with Gobuster

* Some websites contain hidden directories or pages that are not linked from the main website but are still accessible on the server.
* **Gobuster** is a command-line tool that can discover these directories by testing names from a **wordlist** against a target website.
* This technique is known as **directory brute-forcing**.

### Basic Command

```bash
gobuster dir -u http://target.com -w wordlist.txt
```

* `dir` → tells Gobuster to search for directories
* `-u` → specifies the target URL
* `-w` → specifies the wordlist to use

> **Note:** Only perform directory enumeration against systems you own or have explicit permission to test.

---

Day 2 — Python Practice

## Learned

- Started creating Python exercises from easy to harder problems.
- Practiced basic programming logic and user input.
- Built a **Rock, Paper, Scissors** game.
- Built a **BMI Calculator**.
- Built a **Bingo Game**.
- Built a **Password Generator**.
- Built a **File Organizer**.
- Built a **Weather Client**.
- Practiced working with Python modules and external libraries.
- Started learning Object-Oriented Programming (OOP) concepts such as classes, inheritance, and abstract classes.

Problems

- I was not familiar with using the "pathlib" library for working with file paths.
- I had difficulty understanding how to use Abstract Base Classes (ABC) in the Password Generator exercise.

Key Takeaway

Today I improved my Python fundamentals by building small practical projects instead of only solving isolated exercises. I also started moving toward more structured Python programming with modules and OOP.
