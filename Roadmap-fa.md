# 🛡️ AI Security Journey — Job-First Roadmap (v2)

## 🎯 هدف این مسیر

می‌خوام وارد **Cybersecurity** بشم و در ادامه روی **AI / LLM Security** تخصص بگیرم.

اول پایه‌ی Web و Application Security رو محکم می‌کنم، بعد Python رو وارد Security Automation می‌کنم، بعد یه LLM App واقعی می‌سازم و همون رو تست و Hack می‌کنم (Prompt، RAG، Agent).

* Lab زده باشم
* پروژه ساخته باشم
* Write-up (انگلیسی) نوشته باشم
* GitHub قابل ارائه داشته باشم
* و برای Jobهای Junior / Internship آماده بشم

```text
Python + Linux + Git
        ↓
Networking + HTTP + Web Security
        ↓
API Security
        ↓
Python Security Automation  →  Project 1
        ↓
LLM عملی (API + Tool Calling + mini RAG)
        ↓
LLM / AI Security (Prompt + RAG + Agent)
        ↓
AI Security Tools  →  Project 2
        ↓
Portfolio  →  Job Search
```

### چرا v2؟

نسخه‌ی اول چند مشکل داشت که اصلاح شد:

* Phase 1 خیلی فشرده بود (۲۱ موضوع در یک هفته) → حالا ۶ هفته با Buffer
* ۳ هفته ML تئوری برای Junior AI Security لازم نبود → حالا ۲ هفته‌ی عملی
* RAG / Agent دوبار (تئوری و لب جدا) اومده بود → حالا تئوری و لب همون هفته
* شش ابزار AI Security با قانون «ابزار جمع نکنم» نمی‌خوند → حالا ۲ ابزار اصلی
* Buffer نداشت → حالا هر چند هفته یک هفته‌ی جبرانی
* Networking، Docker، Secure Coding و Threat Modeling عمومی جا افتاده بود

---

# 🗺️ Roadmap

---

# Phase 0 — Foundation ✅

## Weeks 1–4

### Week 1 — GitHub + Git + Python Start

* [x] ساخت Repository
* [x] Git / GitHub basics
* [x] ساختار اولیه‌ی Repository
* [x] شروع Python
* [x] Linux basics
* [x] OverTheWire — Bandit
* [x] Gandalf — Level 5

### Week 2 — Python Fundamentals

* [x] Variables، Conditions، Loops، Functions
* [x] Lists / Dictionaries
* [x] OOP basics
* [x] تمرین‌های Python

### Week 3 — Files + JSON + APIs

* [x] File handling
* [x] JSON
* [x] `requests`
* [x] API basics
* [x] Scriptهای ساده
* [x] Response و Status Code

### Week 4 — Linux

* [x] Navigation، Files، Permissions، Processes
* [x] Networking basics
* [x] Bandit Levels 10–15
* [x] مرتب کردن بخش Linux Repository
* [x] Notes

---

# Phase 1 — Application Security

## Weeks 5–11

> اول Web و API رو بفهمم، بعد یاد بگیرم چطور از دید Security بررسی‌شون کنم.

### Week 5 — Security Intro + Python Projects ✅

این هفته طبق برنامه‌ی Security جلو نرفت و بیشتر روی Python و پروژه‌ها رفت.

* [x] Offensive vs Defensive Security
* [x] Pentesting / Red Teaming basics
* [x] Gobuster + Directory Brute-Forcing
* [x] Python projects (OOP، `pathlib`، `pyenv`، `venv`)
* [x] GUI و API-based projects

