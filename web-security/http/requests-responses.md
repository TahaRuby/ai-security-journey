# HTTP Requests and Responses

## 1. What Is HTTP?

HTTP (Hypertext Transfer Protocol) is an application-layer protocol used for communication between clients and servers.

A client sends an HTTP request, and the server returns an HTTP response.

Examples of HTTP clients include web browsers, command-line tools, and mobile applications.

## 2. HTTP Request Structure

An HTTP/1.1 request commonly contains:

1. Request line
2. Headers
3. Optional message body

Example:

```http
GET / HTTP/1.1
Host: example.com
User-Agent: curl/8.x
Accept: */*

```

### Request Line

The request line contains:

- Method: `GET`
- Request target: `/`
- HTTP version: `HTTP/1.1`

### Headers

Headers provide additional information about the request.

Examples:

- `Host`: identifies the target host.
- `User-Agent`: identifies the client software.
- `Accept`: indicates which response media types the client can accept.
- `Content-Type`: describes the media type of the request body.

### Request Body

The body is optional. It is commonly used to send data with requests such as `POST` or `PUT`.

A `GET` request generally does not need a body.

## 3. HTTP Response Structure

An HTTP/1.1 response commonly contains:

1. Status line
2. Headers
3. Optional message body

Example:

```http
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1256

```

### Status Line

The status line contains:

- HTTP version
- Status code
- Reason phrase

For example, `200 OK` indicates that the request succeeded.

### Response Headers

Response headers provide information about the response.

Examples:

- `Content-Type`: describes the response body's media type.
- `Content-Length`: indicates the message body length when applicable.
- `Cache-Control`: provides caching directives.
- `Set-Cookie`: asks the client to store a cookie.

### Response Body

The body may contain HTML, JSON, images, files, or other data. Some responses do not include a body.

## 4. HTTP and HTTPS

HTTP defines the application-level request and response semantics.

HTTPS is HTTP protected by TLS, which provides confidentiality and integrity in transit and helps authenticate the server.

HTTPS does not guarantee that an application is free of vulnerabilities.

## 5. Security Relevance

When testing a web application, inspecting requests and responses helps identify:

- Exposed information
- Authentication and session behavior
- Unexpected server responses
- Missing or incorrect security controls

Testing must be performed against systems you own or are authorized to assess.

## 6. Key Takeaways

- A client sends requests; a server returns responses.
- Requests can contain a method, target, headers, and optional body.
- Responses contain a status code, headers, and an optional body.
- HTTP headers influence how requests and responses are interpreted.
- HTTPS protects data in transit but does not fix application-level vulnerabilities.

## 7. Practical Exercise

Status: Not started

Commands and observations will be recorded after the practical exercises are completed.

- [ ] Inspect response headers with `curl`
- [ ] Inspect request and response details with `curl -v`
- [ ] Record the observed status code
- [ ] Record relevant response headers

### Observations

To be completed after running the commands.

