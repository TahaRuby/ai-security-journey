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

```
gzip → mv+gunzip, bzip2 → mv+bunzip2, tar → mv+tar -xvf
```

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

---

# Day 4 - SSH Keys, Network Services & Bash Scripting (Bandit 13 → 17)

## Learned

- Copying files between the local machine and a remote server with scp

- Understanding that SSH private keys can be used for authentication instead of a password

- Using chmod to restrict permissions on a private SSH key before using it

- Connecting to an SSH server with a specific private key using ssh -i

- Connecting to a local TCP service with nc (netcat)

- Using openssl s_client to establish an SSL/TLS connection to a service

- Understanding that some Bandit levels require interacting with network services listening on specific ports

- Using a Bash for loop to test multiple ports automatically instead of checking them one by one

- Using a Bash variable such as $port inside a loop

- Using echo to display the current port being processed, for example echo "done for $port"

- Using scripts to automate repetitive terminal tasks and reduce manual work

## Practice

- Bandit Level 13 → 14: copied the provided SSH private key with scp, changed its permissions with chmod 600, and used ssh -i to authenticate as the next Bandit user

- Bandit Level 14 → 15: connected to a local service with nc localhost 30000 and provided the current Bandit password

- Bandit Level 15 → 16: connected to a service with openssl s_client -connect localhost:30001 and provided the current Bandit password over an SSL/TLS connection

- Bandit Level 16 → 17: tested the required port range instead of checking every port manually, using a Bash for loop and a small script to automate the process

- Used echo "done for $port" to track progress while the loop was running

## Problems

- Needed to understand why a private SSH key requires restrictive permissions before SSH will use it

- Had to distinguish between a normal TCP connection with nc and an SSL/TLS connection with openssl s_client

- Checking a range of ports manually would be repetitive and inefficient, which led to writing a Bash loop

- Needed to understand how variables such as $port change on every iteration of a for loop

- Had to pay attention to the exact port and protocol being tested instead of treating every service as a normal SSH/TCP connection

## Notes

scp is useful when a file needs to be transferred between the local machine and a remote server. In the Bandit exercise, it was used to copy an SSH private key from the remote account to the local machine.

Private SSH keys should have restrictive permissions. chmod 600 gives the owner read/write access while removing permissions for group and other users.

ssh -i <key> tells SSH to use a specific private key for authentication instead of relying on the default key lookup or password authentication.

nc (netcat) is a simple tool for opening TCP connections to a host and port. It is useful for interacting with plain TCP services and checking whether a service is reachable.

openssl s_client is useful when the target service speaks SSL/TLS. It establishes an encrypted connection and can also be used to inspect the TLS handshake.

A Bash for loop is useful when the same command needs to be repeated over a range of values. Using a variable such as $port makes the command dynamic for each iteration.

Automating repetitive checks with a small shell script is more reliable and less error-prone than manually typing the same command many times.
