# directory_scanner
"A basic web vulnerability scanner using Python"
# 🔍 Web directory scanner (Python)

This is a beginner-friendly Python-based tool that scans a target website for common hidden or sensitive paths such as `/admin`, `/login`, `.git`, etc.

---

## 🚀 Features

- Scans a website for known risky paths
- Displays status codes (200 OK, 403 Forbidden, 404 Not Found)
- Uses a **built-in list** of paths to scan (no external wordlist required)
- Beginner-friendly and easy to run from terminal

---

## 📁 Files in this Project

| File         | Description                          |
|--------------|--------------------------------------|
| `suresh.py`  | Main Python scanner script with built-in path list |
| `README.md`  | This file (project description)      |

---

## ▶️ How to Run

```bash
python suresh.py

pgsql

admin
login
config.php
robots.txt
.git
uploads
backup

output sample
[FOUND] https://testphp.vulnweb.com/admin
[FORBIDDEN] https://testphp.vulnweb.com/.git
[NOT FOUND] https://testphp.vulnweb.com/config.php

⚠️ Disclaimer
This tool is made for educational purposes only.
Do NOT use it to scan websites without permission.
The creator is not responsible for any misuse.
