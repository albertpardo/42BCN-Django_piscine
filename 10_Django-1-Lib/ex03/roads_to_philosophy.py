from bs4 import BeautifulSoup
import requests
import sys

def _get_soup_format(link, session):
    URL = 'https://en.wikipedia.org' 
    url = URL + link

    headers = { "User-Agent": "TestApp/1.0 (test@student.42barcelona.com)" }
    
    resp = session.get(url, headers=headers, allow_redirects=True)
    resp.raise_for_status()

    return BeautifulSoup(resp.content, 'html.parser')

def _get_first_valid_link(soup):
    # Go to main content
    content = soup.find(id="mw-content-text")
    if not content:
        return None

    paragraphs = content.find_all('p')
    for p in paragraphs:
        if p.get_text(strip=True) == '':
            continue  # avoid empty paragraphs

        # look for first valid link in the first paragraph with content
        for a in p.find_all('a', href=True):
            link = a['href']
            if link.startswith('/wiki/') and ':' not in link and '#' not in link:
                return link
        return None
    return None

def roads_to_phylosophy(search):
    title_list = []
    
    title = " ".join([s.lower() for s in search.split() if s])
    link = "/wiki/" + title
    session = requests.session()

    while True:
        soup = _get_soup_format(link, session)
        # Check visited titles and update title_list
        page_title = soup.title.string.rsplit(" - ", 1)[0]     # avoid " - Wikipedia" at the end of the title
        if page_title in title_list:
            raise Exception("It leads to an infinite loop !")
        title_list.append(page_title)
        # Is Philo?
        if page_title == "Philosophy":
            for t in title_list:
                print(t)
            print(f'{len(title_list)} roads from {title} to philosophy !')
            return
        # find a valid link
        link = _get_first_valid_link(soup)
        if link is None:
            raise Exception("It leads to a dead end !")

if __name__ == "__main__":
    argv = sys.argv
    if (len(argv) and len(argv) == 2):
        try:
            roads_to_phylosophy(argv[1])
        except Exception as e:
            print(e)
    else:
        print(f'Use: roads_to_phylosophy <search>')
