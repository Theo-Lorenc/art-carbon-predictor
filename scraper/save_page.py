# scraper/save_page.py

import requests

url = "https://greentrace.ice.com/art/projects"

html = requests.get(url).text

with open(
    "data/art_page.html",
    "w",
    encoding="utf-8"
) as f:
    f.write(html)

print("Saved")