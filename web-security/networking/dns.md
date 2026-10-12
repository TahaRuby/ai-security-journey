# DNS — Domain Name System

## 1. Definition

DNS is a distributed naming system that helps translate domain names into records used to locate network services.

For example, DNS can resolve `example.com` to an IP address.

## 2. Common DNS Records

| Record | Purpose |
|---|---|
| A | IPv4 address |
| AAAA | IPv6 address |
| CNAME | Alias for another domain name |
| MX | Mail server information |
| NS | Authoritative name server information |
| TXT | Text records used for different purposes, including domain verification |

## 3. Practical Commands

```bash
getent hosts example.com
dig example.com
dig example.com A
dig example.com AAAA
```

## 4. Security Relevance

DNS information helps identify the addresses associated with a domain and understand parts of its infrastructure.

DNS results alone do not establish that a host is secure or identify its owner with certainty.

## 5. Key Takeaways

- DNS helps applications locate network resources.
- DNS records serve different purposes.
- DNS responses may be cached.
- A hostname can resolve to multiple IP addresses.