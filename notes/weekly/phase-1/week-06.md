# Week 06 — Networking, HTTP and Burp Suite

## Weekly Objective

Understand networking fundamentals, HTTP communication, and the basics of web security testing with Burp Suite.

## Day 1 — Networking Fundamentals

### Topics Studied

- [x] DNS
- [x] IP addresses
- [x] Ports
- [x] TCP
- [x] TLS and HTTPS

### Commands Practiced

Mark each command as completed only after executing it.

- [ ] `getent hosts example.com`
- [ ] `dig example.com`
- [ ] `ip addr`
- [ ] `ip route`
- [ ] `curl -I https://example.com`
- [ ] `curl -v https://example.com`

### Notes

- [Networking Overview](../../../web-security/README.md)
- [DNS](../../../web-security/networking/dns.md)
- [TCP, IP and Ports](../../../web-security/networking/tcp-ip-ports.md)
- [TLS and HTTPS](../../../web-security/networking/tls-https.md)

### Key Takeaways

- DNS resolves domain names into network-related records.
- IP addresses identify network interfaces or destinations; ports identify application endpoints.
- TCP provides reliable, ordered byte-stream delivery.
- TLS protects communication in transit.
- HTTPS does not guarantee that a web application is free of vulnerabilities.

### Problems Encountered

- None recorded yet.

### Day 1 Status

Networking notes have been created and committed. Practical command execution and verification remain pending.

## Day 2 — HTTP Fundamentals

### Topics

- [x] HTTP request and response structure
- [x] HTTP methods
- [x] Request and response headers
- [x] HTTP status codes
- [ ] Practical inspection with `curl`

### Notes

- [HTTP Requests and Responses](../../../web-security/http/requests-responses.md)
- [HTTP Methods, Headers and Status Codes](../../../web-security/http/methods-headers-status-codes.md)

### Practical Commands

- [ ] `curl -I https://example.com`
- [ ] `curl -v https://example.com`
- [ ] `curl -i https://example.com`

### Observations

To be completed after running the commands and reviewing their actual output.

### Day 2 Status

HTTP reference notes have been created and committed. Practical exercises remain pending.

## Day 3 — Cookies and Sessions

### Topics Studied
- [x] What are Cookies?
- [x] What are Sessions?
- [x] Cookies vs Sessions
- [x] How websites maintain user authentication
- [x] Session IDs and their purpose
- [x] Cookie attributes:
  - [x] `HttpOnly`
  - [x] `Secure`
  - [x] `SameSite`
  - [x] `Domain`
  - [x] `Path`
  - [x] `Expires`
  - [x] `Max-Age`
- [x] Session lifecycle:
  - [x] Session creation
  - [x] Session identification
  - [x] Session expiration
  - [x] Session invalidation (Logout)

### Practical Commands
- [x] `curl -i https://httpbin.org/cookies`
- [x] `curl -i https://httpbin.org/cookies/set/test/session123`
- [x] `curl -i -c cookies.txt https://httpbin.org/cookies/set/test/session123`
- [x] `cat cookies.txt`
- [x] `curl -i -b cookies.txt https://httpbin.org/cookies`
- [x] `curl -i -b "test=session123" https://httpbin.org/cookies`

### Browser Practice
- [x] Inspected cookies using Browser Developer Tools.
- [x] Navigated to Application → Storage → Cookies.
- [x] Inspected cookie names and values.
- [x] Reviewed `HttpOnly`, `Secure`, and `SameSite` attributes.
- [x] Observed how cookies are transmitted with HTTP requests.
- [x] Reviewed cookie behavior during authentication.

### Security Concepts Studied
- [x] Session Hijacking
- [x] Session Fixation
- [x] Insecure Cookie Configuration
- [x] Session Expiration Problems
- [x] Secure Session Management

### Notes
- [Cookies and Sessions](../../../web-security/http/cookies-sessions.md)

### Key Takeaways
- Cookies are small pieces of data stored by the browser.
- Sessions allow web applications to maintain user state across multiple HTTP requests.
- Session IDs are commonly stored in cookies.
- `HttpOnly` prevents JavaScript from accessing a cookie.
- `Secure` restricts cookie transmission to HTTPS connections.
- `SameSite` helps control cross-site cookie transmission.
- Session IDs must be unpredictable and securely managed.
- Logging out should invalidate the server-side session.
- Improper cookie configuration can introduce security vulnerabilities.

### Problems Encountered
- No major problems were recorded.
- Reviewed the differences between browser-side cookies and server-side sessions.

### Solutions
- Used `curl` to inspect HTTP responses and cookie behavior.
- Used Browser Developer Tools to examine cookie attributes.
- Compared cookie storage and transmission mechanisms.

### Day 3 Status
Completed. Studied Cookies and Sessions, reviewed important security attributes, and examined cookie behavior through command-line and browser tools.

### Deliverables
- Created `web-security/http/cookies-sessions.md`.
- Documented Cookies vs Sessions.
- Recorded practical command examples.
- Documented important cookie security attributes.
- Updated Week 06 progress.

## Day 4 — Burp Suite Setup


## Day 5 — Repeater and Labs

Not started.

## Day 6 — Practical Labs and Write-up

Not started.

## Day 7 — Review

Not started.

## Weekly Summary

To be completed at the end of Week 6.

## Next Week

SQL Injection and Cross-Site Scripting (XSS).