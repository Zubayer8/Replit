import requests
from bs4 import BeautifulSoup

WORKER_URL = "https://quiet-math-98cd.zhtamim000.workers.dev/"

def shorten_with_worker(original_url):
    try:
        response = requests.get(WORKER_URL, params={"url": original_url}, timeout=10)
        if response.ok:
            return response.text.strip()
    except Exception as e:
        print("[Shorten Error]", e)
    return original_url

def search_anime(query):
    url = f"https://toonworld4all.co.in/?s={query.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        raise Exception(f"ToonWorld4All error: {e}")

    soup = BeautifulSoup(response.text, "lxml")
    posts = soup.select("h2.entry-title > a")
    if not posts:
        raise Exception("No anime posts found.")

    results = []
    for a in posts[:5]:
        title = a.text.strip()
        link = a["href"]
        short_link = shorten_with_worker(link)
        results.append({
            "title": title,
            "link": short_link
        })

    return results
