# 🛡️ AI Security Journey — Job-First Roadmap (v2)

## 🎯 Goal

I want to enter **Cybersecurity** and eventually specialize in **AI / LLM Security**.

First, I will build a strong foundation in Web and Application Security. Then I will bring Python into Security Automation. After that, I will build a real LLM application and test/hack the same application across Prompt, RAG, and Agent security.

By the end, I want to have:

* Completed hands-on labs
* Built real projects
* Written English security write-ups
* A presentable GitHub portfolio
* Readiness for Junior / Internship roles

```text
Python + Linux + Git
        ↓
Networking + HTTP + Web Security
        ↓
API Security
        ↓
Python Security Automation → Project 1
        ↓
Practical LLM (API + Tool Calling + mini RAG)
        ↓
LLM / AI Security (Prompt + RAG + Agent)
        ↓
AI Security Tools → Project 2
        ↓
Portfolio → Job Search
```

### Why v2?

The first version had several problems that have now been fixed:

* Phase 1 was too compressed → now 6 weeks + a Buffer
* Three weeks of ML theory were unnecessary for Junior AI Security → now 2 practical weeks
* RAG / Agent topics were duplicated between theory and labs → now theory and labs happen in the same week
* Six AI Security tools conflicted with the "don't collect tools" rule → now 2 main tools
* There was no Buffer → now there are dedicated catch-up weeks
* Networking, Docker, Secure Coding, and general Threat Modeling were missing

---

# 🗺️ Roadmap

---

# Phase 0 — Foundation ✅

## Weeks 1–4

### Week 1 — GitHub + Git + Python Start

* [x] Create Repository
* [x] Git / GitHub basics
* [x] Initial Repository structure
* [x] Start Python
* [x] Linux basics
* [x] OverTheWire — Bandit
* [x] Gandalf — Level 5

### Week 2 — Python Fundamentals

* [x] Variables, Conditions, Loops, Functions
* [x] Lists / Dictionaries
* [x] OOP basics
* [x] Python exercises

### Week 3 — Files + JSON + APIs

* [x] File handling
* [x] JSON
* [x] `requests`
* [x] API basics
* [x] Simple scripts
* [x] Response and Status Codes

### Week 4 — Linux

* [x] Navigation, Files, Permissions, Processes
* [x] Networking basics
* [x] Bandit Levels 10–15
* [x] Organize the Linux section of the Repository
* [x] Notes

---

# Phase 1 — Application Security

## Weeks 5–11

> First understand Web and API systems, then learn how to assess them from a Security perspective.

### Week 5 — Security Intro + Python Projects ✅

This week did not follow the Security plan exactly and was mostly focused on Python and practical projects.

* [x] Offensive vs Defensive Security
* [x] Pentesting / Red Teaming basics
* [x] Gobuster + Directory Brute-Forcing
* [x] Python projects (OOP, `pathlib`, `pyenv`, `venv`)
* [x] GUI and API-based projects

**Result:** Python became more practical. From now on, GUI projects are no longer a priority.

---

## Week 6 — Networking + HTTP + Burp

```text
DNS / TCP / TLS
      ↓
HTTP
      ↓
Burp Suite
      ↓
Requests / Responses
      ↓
First PortSwigger Labs
```

* [ ] DNS, TCP, TLS, Ports (conceptual level)
* [ ] Nmap basics
* [ ] HTTP Request / Response
* [ ] Methods, Headers, Cookies, Parameters, Status Codes
* [ ] Install and configure Burp Suite
* [ ] Proxy, Intercept, Repeater
* [ ] Start PortSwigger Web Security Academy
* [ ] At least 3–5 Apprentice labs
* [ ] 1 Write-up

---

## Week 7 — SQL Injection + XSS

* [ ] SQLi (Apprentice + some Practitioner)
* [ ] XSS (Reflected, Stored, DOM)
* [ ] Write payloads and understand why they work
* [ ] Mitigation for each (Parameterized Queries, Output Encoding, CSP)
* [ ] Around 8 labs
* [ ] 1–2 Write-ups

