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

# Day 2 - Text Search, Encoding & Piping (Bandit 7-11)

## Learned

- Searching for a keyword inside a file with grep "word" file
- Piping: using | to send the output of one command as input to the next
- Sorting lines with sort, and finding lines that appear only once with sort file | uniq -u
- Extracting readable text out of a binary file with strings
- Combining strings with grep to filter for specific patterns (e.g. lines starting with "=")
- Decoding Base64-encoded data with base64 -d file
- Understanding what Base64 is (an encoding, not encryption — reversible by anyone)
- Understanding ROT13 (each letter shifted 13 places in the alphabet, self-reversing)
- Using tr to translate/rotate characters, e.g. tr 'A-Za-z' 'N-ZA-Mn-za-m' for ROT13

## Practice

- Bandit Level 7 → 8: grep millionth data.txt — find the line next to a specific word
- Bandit Level 8 → 9: sort data.txt | uniq -u — find the one line that occurs only once
- Bandit Level 9 → 10: strings data.txt | grep "=" — find a human-readable password preceded by "=" characters in a binary file
- Bandit Level 10 → 11: base64 -d data.txt — decode a Base64-encoded file
- Bandit Level 11 → 12: cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m' — reverse a ROT13-rotated file

## Problems

- Didn't know sort was needed before uniq (uniq only catches consecutive duplicate lines)
- Wasn't sure how tr's two character-range arguments map to each other for ROT13
- Needed clarification on why piping (|) is required instead of running commands separately

## Notes

Piping (command1 | command2) lets the output of one command become the input of the next, which is the basis for chaining small tools together instead of writing one big command.

uniq only removes/detects duplicates that are next to each other, so the input usually needs to be sorted first.

strings is essential for inspecting binary files without flooding the terminal with unreadable bytes.

Base64 and ROT13 are both encodings, not real encryption — they're reversible by anyone who knows the method, which is why base64 -d and tr can undo them directly.

---

# Day 3 - Repeated Compression & Working in /tmp (Bandit 12 → 13, completed)

## Learned

- Why /tmp is used for scratch work instead of the home directory (home directories are not writable for this)
- Creating a random, hard-to-guess temporary directory with mktemp -d
- Navigating into it with cd, and confirming location with pwd
- Copying a file into the working directory with cp source destination
- Reversing a hexdump back into its original binary file with xxd -r input output
- Understanding the difference between xxd (binary → hex text) and xxd -r (hex text → binary)
- Identifying a file's real type regardless of its name/extension with file
- Renaming a file to give it the correct extension with mv old new (mv is also used for renaming, not just moving)
- Decompressing gzip archives: rename to .gz, then gunzip file.gz
- Decompressing bzip2 archives: rename to .bz2, then bunzip2 file.bz2
- Extracting tar archives: rename to .tar, then tar -xvf file.tar (-x extract, -v verbose, -f specify file)
- Recognizing that a file is no longer compressed when file reports "ASCII text"
- Working through a chain of nested/repeated compression by repeating: file → rename → decompress/extract → file again, until reaching a plain text file

## Practice

- Bandit Level 12 → 13 (completed) — full chain of steps:
  - mktemp -d to create a working directory under /tmp
  - cp ~/data.txt . to copy the data file into it
  - xxd -r data.txt data.bin to rebuild the original binary file from its hexdump
  - Repeatedly ran file to detect the compression type, then renamed and unpacked with the matching tool:
    gzip → mv+gunzip, bzip2 → mv+bunzip2, tar → mv+tar -xvf
  - The file went through about 8 layers of compression (gzip, bzip2, tar, gzip, tar, bzip2, tar, gzip) before file finally reported "ASCII text"
  - cat on the final file revealed the password

## Problems

- Ran a command from the home directory instead of the /tmp working directory by mistake, causing a "Permission denied" error
- Forgot the -r flag once, running xxd in the wrong direction
- Got confused switching between multiple terminal steps — learned to check pwd before each step to confirm location
- Accidentally ran the same decompress command twice (second time failed because the file no longer existed after the first successful run) — learned to check ls after each step before repeating a command
- Didn't realize at first that the compression type could keep changing at every layer, requiring file to be re-checked after every single unpack step

## Notes

Home directories on this server are read-only for new files, so any level involving file creation/extraction needs a scratch directory under /tmp made with mktemp -d.

xxd converts a binary file into a readable hex dump; xxd -r reverses that, turning a hex dump back into the original binary — the direction matters and is easy to mix up.

When a multi-step task in the terminal gets confusing, running pwd before each command is a simple way to confirm exactly where you are before proceeding.

Compression tools generally expect a matching file extension to work correctly (.gz for gunzip, .bz2 for bunzip2, .tar for tar), even though the actual file type is determined by its content, not its name — so mv is used purely to rename before each unpack step.

A file that's been "repeatedly compressed" has to be unwrapped one layer at a time — there's no way to know in advance how many layers there are or what order they're in; file after every step is what tells you whether to keep going or whether you've reached the final plain file.

xxd converts a binary file into a readable hex dump; xxd -r reverses that, turning a hex dump back into the original binary — the direction matters and is easy to mix up.

When a multi-step task in the terminal gets confusing, running pwd before each command is a simple way to confirm exactly where you are before proceeding.

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