# File and Text Commands

## `mkdir`

Creates a new directory.

```bash
mkdir <directory>
```

**Example:**

```bash
mkdir labs
```

---

## `touch`

Creates an empty file or updates a file's timestamp.

```bash
touch <file>
```

**Example:**

```bash
touch notes.md
```

---

## `cat`

Displays the contents of a text file.

```bash
cat <file>
```

**Example:**

```bash
cat /var/lib/dpkg/info/bandit7.password
```

---

## `file`

Identifies the type of a file.

```bash
file <file>
```

**Example:**

```bash
file inhere/
```

---

## `du`

Displays disk usage for files and directories.

```bash
du <file_or_directory>
```

**Example:**

```bash
du inhere/
```

---

## `cp`

Copies a file or directory.

```bash
cp <source> <destination>
```

**Example:**

```bash
cp ~/data.txt .
```

---

## `mv`

Moves or renames a file or directory.

```bash
mv <source> <destination>
```

**Example:**

```bash
mv data.bin data.gz
```

---

## `rm`

Removes a file.

```bash
rm <file>
```

**Example:**

```bash
rm old_file.txt
```

---

## `rmdir`

Removes an empty directory.

```bash
rmdir <directory>
```

**Example:**

```bash
rmdir empty_dir
```

---

## `find`

Searches for files and directories based on specified conditions.

```bash
find <path> <conditions>
```

**Example:**

```bash
find inhere -size 1033c
```

---

## `grep`

Searches for lines matching a pattern inside a file.

```bash
grep "pattern" <file>
```

**Example:**

```bash
grep millionth data.txt
```

---

## `sort`

Sorts lines of text.

```bash
sort <file>
```

**Example:**

```bash
sort data.txt
```

---

## `uniq`

Filters repeated adjacent lines.

```bash
uniq [options]
```

**Example:**

```bash
sort data.txt | uniq -u
```

---

## `strings`

Extracts readable strings from binary files.

```bash
strings <file>
```

**Example:**

```bash
strings data.txt
```

---

## `base64`

Encodes or decodes data using Base64.

```bash
base64 [options] <file>
```

**Example:**

```bash
base64 -d data.txt
```

---

## `tr`

Translates or replaces characters.

```bash
tr 'set1' 'set2'
```

**Example:**

```bash
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

---

## `mktemp`

Creates a temporary file or directory.

```bash
mktemp -d
```

**Example:**

```bash
mktemp -d
```

---

## `xxd`

Creates or reverses a hexadecimal dump.

```bash
xxd -r <input> <output>
```

**Example:**

```bash
xxd -r data.txt data.bin
```

---

## `gunzip`

Decompresses a gzip-compressed file.

```bash
gunzip <file.gz>
```

**Example:**

```bash
gunzip data.gz
```

---

## `bunzip2`

Decompresses a bzip2-compressed file.

```bash
bunzip2 <file.bz2>
```

**Example:**

```bash
bunzip2 data.bz2
```

---

## `tar`

Extracts files from a tar archive.

```bash
tar -xvf <file.tar>
```

**Example:**

```bash
tar -xvf data.tar
```

---

## `|` — Pipe

Sends the output of one command to another command as input.

```bash
command1 | command2
```

**Example:**

```bash
strings data.txt | grep "="
```

---

## `2>/dev/null`

Redirects standard error to `/dev/null`, hiding error messages.

```bash
command 2>/dev/null
```

**Example:**

```bash
find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
```

---

## Special Filenames

### Filename Starting With `-`

Use `./` when a filename starts with `-` to prevent it from being interpreted as an option.

```bash
cat ./-filename
```

**Example:**

```bash
cat ./-file00
```

### Filename Containing Spaces

Use quotes or escape spaces when a filename contains spaces.

```bash
cat "file name"
```

**Example:**

```bash
cat "spaces in this filename"
```

Alternative:

```bash
cat spaces\ in\ this\ filename
```
