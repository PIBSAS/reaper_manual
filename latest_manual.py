import requests
import re

url = "https://www.reaper.fm/userguide.php"
r = requests.get(url)
r.raise_for_status()
html = r.text

matches = re.findall(r"ReaperUserGuide(\d+[a-zA-Z]*)\.pdf", html)

if not matches:
    raise ValueError("No se encontró ningún PDF")


def sort_key(ver):
    num_match = re.match(r"(\d+)", ver)
    num = int(num_match.group(1)) if num_match else 0
    suffix = ver[len(str(num)):] 
    return (num, suffix)

latest_ver = sorted(matches, key=sort_key, reverse=True)[0]

latest_url = f"https://www.reaper.fm/userguide/ReaperUserGuide{latest_ver}.pdf"


with open("latest.txt", "w") as f:
    f.write(latest_url)

print(f"Última URL: {latest_url}")
