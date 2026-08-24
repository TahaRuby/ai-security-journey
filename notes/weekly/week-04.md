# Week 04 - Linux Practical (OverTheWire Bandit)

## Goals

- Learn basic Linux/Bash commands
- Get comfortable navigating a remote server over SSH
- Learn file inspection commands (ls, cat, file, du)
- Learn how to search effectively with find and grep
- Progress through Bandit levels

---

# Day 1 - SSH & Basic Linux Commands (Bandit 0-6)

## Learned

- Connecting to a remote server with ssh (ssh user@host -p port)
- Logging out of a session with exit
- Basic navigation: ls, ls -a, cd, cd .., cd
- Reading file content with cat
- Identifying file type with file
- Checking disk usage with du
- Handling tricky filenames (starting with "-" or containing spaces)
- Using find to search by name, size, owner, and group
- Redirecting error output with 2>/dev/null
- Using man to look up command options instead of memorizing everything

## Practice

- Bandit Level 0 → 1: basic SSH login
- Bandit Level 1 → 2: reading a file named "-"
- Bandit Level 2 → 3: reading a file with spaces in its name
- Bandit Level 3 → 4: finding a hidden file with find
- Bandit Level 4 → 5: finding the right file among files starting with "-" using file
- Bandit Level 5 → 6: finding a file by exact size (1033 bytes) under a directory
- Bandit Level 6 → 7: finding a file across the whole filesystem by owner, group, and size

## Problems

- Confused "-" as a filename with "-" as a command flag
- Didn't know find could filter by owner/group/size, not just name
- Wasn't sure how to search man pages efficiently instead of reading the whole page

## Notes

Hidden files in Linux start with "." and don't show up with a plain ls — need ls -a or find.

When a filename starts with "-" or has a space, the shell misreads it as an option or as multiple arguments; prefixing with ./ or quoting the name fixes this.

find is the most powerful search tool covered so far — it can filter by name, type, size, owner, and group at the same time, which makes it possible to locate a file without knowing its name or exact location.

Instead of memorizing every command's options, using man <command> and searching inside it with / is a more sustainable way to learn.


---

# Day 2 - 

## Learned

- 

## Practice

- 

## Problems 
- 

## Notes

---

# Day 3 - 

## Learned

- 

## Practice

- 

## Problems

- 

## Notes

---

# Day 4 - 

## Learned

- 

## Practice

- 

## Problems

- 

## Notes

---

# Day 5 - 

## Learned

- 

## Practice

- 

## Problems

- 

## Notes