---

## Week 8 — Authentication + Access Control

* [ ] Authentication vulnerabilities
* [ ] Session / Cookie Security
* [ ] Access Control and IDOR
* [ ] Authorization vs Authentication
* [ ] Around 8 labs
* [ ] 1–2 Write-ups

---

## Week 9 — Server-Side + Docker

* [ ] CSRF
* [ ] SSRF
* [ ] Path Traversal
* [ ] File Upload
* [ ] Command Injection
* [ ] Business Logic (intro)
* [ ] Docker basics + run OWASP Juice Shop locally
* [ ] Around 8 labs
* [ ] 1–2 Write-ups

---

## Week 10 — API Security

* [ ] REST API basics from a Security perspective
* [ ] OWASP API Security Top 10 (overview)
* [ ] JWT
* [ ] BOLA / Broken Access Control
* [ ] Mass Assignment
* [ ] Rate Limiting
* [ ] Run crAPI with Docker and practice on it
* [ ] Around 8 labs / challenges
* [ ] 1–2 Write-ups

---

## Week 11 — Buffer + Consolidation

Goal: consolidate scattered knowledge and catch up if anything was missed.

* [ ] Catch up on delayed weeks
* [ ] Review HTTP, Burp, SQLi, XSS, Access Control, SSRF, API Security
* [ ] Phase 1 total: around 40 labs and 8–10 Write-ups
* [ ] Study STRIDE (general Threat Modeling)
* [ ] Start reviewing Job requirements (which Skills appear repeatedly?)
* [ ] Clean up `web-security/` and `writeups/` on GitHub

### 🔜 After Phase 1 — Optional / Advanced

These topics are important but heavier than what should fit into the main 6-week sequence:

* [ ] OAuth
* [ ] GraphQL
* [ ] Race Conditions
* [ ] More Practitioner labs
* [ ] Long-term goal: **BSCP (Burp Suite Certified Practitioner)**

---

# Phase 2 — Python Security Automation

## Weeks 12–13

> Use Python for Security and Automation.

### Week 12 — Security Automation

* [ ] `requests` and HTTP Automation
* [ ] JSON
* [ ] CLI and Argument Parsing (`argparse`)
* [ ] Error Handling and Logging
* [ ] Practical Regex
* [ ] Execute Linux Commands with Python
* [ ] Several small Security Scripts (e.g. Header Checker, Status Checker, simple IDOR test on a local lab)
* [ ] Secure Coding basics: run `bandit` and `pip-audit` on my own projects (e.g. `password-checker`)

```text
Python → HTTP / API → CLI → Automation → Security
```

### Week 13 — Project 1

## `api-security-checker`

A Python/CLI tool for basic analysis of a Web/API Target.

* [ ] HTTP Methods and Status Codes
* [ ] Security Headers
* [ ] CORS
* [ ] Response Information
* [ ] Observable Endpoints
* [ ] Clean CLI + Output
* [ ] README + Example Usage
* [ ] Test only authorized Targets (local lab / my own site)

This is not intended to be a professional scanner.

The goal is to demonstrate:

> Python + HTTP + Security can be used together.

**After this week (with around 8+ Write-ups and this project), start applying more seriously.**

---

# Phase 3 — Practical LLM

## Weeks 14–15

I am not trying to become an ML Engineer. I want to understand how an LLM application is built because I will later test that same application.

### Week 14 — LLM Basics + First App

* [ ] Concepts at an understanding level: Training vs Inference, Overfitting, Evaluation
* [ ] Token, Embedding, Context Window
* [ ] Transformer / Attention (intuition only)
* [ ] System Message / User Message
* [ ] Call an LLM API with Python
* [ ] Build a small Chat App with FastAPI

### Week 15 — Tool Calling + mini RAG

* [ ] Tool Calling / Function Calling
* [ ] Embedding + simple Vector Store
* [ ] Build a mini RAG over several documents
* [ ] Input / Output Logging

