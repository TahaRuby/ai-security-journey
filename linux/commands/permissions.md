# Permission Commands

## `ls -l`

Displays files with detailed permission and ownership information.

```bash
ls -l
```

**Example:**

```bash
ls -l
```

---

## `chmod`

Changes the permissions of a file or directory.

```bash
chmod <permissions> <file>
```

**Example:**

```bash
chmod 600 ~/Downloads/sshkey.private
```

---

## `chmod 600`

Sets read and write permissions for the owner and removes permissions for the group and others.

```bash
chmod 600 <file>
```

**Example:**

```bash
chmod 600 ~/Downloads/sshkey.private
```

### Permission Breakdown

```text
600
│││
││└── Others: no permissions
│└─── Group: no permissions
└──── Owner: read + write
```

This permission mode is commonly used for private SSH keys.
