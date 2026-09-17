# Networking Commands

## `ssh`

Connects to a remote machine using the SSH protocol.

```bash
ssh user@host -p port
```

**Example:**

```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

---

## `ssh -i`

Connects to a remote machine using a specified private key for authentication.

```bash
ssh -i <private_key> user@host -p port
```

**Example:**

```bash
ssh -i ~/Downloads/sshkey.private bandit14@bandit.labs.overthewire.org -p 2220
```

---

## `scp`

Transfers files between local and remote systems over SSH.

```bash
scp -P port <source> <destination>
```

**Example:**

```bash
scp -P 2220 bandit13@bandit.labs.overthewire.org:/home/bandit13/sshkey.private ~/Downloads/
```

> **Note:** `scp` uses uppercase `-P` for the port, while `ssh` uses lowercase `-p`.

---

## `nc`

Creates a TCP or UDP connection to a host and port.

```bash
nc <host> <port>
```

**Example:**

```bash
nc localhost 30000
```

---

## `openssl s_client`

Connects to an SSL/TLS service for testing or communication.

```bash
openssl s_client -connect <host>:<port>
```

**Example:**

```bash
openssl s_client -connect localhost:30001
```