```text
User → Application → Prompt → LLM → Tools / Data / RAG → Response
```

This App becomes the **Target** for the following phases.

> If I become curious later, I can study Neural Networks and Gradient Descent optionally.

---

# Phase 4 — LLM / AI Security

## Weeks 16–18

Every week:

**Understand → Attack → Write Mitigation**

Main frameworks:

**OWASP LLM Top 10** and **MITRE ATLAS**

### Week 16 — Prompt + Output Security

* [ ] Prompt Injection (Direct / Indirect)
* [ ] Jailbreaking
* [ ] System Prompt Leakage
* [ ] Sensitive Information Disclosure (Secrets, PII, Credentials)
* [ ] Unsafe Output Handling
* [ ] Input / Output Validation
* [ ] Labs on my own App + Gandalf + HackAPrompt
* [ ] 1–2 Write-ups

### Week 17 — RAG Security

```text
User → Application → Retriever → Vector DB → Documents → LLM → Answer
```

* [ ] Unauthorized Retrieval
* [ ] Document Injection / Retrieval Manipulation
* [ ] Data Leakage
* [ ] Access Control and Tenant Isolation
* [ ] Data / Model Poisoning
* [ ] Supply Chain Considerations
* [ ] Lab on the mini RAG from Week 15
* [ ] 1–2 Write-ups

### Week 18 — Agent Security

```text
User → Agent → LLM ─┬─ Tool
                    ├─ API
                    ├─ Database
                    ├─ File System
                    └─ External Service
```

* [ ] Excessive Agency
* [ ] Tool Abuse and Unsafe Tool Calls
* [ ] Tool Permissions / Least Privilege
* [ ] Authorization Boundaries
* [ ] Secret Exposure
* [ ] Human-in-the-loop
* [ ] Tool Trust / Supply Chain
* [ ] AI-specific Threat Modeling
* [ ] Lab on a simple Agent (Search / File / API Tool)
* [ ] 1–2 Write-ups

Finding structure:

```text
Attack → Reproduction → Observed Behavior → Impact → Mitigation
```

---

# Phase 5 — AI Security Tools + Project 2

## Weeks 19–21

First understand the concept, then use the tool.

For every tool I should be able to answer:

> What does it test? How does it test it? What does the result mean?

### Week 19 — Tools + Test Suite

**Main tools:** Promptfoo and Garak

**Optional:** PyRIT (testing), LLM Guard (Mitigation)

* [ ] Install and run them on my App
* [ ] Build Test Cases for Prompt Injection, Jailbreak, System Prompt Leakage, Data Disclosure, and Basic Tool Abuse
* [ ] Review Results
* [ ] False Positive / False Negative

### Week 20 — Project 2

## `llm-security-tester`

A Python/CLI tool for testing the security of an LLM Application.

* [ ] Test Cases
* [ ] Automated Requests
* [ ] Result Classification
* [ ] Logging
* [ ] JSON Output
* [ ] CLI
* [ ] Report (using the Finding structure above)
* [ ] README

### Week 21 — Project Hardening

* [ ] Clean Code and Error Handling
* [ ] Documentation and Example Tests
* [ ] Screenshots and Demo
* [ ] GitHub Release / Tag

---

# Phase 6 — Portfolio + Job Search

## Weeks 22–24

### Week 22 — Buffer + Project 3

* [ ] Catch up on delayed work
* [ ] Combine the RAG and Agent labs into **Project 3: Secure RAG / Agent Security Lab**
* [ ] For each Finding: Attack → Impact → Mitigation

### Week 23 — Portfolio

* [ ] Main README (Introduction, Architecture Diagram, Project and Write-up links)
* [ ] Organize Repository
* [ ] Screenshots and Demo
* [ ] Security Findings and Mitigations
* [ ] Prepare LinkedIn / short Resume

### Week 24 — Serious Job Search

