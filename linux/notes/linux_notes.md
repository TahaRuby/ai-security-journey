# Linux Notes

> Practical Linux notes based on my hands-on practice, especially with OverTheWire Bandit.

---

## 1. SSH Connection and Session Management

### `ssh`

Connects to a remote machine using the SSH protocol.

**Syntax:**

```bash
ssh user@host -p port
```

**Example:**

```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

* `user` → Remote username
* `host` → Remote server
* `-p` → Specify the SSH port
* Default SSH port: `22`

### `exit`

Closes the current shell or SSH session.

```bash
exit
```

This is useful when working with multiple nested SSH sessions.

---

## 2. Linux Files and Directories

### Hidden Files

Linux hidden files usually start with a dot (`.`).

A normal `ls` command does not show hidden files.

Use:

```bash
ls -a
```

This displays both normal and hidden files.

---

### Absolute vs Relative Paths

A **relative path** starts from the current directory.

```bash
cd inhere/
```

An **absolute path** starts from the root directory or another complete path.

```bash
cat /var/lib/dpkg/info/bandit7.password
```

Understanding paths is important when navigating the Linux filesystem.

---

## 3. Special Filenames

Some filenames can be interpreted differently by shell commands.

### Filenames Starting With `-`

A filename beginning with `-` can be interpreted as a command option.

For example:

```bash
cat -filename
```

may be interpreted as an option instead of a filename.

A simple solution is to specify the relative path:

```bash
cat ./-filename
```

Another option is to use `--`:

```bash
cat -- -filename
```

---

### Filenames Containing Spaces

A filename containing spaces should be treated as a single argument.

Using quotes:

```bash
cat "spaces in this filename"
```

Or escaping the spaces:

```bash
cat spaces\ in\ this\ filename
```

---

## 4. File Types and Disk Usage

### `file`

The `file` command identifies the type of a file.

```bash
file filename
```

Example:

```bash
file inhere/
```

Possible output:

```text
inhere/: directory
```

It can also identify text files, binary files, archives, and other formats.

---

### `du`

`du` shows disk usage for files and directories.

```bash
du directory/
```

Example:

```bash
du inhere/
```

For a more human-readable summary:

```bash
du -sh directory/
```

---

## 5. Finding Files with `find`

The `find` command searches for files and directories based on different conditions.

**General structure:**

```bash
find <path> <conditions>
```

### Search by Name

```bash
find . -name "filename"
```

Example:

```bash
find . -name "data.txt"
```

### Search by Size

The `c` suffix means bytes.

```bash
find inhere -size 1033c
```

This searches for a file that is exactly `1033` bytes.

### Search by User, Group, and Size

Multiple conditions can be combined:

```bash
find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
```

This searches the entire filesystem for a file that:

* Is owned by `bandit7`
* Belongs to group `bandit6`
* Is exactly `33` bytes
* Hides permission errors using `2>/dev/null`

---

## 6. Error Redirection

### `2>/dev/null`

This is shell redirection, not a `find` option.

```bash
command 2>/dev/null
```

The number `2` represents **stderr**, which is the standard error stream.

`/dev/null` discards the redirected output.

For example:

```bash
find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
```

This prevents messages such as:

```text
Permission denied
```

from cluttering the terminal output.

---

## 7. Manual Pages and Help

### `man`

The `man` command opens the manual page for a command.

```bash
man find
```

Inside a manual page:

* `/keyword` → Search for a keyword
* `n` → Go to the next match
* `q` → Quit

Example:

```text
man find
/user
```

This is useful when you need to understand command options instead of memorizing them.

---

## 8. Searching Text

### `grep`

`grep` searches text and displays lines matching a pattern.

```bash
grep "pattern" filename
```

Example:

```bash
grep millionth data.txt
```

This was useful in Bandit when searching for a specific line inside a large text file.

---

## 9. Pipes and Text Processing

### Pipe: `|`

A pipe sends the output of one command to another command as input.

```bash
command1 | command2
```

Example:

```bash
strings data.txt | grep "="
```

This allows simple commands to be combined into a processing pipeline.

---

### `sort`

Sorts lines of text.

```bash
sort filename
```

Example:

```bash
sort data.txt
```

It is especially useful before using `uniq`.

---

### `uniq`

`uniq` removes or identifies repeated adjacent lines.

Example:

```bash
sort data.txt | uniq -u
```

The `-u` option displays only lines that occur exactly once.

> **Important:** `uniq` only compares adjacent lines, so `sort` is commonly used first when you want to detect duplicates across the entire file.

---

### `strings`

Extracts readable strings from binary files.

```bash
strings filename
```

Example:

```bash
strings data.txt | grep "="
```

This can be useful when a binary file contains readable text.

---

## 10. Encoding and Text Transformation

### Base64

Base64 is an encoding format, **not encryption**.

To decode Base64 data:

```bash
base64 -d data.txt
```

The decoded output is the original data represented by the Base64 encoding.

---

### `tr`

The `tr` command translates or replaces characters.

```bash
tr 'set1' 'set2'
```

A useful example is decoding ROT13:

```bash
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

ROT13 replaces each letter with the letter 13 positions away in the alphabet.

---

## 11. Temporary Directories and File Operations

### `mktemp -d`

Creates a temporary directory with a unique name.

```bash
mktemp -d
```

Example:

```text
/tmp/tmp.PoEMEPqzkZ
```

Temporary directories are useful when you need a clean workspace for temporary files.

---

### `cp`

Copies files or directories.

```bash
cp <source> <destination>
```

Example:

```bash
cp ~/data.txt .
```

The original file remains unchanged.

---