**نتیجه:** Python عملی‌تر شد. از اینجا به بعد پروژه‌های GUI اولویت نیستند.

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
اولین PortSwigger Labs
```

* [ ] DNS، TCP، TLS، Portها (در حد مفهوم)
* [ ] Nmap basics
* [ ] HTTP Request / Response
* [ ] Methods، Headers، Cookies، Parameters، Status Codes
* [ ] نصب و تنظیم Burp Suite
* [ ] Proxy، Intercept، Repeater
* [ ] شروع PortSwigger Web Security Academy
* [ ] حداقل ۳–۵ لب (Apprentice)
* [ ] ۱ Write-up

---

## Week 7 — SQL Injection + XSS

* [ ] SQLi (Apprentice + چند Practitioner)
* [ ] XSS (Reflected، Stored، DOM)
* [ ] نوشتن Payloadها و فهمیدن چرا کار می‌کنن
* [ ] Mitigation هر کدوم (Parameterized Queries، Output Encoding، CSP)
* [ ] حدود ۸ لب
* [ ] ۱–۲ Write-up

---

## Week 8 — Authentication + Access Control

* [ ] Authentication vulnerabilities
* [ ] Session / Cookie Security
* [ ] Access Control و IDOR
* [ ] Authorization vs Authentication
* [ ] حدود ۸ لب
* [ ] ۱–۲ Write-up

---

## Week 9 — Server-Side + Docker

* [ ] CSRF
* [ ] SSRF
* [ ] Path Traversal
* [ ] File Upload
* [ ] Command Injection
* [ ] Business Logic (مقدماتی)
* [ ] Docker basics + بالا آوردن OWASP Juice Shop به صورت لوکال
* [ ] حدود ۸ لب
* [ ] ۱–۲ Write-up

---

## Week 10 — API Security

* [ ] REST API basics از دید Security
* [ ] OWASP API Security Top 10 (مرور)
* [ ] JWT
* [ ] BOLA / Broken Access Control
* [ ] Mass Assignment
* [ ] Rate Limiting
* [ ] بالا آوردن crAPI با Docker و تمرین روی اون
* [ ] حدود ۸ لب / چالش
* [ ] ۱–۲ Write-up

---

## Week 11 — Buffer + Consolidation

هدف: چیزهای پراکنده جمع بشن و اگه جایی عقب افتادم جبران کنم.

* [ ] جبران Weekهای عقب‌افتاده
* [ ] مرور HTTP، Burp، SQLi، XSS، Access Control، SSRF، API
* [ ] مجموع Phase 1: حدود ۴۰ لب و ۸–۱۰ Write-up
* [ ] مطالعه‌ی STRIDE (Threat Modeling عمومی)
* [ ] شروع بررسی Jobها (چه Skillهایی می‌خوان؟)
* [ ] تمیز کردن بخش `web-security/` و `writeups/` در GitHub

### 🔜 بعد از Phase 1 (اختیاری / Advanced)

این‌ها مهم‌ان ولی سنگین‌تر از اینن که توی همون ۶ هفته بگنجن. هر وقت وقت شد:

* [ ] OAuth
* [ ] GraphQL
* [ ] Race Conditions
* [ ] لب‌های Practitioner بیشتر
* [ ] هدف بلندمدت: **BSCP** (Burp Suite Certified Practitioner)

---

# Phase 2 — Python Security Automation

## Weeks 12–13

> استفاده از Python برای Security و Automation.

### Week 12 — Security Automation

* [ ] `requests` و HTTP Automation
* [ ] JSON
* [ ] CLI و Argument Parsing (`argparse`)
* [ ] Error Handling و Logging
* [ ] Regex در حد کاربردی
* [ ] اجرای Linux Commandها با Python
* [ ] چند Security Script کوچیک (مثلاً چک Header، چک Status، تست IDOR ساده روی لب لوکال)
* [ ] Secure Coding مقدماتی: اجرای `bandit` و `pip-audit` روی پروژه‌های خودم (مثلاً `password-checker`)

```text
Python → HTTP / API → CLI → Automation → Security
```

### Week 13 — Project 1

## `api-security-checker`

یک ابزار Python/CLI برای بررسی اولیه‌ی Web/API Target.

* [ ] HTTP Methods و Status Codes
* [ ] Security Headers
* [ ] CORS
* [ ] Response Information
* [ ] Endpointهای قابل مشاهده
* [ ] CLI + خروجی مرتب
* [ ] README + Example Usage
* [ ] فقط روی Target مجاز تست بشه (لب لوکال / سایت خودم)

قرار نیست Scanner حرفه‌ای باشه. هدفش اینه که نشون بدم:

> Python + HTTP + Security رو می‌تونم کنار هم استفاده کنم.

**بعد از این Week (با حدود ۸+ Write-up و این پروژه) Apply کردن رو جدی‌تر شروع می‌کنم.**

---

# Phase 3 — LLM عملی

## Weeks 14–15

قرار نیست ML Engineer بشم. می‌خوام بدونم یه LLM App چطور ساخته می‌شه، چون همون رو بعداً تست می‌کنم.

### Week 14 — LLM Basics + اولین App

* [ ] مفاهیم در حد فهم: Training vs Inference، Overfitting، Evaluation
* [ ] Token، Embedding، Context Window
* [ ] Transformer / Attention (فقط شهودی)
* [ ] System Message / User Message
* [ ] صدا زدن یک LLM API با Python
* [ ] ساخت یه Chat App کوچیک با FastAPI

### Week 15 — Tool Calling + mini RAG

* [ ] Tool Calling / Function Calling
* [ ] Embedding + Vector Store ساده
* [ ] ساخت یه mini RAG روی چند سند
* [ ] Logging ورودی / خروجی

```text
User → Application → Prompt → LLM → Tools / Data / RAG → Response
```

این App همون **Target** فازهای بعدی هست.

> اگه بعداً کنجکاو شدم، Neural Network و Gradient Descent رو به صورت اختیاری می‌رم.

---

# Phase 4 — LLM / AI Security

## Weeks 16–18

هر هفته: **بفهم ← حمله کن ← Mitigation بنویس**. تئوری و لب همون هفته.

اسکلت موضوعات: **OWASP LLM Top 10** و **MITRE ATLAS**.

### Week 16 — Prompt + Output Security

* [ ] Prompt Injection (Direct / Indirect)
* [ ] Jailbreaking
* [ ] System Prompt Leakage
* [ ] Sensitive Information Disclosure (Secrets، PII، Credentialها)
* [ ] Unsafe Output Handling
* [ ] Input / Output Validation
* [ ] لب روی App خودم + Gandalf + HackAPrompt
* [ ] ۱–۲ Write-up

### Week 17 — RAG Security

```text
User → Application → Retriever → Vector DB → Documents → LLM → Answer
```

* [ ] Unauthorized Retrieval
* [ ] Document Injection / Retrieval Manipulation
* [ ] Data Leakage
* [ ] Access Control و Tenant Isolation
* [ ] Data / Model Poisoning
* [ ] Supply Chain Considerations
* [ ] لب روی mini RAG هفته‌ی ۱۵
* [ ] ۱–۲ Write-up

### Week 18 — Agent Security

```text
User → Agent → LLM ─┬─ Tool
                    ├─ API
                    ├─ Database
                    ├─ File System
                    └─ External Service
