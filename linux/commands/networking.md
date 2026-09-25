# Networking Commands

## `ssh`

Connects to a remote machine using the SSH protocol.

```
ssh user@host -p port
```

**Example:**

```
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

---

## `ssh -i`

Connects to a remote machine using a specified private key for authentication.

```
ssh -i <private_key> user@host -p port
```

**Example:**

```
ssh -i ~/Downloads/sshkey.private bandit14@bandit.labs.overthewire.org -p 2220
```

---

## `scp`

Transfers files between local and remote systems over SSH.

```
scp -P port <source> <destination>
```

**Example:**

```
scp -P 2220 bandit13@bandit.labs.overthewire.org:/home/bandit13/sshkey.private ~/Downloads/
```

> **Note:** `scp` uses uppercase `-P` for the port, while `ssh` uses lowercase `-p`.

---

## `nc`

Netcat is a networking utility used to create and test network connections.

```
nc <host> <port>
```

**Example:**

```
nc localhost 30000
```

Test a TCP connection:

```
nc -vz example.com 443
```

* `-v` → verbose output
* `-z` → test the connection without sending data

---

## `openssl s_client`

Connects to an SSL/TLS service for testing.

```
openssl s_client -connect <host>:<port>
```

**Example:**

```
openssl s_client -connect localhost:30001
```

---

## `ss`

Shows network sockets, listening ports, and active connections.

```
ss -tuln
```

Show listening ports and the processes using them:

```
sudo ss -tulnp
```

**Example:**

```
sudo ss -tulnp
```

This can show information such as:

```
127.0.0.53:53     systemd-resolve
127.0.0.1:631      cupsd
127.0.0.1:43023    code
```

* `53` → DNS endpoint
* `631` → CUPS printing service
* `43023` → VS Code process
