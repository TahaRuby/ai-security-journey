# Networking & HTTP — Week 6

## Part 1 — Networking Foundation

### 1. DNS

#### Questions

* What is DNS?

  * DNS stands for Domain Name System.
  * It translates domain names into IP addresses.

* Why do we need DNS?

  * Humans can easily remember names such as `example.com`, but computers need IP addresses to communicate with servers.
  * DNS helps the system find the IP address associated with a domain name.

* How does a domain become an IP address?

  * The system sends a DNS query to a DNS resolver.
  * The resolver finds the IP address associated with the domain and returns it.
  * A domain can have multiple IP addresses.

#### Test

```bash
nslookup example.com
```

#### Observation

The command showed that my system uses `127.0.0.53` as its local DNS resolver.

```text
Server:   127.0.0.53
Address:  127.0.0.53#53
```

* `127.0.0.53` is the address of the DNS resolver used by my system.
* `#53` means the DNS resolver is using port `53`.
* `Non-authoritative answer` means the response came from the resolver rather than directly from the authoritative DNS server for the domain.
* The DNS query for `example.com` returned IP addresses for the domain.

Example:

```text
Name:    example.com
Address: 172.66.147.243
```

Here, `172.66.147.243` is an IP address associated with `example.com`, not the address of the DNS resolver.

The command also returned IPv6 addresses for `example.com`.

#### My Understanding

DNS works like a name-to-address lookup system. When I use a domain name such as `example.com`, my system asks a DNS resolver for the IP address associated with that domain. The resolver returns one or more IP addresses that can be used to find the destination server.

The DNS resolver address and the IP address of the requested domain are different things:

```text
127.0.0.53:53
      ↓
DNS Resolver
      ↓
example.com
      ↓
172.66.147.243
```

**Key point:** DNS does not connect my browser to the website by itself. It helps my system discover the IP address needed to communicate with the destination.


---

## 2. Ports

### Questions

* What is a port?

  * A port is a logical endpoint used by network services to communicate.

* Why do we need ports?

  * A single computer can run many network services at the same time.
  * Ports allow the operating system to distinguish between different network services.

* What is the difference between an IP address and a port?

  * An IP address identifies a host.
  * A port identifies a network endpoint associated with a service on that host.

For example:

```text
192.168.1.10:22

192.168.1.10 → IP address
22           → Port
Common Ports
Port	Service
22	SSH
53	DNS
80	HTTP
443	HTTPS
Test
ss -tuln
Observation

The command shows network sockets that are listening on my system.

For example, an entry such as:

127.0.0.53:53

means that a service is listening on port 53 on the local address 127.0.0.53.

The LISTEN state means that the service is waiting for incoming TCP connections.

My Understanding

An IP address tells us which host we want to communicate with, while a port tells us which network service or endpoint we want to communicate with on that host.

For example:

192.168.1.10:22
       │      │
       │      └── Port 22
       └───────── IP address

So an IP address and a port work together to identify a network endpoint