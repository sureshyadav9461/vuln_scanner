import requests

# Hardcoded target URL (no input)
url = "https://creatiqa.com"

# Hardcoded list of paths (no file)
paths = [
    "admin",
    "login",
    "config.php",
    "robots.txt",
    "uploads",
    ".git",
    "backup"
]

print(f"\n[+] Scanning started for {url}...\n")

for path in paths:
    full_url = f"{url.rstrip('/')}/{path}"
    try:
        response = requests.get(full_url, timeout=5)
        if response.status_code == 200:
            print(f"[FOUND] {full_url}")
        elif response.status_code == 403:
            print(f"[FORBIDDEN] {full_url}")
        else:
            print(f"[NOT FOUND] {full_url} ({response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] {full_url} --> {e}")

print("\n[✓] Scan Complete.\n")
