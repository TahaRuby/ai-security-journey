# TCP, IP and Ports

## 1. IP Address

An IP address identifies a network interface or destination within an IP network.

Common versions:

- IPv4
- IPv6

## 2. Ports

A transport-layer port identifies an application endpoint on a host.

| Port | Common Usage |
|---|---|
| 22 | SSH |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |

These are common assignments, not guarantees about which service is running.

## 3. TCP

TCP is a connection-oriented transport protocol that provides reliable and ordered data delivery.

### Three-Way Handshake

1. SYN: the client initiates a connection.
2. SYN-ACK: the server responds.
3. ACK: the client acknowledges the response.

TCP does not encrypt data by itself.

## 4. Practical Commands

```bash
ip addr
ip route
```

- `ip addr` displays network addresses and interfaces.
- `ip route` displays routing information.

## 5. Nmap Basics

Nmap is a network discovery and service-scanning tool.

Example for an authorized target:

```bash
nmap -sT -p 80,443 <authorized-host>
```

An open port does not automatically indicate a vulnerability.

## 6. Security Relevance

Understanding IP addresses, ports, and services helps identify network exposure during authorized security assessments.

## 7. Key Takeaways

- IP identifies a network destination.
- Ports identify transport endpoints.
- TCP provides reliable, ordered delivery.
- TCP does not provide encryption.
- Network scans must be authorized.