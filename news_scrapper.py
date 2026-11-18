import re, csv, time, requests
from bs4 import BeautifulSoup

BASE = "https://www.onmanorama.com"          # English edition of Manorama Online
HDR = {"User-Agent": "Mozilla/5.0"}

def get_soup(url):
    return BeautifulSoup(requests.get(url, headers=HDR, timeout=15).text, "html.parser")

def meta(s, prop):
    t = s.find("meta", property=prop)
    return t["content"].strip() if t and t.get("content") else ""

# 1. collect article links (pattern: /news/kerala/2025/07/11/slug.html)
links = {BASE + a["href"] if a["href"].startswith("/") else a["href"]
         for a in get_soup(BASE).select("a[href]")
         if re.search(r"/\d{4}/\d{2}/\d{2}/.+\.html$", a["href"])}

# 2. visit each article and extract headline, date, category
rows = []
for url in list(links)[:20]:
    s = get_soup(url)
    title = meta(s, "og:title") or s.h1.get_text(strip=True)
    m = re.search(r"/([^/]+)/(\d{4})/(\d{2})/(\d{2})/", url)      # /category/yyyy/mm/dd/
    date = meta(s, "article:published_time") or "-".join(m.groups()[1:])
    category = meta(s, "article:section") or m.group(1)
    rows.append([title, date, category, url])
    time.sleep(1)                              # be polite to the server

# 3. save to CSV
with open("headlines.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["Headline", "Publication Date", "Category", "URL"])
    w.writerows(rows)
print(f"Saved {len(rows)} headlines to headlines.csv")
