import sys
import dewiki
import json
import requests

def _get_page(search):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "prop": "extracts",
        "format": "json",
        "explaintext": True,
        "titles": search,
        "redirects": True
    }
    headers = {"User-Agent": "TestApp/1.0 (test@student.42barcelona.com)" }
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    data = response.json()
    pages = data["query"]["pages"]
    return next(iter(pages.values()))

def _write_page(page, search):
    if "missing" in page or "extract" not in page:
        raise Exception(f"No results for '{search}'")
    filename = search.replace(" ", "_") + ".wiki"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(dewiki.from_string(page["extract"]))

def request_wikipedia(search):
    page = _get_page(search)
    _write_page(page, search)

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) == 2:
        try:
            request_wikipedia(argv[1].strip())
        except Exception as e:
            print(e)
    else:
        print(f'Use: request_wikipedia <search>')
