# HTTP Methods, Headers and Status Codes

## 1. HTTP Methods

HTTP methods describe the intended action for a request.

| Method | Common Purpose |
|---|---|
| `GET` | Retrieve a representation of a resource |
| `HEAD` | Retrieve response headers without the response body |
| `POST` | Submit data or trigger resource-specific processing |
| `PUT` | Create or replace a resource at a known target URI |
| `PATCH` | Partially modify a resource |
| `DELETE` | Request deletion of a resource |
| `OPTIONS` | Discover communication options supported by a resource |

The actual behavior depends on the server and application implementation.

### Safe and Idempotent Methods

- Safe methods are intended not to change server state.
- An idempotent method has the same intended effect when repeated with the same request.

`GET` is defined as safe and idempotent. `PUT` and `DELETE` are idempotent by definition, although repeated responses may differ.

## 2. HTTP Request Headers

| Header | Purpose |
|---|---|
| `Host` | Identifies the target host in HTTP/1.1 |
| `User-Agent` | Describes the client software |
| `Accept` | Indicates acceptable response media types |
| `Content-Type` | Describes the media type of the message body |
| `Authorization` | Carries authentication credentials or tokens |
| `Cookie` | Sends stored cookies to the server |

Headers are inputs to application behavior. Their presence alone does not guarantee that the server handles them securely.

## 3. HTTP Response Headers

| Header | Purpose |
|---|---|
| `Content-Type` | Describes the response body media type |
| `Content-Length` | Indicates message body length when applicable |
| `Cache-Control` | Defines caching directives |
| `Set-Cookie` | Instructs the client to store a cookie |
| `Location` | Commonly identifies a redirect target |
| `Content-Security-Policy` | Defines browser-enforced content restrictions |

Security headers can help reduce risk, but they do not replace secure application logic.

## 4. HTTP Status Codes

| Code | Meaning |
|---|---|
| `200 OK` | Request succeeded |
| `201 Created` | A resource was created |
| `204 No Content` | Request succeeded without response content |
| `301 Moved Permanently` | Permanent redirect |
| `302 Found` | Temporary redirect in common usage |
| `400 Bad Request` | Request could not be processed due to a client-side request problem |
| `401 Unauthorized` | Authentication is required or has failed |
| `403 Forbidden` | Server refuses the request |
| `404 Not Found` | Resource was not found or is not being disclosed |
| `405 Method Not Allowed` | Method is not supported for the target resource |
| `429 Too Many Requests` | Rate limiting or request throttling |
| `500 Internal Server Error` | Unexpected server-side failure |
| `502 Bad Gateway` | Gateway received an invalid upstream response |
| `503 Service Unavailable` | Server is temporarily unable to handle the request |

### Important Distinctions

- `401` relates to authentication.
- `403` usually indicates that access is refused.
- `404` does not always prove that a resource does not exist.
- `500` indicates a server-side failure but does not identify its root cause.

## 5. Security Relevance

During authorized security testing, inspect:

- Whether sensitive information appears in responses
- Whether redirects expose unexpected destinations
- Whether access controls are enforced server-side
- Whether error responses reveal unnecessary implementation details
- Whether caching and security headers are appropriate

Never assume a vulnerability based only on one status code.

## 6. Key Takeaways

- Methods express the intended action of a request.
- Request and response headers provide metadata and influence behavior.
- Status codes describe the outcome at the HTTP level.
- Application authorization must be enforced server-side.
- Security conclusions require evidence beyond a single header or status code.

## 7. Practical Exercise

Status: Not started

- [ ] Inspect response status codes with `curl`
- [ ] Compare `curl -I` and `curl -i`
- [ ] Identify at least three response headers
- [ ] Record actual results after running the commands

### Observations

To be completed after running the commands.
