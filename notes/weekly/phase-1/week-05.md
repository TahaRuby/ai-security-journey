# Day 1 - TryHackMe: Offensive Security Intro

## Learned

### Offensive vs Defensive Security
- **Offensive Security**: شبیه‌سازی رفتار هکر برای پیدا کردن آسیب‌پذیری قبل از اینکه یه مهاجم واقعی پیداش کنه
- **Defensive Security**: محافظت و دفاع از سیستم در برابر حمله
- این دوره روی مسیر Offensive تمرکز داره (Penetration Testing / Red Teaming)

### Directory Brute-forcing با Gobuster
- خیلی از سایت‌ها صفحات مخفی دارن که جایی لینک نشدن (مثل پنل ادمین یا صفحات تست) ولی هنوز روی سرور فعالن
- **Gobuster** یه ابزار خط‌فرمانیه که یه لیست از اسم‌های احتمالی (wordlist) رو یکی‌یکی روی آدرس سایت امتحان می‌کنه تا ببینه کدوم صفحه واقعاً وجود داره
- دستور پایه:
```bash
  gobuster -u http://target.com -w wordlist.txt dir
```
  - `-u` → آدرس هدف