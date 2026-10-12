# TLS and HTTPS

## 1. TLS

Transport Layer Security protects communication between network endpoints.

Its main security properties include:

- Confidentiality
- Integrity
- Authentication

## 2. HTTPS

HTTPS is HTTP carried over TLS.

For HTTP/1.1 and HTTP/2 over TLS, TCP is commonly used as the transport protocol.

HTTP/3 uses QUIC over UDP.

## 3. Certificates

TLS certificates bind an identity to a public key through a certificate validation process.

Certificate validation includes checks such as:

- Certificate chain trust
- Validity period
- Hostname matching

## 4. Practical Commands

Inspect HTTP response headers:

```bash
curl -I https://example.com
```

Inspect connection and TLS details:

```bash
curl -v https://example.com
```

Inspect certificate information:

```bash
openssl s_client \
  -connect example.com:443 \
  -servername example.com
```

## 5. Security Limitations

HTTPS protects communication in transit but does not guarantee that the application is secure.

An HTTPS website can still contain vulnerabilities such as:

- SQL Injection
- Cross-Site Scripting
- Broken Access Control
- Insecure File Upload

## 6. Key Takeaways

- TLS protects data in transit.
- Certificate validation helps authenticate the server.
- HTTPS does not automatically secure application logic or authorization.s