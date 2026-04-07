# Django - 1 - Lib

##  Exercise 00 — Antigravity

- Create geohashing.py that accepts parameters, computes a geohash, and prints it.
- Use only sys and antigravity modules.
- On error print a relevant message and exit.

| Example of use| Expected answer |
| --- | --- |
| `python3 geohashing.py 37.421542 -122.085589 2005-05-26-10458.68` | `37.421542, -122.544543`|

##   Exercise 01 — Pip

- Write a .sh script that:
    - Shows pip version,
    - Installs the development version of path.py from GitHub into repo/local_lib (overwrite if exists),
    - Logs install output to a .log file,
    - Runs the Python program if install succeeded.
- Write a Python program that imports path from the installed location, creates a folder and a file, writes text, then reads and displays it.
- Use : `. ./myscript.sh`

##  Exercise 02 — request an API 1

- Build request_wikipedia.py that takes a search string, queries Wikipedia API (FR or EN), and writes a plain-text result to name_of_search.wiki (no spaces).
- Must still write a result when requests are misspelled if Wikipedia returns a match.
- On missing/invalid parameters, server errors, or no result: do not create a file and print an error.
- Include requirement.txt listing needed libs.

- Activate __venv__ and download modules :
    - ```
        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirement.txt
        ```
- Example of use : `python3 request_wikipedia.py "chocolatine"

## Exercise 03 — request an API 2

- Implement roads_to_philosophy.py that takes a search term (unique match), fetches the English Wikipedia HTML (NOT API), and uses BeautifulSoup to:
    - Handle in-page redirections,
    - Extract page title and the first valid link in the intro (ignoring help links),
    - Follow links repeatedly until reaching the "Philosophy" page, hitting a dead end (no valid link), or detecting a loop.
- Print visited article titles and final message: either " roads from to philosophy !" or "It's a dead end !" or "It leads to an infinite loop !".

- Activate __venv__ and download modules :
    - ```
        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirement.txt
        ```
    
- Examples of use :
    - `python3 roads_to_phylosophy.py "philo"`
    - `python3 roads_to_phylosophy.py "ttttttt"`

## Exercise 04: Virtualenv

- Create requirement.txt listing latest stable django and psycopg2.
- Provide a .sh script that:
    - Creates a Python 3 virtualenv named django_venv.
    - Installs the packages from requirement.txt into that virtualenv.
    - Leaves the virtualenv activated when the script exits.
- Use : `. ./myscript.sh`

## Exercise 05: Hello World
    
- Create a Django project (repo is the project folder).
- Follow/adapt the official tutorial to make a page at [http://localhost:8000/helloworld](http://localhost:8000/helloworld) that displays: "Hello World !".

> Tip : view.py

- Use :
    - venv activation : `. ./myscript.sh`
    - now in __django_venv__ :
        - ```
            cd ex05_django
            python3 manage.py runserver
            ```
    - In browser  [http://localhost:8000/helloworld](http://localhost:8000/helloworld)