### `mv`

Moves or renames files.

```bash
mv <old_name> <new_name>
```

Example:

```bash
mv data.bin data.gz
```

During Bandit exercises, `mv` was useful for giving compressed files the correct extension before extracting them.

---

## 12. Hexadecimal Data and Compression

### `xxd -r`

Converts a hexadecimal dump back into binary data.

```bash
xxd -r input.txt output.bin
```

Example:

```bash
xxd -r data.txt data.bin
```

The `-r` option means **reverse**.

---

### `gunzip`

Extracts files compressed with gzip.

```bash
gunzip file.gz
```

Example:

```bash
gunzip data.gz
```

---

### `bunzip2`

Extracts files compressed with bzip2.

```bash
bunzip2 file.bz2
```

Example:

```bash
bunzip2 data.bz2
```

---

### `tar`

Extracts files from a tar archive.

```bash
tar -xvf file.tar
```

Options:

* `-x` → Extract
* `-v` → Verbose output
* `-f` → Specify the archive file

Example:

```bash
tar -xvf data.tar
```

---

## 13. Identifying Multi-Layer Compressed Files

Some files may be compressed or archived multiple times.

A useful workflow is:

1. Check the file type with `file`.
2. Determine the required format.
3. Give the file the correct extension if necessary.
4. Extract or decompress it.
5. Run `file` again.
6. Repeat until the final file is readable text.

Example workflow:

```bash
file data
```

Then, depending on the result:

```bash
mv data data.gz
gunzip data.gz
```

or:

```bash
mv data data.bz2
bunzip2 data.bz2
```

or:

```bash
mv data data.tar
tar -xvf data.tar
```

This technique was practiced extensively in Bandit Level 12.

---

## 14. Secure File Transfer and SSH Keys

### `scp`

`scp` securely copies files between a local machine and a remote machine over SSH.

```bash
scp <source> <destination>
```

Example:

```bash
scp -P 2220 bandit13@bandit.labs.overthewire.org:/home/bandit13/sshkey.private ~/Downloads/
```

> **Note:** `scp` uses uppercase `-P` for the SSH port.

---

### `chmod 600`

Changes file permissions.

```bash
chmod 600 private_key
```

Example:

```bash
chmod 600 ~/Downloads/sshkey.private
```

Permission `600` means:

* Owner → read + write
* Group → no access
* Others → no access

Restrictive permissions are commonly used for private SSH keys.

---

### `ssh -i`

Uses a specific private key for SSH authentication.

```bash
ssh -i <private_key> user@host -p port
```

Example:

```bash
ssh -i ~/Downloads/sshkey.private bandit14@bandit.labs.overthewire.org -p 2220
```

### `scp` vs `ssh -i`

| Command  | Purpose                              |
| -------- | ------------------------------------ |
| `scp`    | Transfer files over SSH              |
| `ssh -i` | Connect using a specific private key |

---

## 15. Network Services

### `nc`

`nc` (Netcat) can establish a TCP or UDP connection to a host and port.

```bash
nc <host> <port>
```

Example:

```bash
nc localhost 30000
```

In Bandit, `nc` was used to interact with local network services.

---

### `openssl s_client`

`openssl s_client` can establish a connection to an SSL/TLS service.

```bash
openssl s_client -connect <host>:<port>
```

Example:

```bash
openssl s_client -connect localhost:30001
```

It is useful when the service expects an SSL/TLS connection.

---

### `nc` vs `openssl s_client`

| Tool               | Typical use               |
| ------------------ | ------------------------- |
| `nc`               | Basic TCP/UDP connections |
| `openssl s_client` | SSL/TLS connections       |

The appropriate tool depends on what protocol the target service expects.

---

## 16. Basic Bash Automation

When the same operation needs to be repeated for multiple values, a Bash `for` loop can automate the process.

### `for` Loop

```bash
for variable in values
do
    commands
done
```

Example:

```bash
for port in 31000 31001 31002 31003 31004
do
    echo "testing $port"
done
```

---

### Bash Variables

A variable's value is accessed using `$`.

```bash
$port
```

Example:

```bash
echo "Testing port $port"
```

The value of `port` changes during each iteration of the loop.

---

### `echo`

Displays text or variable values in the terminal.

```bash
echo "Hello"
```

Example:

```bash
echo "done for $port"
```

It is useful for displaying progress while a script is running.

---

## 17. Key Lessons

* Linux filenames can contain spaces and special characters.
* Files beginning with `.` are hidden by default.
* `find` can search for files using properties such as name, size, owner, group, and type.
* `man` and `--help` are useful alternatives to memorizing every command option.
* Pipes allow multiple commands to work together.
* `2>/dev/null` redirects error output away from the terminal.
* Base64 is **encoding, not encryption**.
* `file` is useful for identifying unknown file formats.
* Compressed files may need to be identified and processed multiple times.
* `scp` transfers files over SSH.
* `ssh -i` uses a specific private key for authentication.
* Private SSH keys should have restrictive file permissions.
* `nc` can be used for basic network connections.
* `openssl s_client` is useful for SSL/TLS connections.
* Bash loops can automate repetitive tasks and reduce manual work.
* `$variable` is used to access the value of a Bash variable.

---

## 18. Learning Through Bandit

Most of these notes were learned through practical exercises in **OverTheWire Bandit**.

The goal was not only to memorize commands, but to understand:

* How Linux handles files and directories
* How paths work
* How command-line tools can be combined
* How file permissions affect access
* How SSH authentication works
* How files can be encoded, compressed, and archived
* How network services can be accessed from the command line
* How basic Bash automation can reduce repetitive work