```

* [ ] Excessive Agency
* [ ] Tool Abuse و Unsafe Tool Calls
* [ ] Tool Permissions / Least Privilege
* [ ] Authorization Boundaries
* [ ] Secret Exposure
* [ ] Human-in-the-loop
* [ ] Tool Trust / Supply Chain
* [ ] AI-specific Threat Modeling
* [ ] لب روی یه Agent ساده (Search / File / API Tool)
* [ ] ۱–۲ Write-up

ساختار هر Finding:

```text
Attack → Reproduction → Observed Behavior → Impact → Mitigation
```

---

# Phase 5 — AI Security Tools + Project 2

## Weeks 19–21

اول مفهوم، بعد ابزار. برای هر ابزار باید جواب بدم:

> چی رو تست می‌کنه؟ چطور؟ نتیجه‌اش چی می‌گه؟

### Week 19 — Tools + Test Suite

**ابزار اصلی:** Promptfoo و Garak
**اختیاری:** PyRIT (تست)، LLM Guard (به عنوان Mitigation)

* [ ] نصب و اجرا روی App خودم
* [ ] ساخت Test Caseهای Prompt Injection، Jailbreak، System Prompt Leakage، Data Disclosure، Basic Tool Abuse
* [ ] بررسی Results
* [ ] False Positive / False Negative

### Week 20 — Project 2

## `llm-security-tester`

یک ابزار Python/CLI برای تست امنیت LLM Application.

* [ ] Test Cases
* [ ] Automated Requests
* [ ] Result Classification
* [ ] Logging
* [ ] JSON Output
* [ ] CLI
* [ ] Report (با ساختار Finding بالا)
* [ ] README

### Week 21 — Project Hardening

* [ ] تمیز کردن Code و Error Handling
* [ ] Documentation و Example Tests
* [ ] Screenshots و Demo
* [ ] GitHub Release / Tag

---

# Phase 6 — Portfolio + Job Search

## Weeks 22–24

### Week 22 — Buffer + Project 3

* [ ] جبران چیزای عقب‌افتاده
* [ ] جمع کردن لب‌های RAG و Agent به شکل **Project 3: Secure RAG / Agent Security Lab**
* [ ] برای هر Finding: Attack → Impact → Mitigation

### Week 23 — Portfolio

* [ ] README اصلی (معرفی، Architecture Diagram، لینک به پروژه‌ها و Write-upها)
* [ ] مرتب کردن Repository
* [ ] Screenshots و Demo
* [ ] Security Findings و Mitigations
* [ ] آماده کردن LinkedIn / رزومه‌ی کوتاه

### Week 24 — Job Search جدی

* [ ] Apply روزانه / هفتگی
* [ ] آماده‌سازی توضیح ۲ دقیقه‌ای هر پروژه
* [ ] مرور مسائل رایج مصاحبه (OWASP Top 10، HTTP، Auth)
* [ ] برنامه‌ریزی BSCP (اگه هنوز نشده)

### پروژه‌ها

```text
1. api-security-checker
2. llm-security-tester
3. Secure RAG / Agent Security Lab
```

### قالب Write-up (انگلیسی)

```text
Problem → Attack → Reproduction → Impact → Mitigation → What I Learned
```

---

# 💼 Job Search

* از **Week 11**: بازار رو نگاه می‌کنم و Skillهای تکراری رو یادداشت می‌کنم.
* از **Week 13** (بعد از Project 1 و حدود ۸+ Write-up): Apply جدی‌تر.
* از **Week 23**: تمرکز کامل روی Apply.

### Roleها

* Application Security Intern / Junior Application Security
* Security Engineer Intern
* Product Security Intern
* Security Automation / Python Security
* API Security
* AI Security Intern / LLM Security
* AI Application Security / GenAI Security
* AI Red Team / LLM Red Team

---

# 🧰 ابزارها

## Security

* Burp Suite
* PortSwigger Web Security Academy
* OWASP Juice Shop و crAPI (لوکال با Docker)
* TryHackMe
* OverTheWire
* Nmap

## Secure Coding

* Bandit
* pip-audit
* Semgrep (اختیاری)

## AI Security

* Promptfoo
* Garak
* PyRIT (اختیاری)
* LLM Guard (اختیاری، Mitigation)
* Gandalf و HackAPrompt (تمرین، نه ابزار)

## Development

* Python
* FastAPI
* Git / GitHub
* Docker
* Linux
* Colab
* Hugging Face

### Django

فعلاً Priority نیست. **Python + FastAPI** کافیه.

---

# 📚 منابع

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

# 🎯 خروجی نهایی

* [ ] HTTP و Web Security رو درست بفهمم و توضیح بدم
* [ ] با Burp کار کنم
* [ ] Vulnerabilityهای رایج Web و API رو تست و Mitigate کنم
* [ ] با Python ابزار Security بسازم
* [ ] معماری یه LLM App رو توضیح بدم
* [ ] Prompt Injection، RAG و Agent Security رو تست کنم
* [ ] Tool Abuse و Authorization Boundary رو بفهمم
* [ ] AI-specific Threat Modeling انجام بدم
* [ ] با Promptfoo و Garak کار کنم
* [ ] Findingها رو مستند کنم
* [ ] ۳ پروژه و حدود ۱۵+ Write-up روی GitHub داشته باشم
* [ ] برای Junior / Internship Roles آماده باشم

---

# 🚀 مسیر در یک نگاه

| Weeks | تمرکز |
|---|---|
| 1–4 ✅ | Foundation: Python + Linux + Git |
| 5 ✅ | Security Intro + Python Projects |
| 6 | Networking + HTTP + Burp |
| 7 | SQLi + XSS |
| 8 | Authentication + Access Control |
| 9 | CSRF، SSRF، File Upload، Command Injection + Docker |
| 10 | API Security |
| 11 | Buffer + Consolidation |
| 12–13 | Security Automation + Project 1 |
| 14–15 | LLM عملی (API، Tool Calling، mini RAG) |
| 16–18 | Prompt / RAG / Agent Security (تئوری + لب) |
| 19–21 | AI Security Tools + Project 2 |
| 22 | Buffer + Project 3 |
| 23–24 | Portfolio + Job Search |

## 📍 وضعیت فعلی

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

### قدم بعدی

**Networking → HTTP → Burp → اولین PortSwigger Labs**