* [ ] Apply daily / weekly
* [ ] Prepare a 2-minute explanation of each project
* [ ] Review common interview topics (OWASP Top 10, HTTP, Auth)
* [ ] Plan BSCP (if not completed)

### Projects

```text
1. api-security-checker
2. llm-security-tester
3. Secure RAG / Agent Security Lab
```

### Write-up Template (English)

```text
Problem → Attack → Reproduction → Impact → Mitigation → What I Learned
```

---

# 💼 Job Search

* From **Week 11**: Review the market and note repeatedly requested Skills.
* From **Week 13** (after Project 1 and around 8+ Write-ups): Apply more seriously.
* From **Week 23**: Full focus on applications.

### Roles

* Application Security Intern / Junior Application Security
* Security Engineer Intern
* Product Security Intern
* Security Automation / Python Security
* API Security
* AI Security Intern / LLM Security
* AI Application Security / GenAI Security
* AI Red Team / LLM Red Team

---

# 🧰 Tools

## Security

* Burp Suite
* PortSwigger Web Security Academy
* OWASP Juice Shop and crAPI (local with Docker)
* TryHackMe
* OverTheWire
* Nmap

## Secure Coding

* Bandit
* pip-audit
* Semgrep (optional)

## AI Security

* Promptfoo
* Garak
* PyRIT (optional)
* LLM Guard (optional, Mitigation)
* Gandalf and HackAPrompt (practice, not tools)

## Development

* Python
* FastAPI
* Git / GitHub
* Docker
* Linux
* Colab
* Hugging Face

### Django

Not a priority for now. **Python + FastAPI** is enough.

---

# 📚 Resources

* OWASP Top 10
* OWASP API Security Top 10
* OWASP Top 10 for LLM Applications
* MITRE ATLAS
* PortSwigger Web Security Academy
* Lakera Blog
* AI Incident Database
* Simon Willison
* TryHackMe
* OverTheWire

---

# 🎯 Final Outcomes

* [ ] Properly understand and explain HTTP and Web Security
* [ ] Work with Burp
* [ ] Test and mitigate common Web and API vulnerabilities
* [ ] Build Security tools with Python
* [ ] Explain the architecture of an LLM App
* [ ] Test Prompt Injection, RAG, and Agent Security
* [ ] Understand Tool Abuse and Authorization Boundaries
* [ ] Perform AI-specific Threat Modeling
* [ ] Work with Promptfoo and Garak
* [ ] Document Findings
* [ ] Have 3 projects and around 15+ Write-ups on GitHub
* [ ] Be ready for Junior / Internship Roles

---

# 🚀 Roadmap at a Glance

| Weeks | Focus                                               |
| ----- | --------------------------------------------------- |
| 1–4 ✅ | Foundation: Python + Linux + Git                    |
| 5 ✅   | Security Intro + Python Projects                    |
| 6     | Networking + HTTP + Burp                            |
| 7     | SQLi + XSS                                          |
| 8     | Authentication + Access Control                     |
| 9     | CSRF, SSRF, File Upload, Command Injection + Docker |
| 10    | API Security                                        |
| 11    | Buffer + Consolidation                              |
| 12–13 | Security Automation + Project 1                     |
| 14–15 | Practical LLM (API, Tool Calling, mini RAG)         |
| 16–18 | Prompt / RAG / Agent Security (Theory + Labs)       |
| 19–21 | AI Security Tools + Project 2                       |
| 22    | Buffer + Project 3                                  |
| 23–24 | Portfolio + Job Search                              |

## 📍 Current Status

```text
Phase 0  ██████████  Done

Phase 1  ██░░░░░░░░  In Progress
                ↑
            Week 6

Phase 2  ░░░░░░░░░░  Next
Phase 3  ░░░░░░░░░░
Phase 4  ░░░░░░░░░░
Phase 5  ░░░░░░░░░░
Phase 6  ░░░░░░░░░░
```

### Next Step

**Networking → HTTP → Burp → First PortSwigger Labs**
