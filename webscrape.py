import requests
from bs4 import BeautifulSoup

def web_scraper(url, depth):
    # Error handling for user input
    try:
        depth = int(depth)
    except ValueError:
        print("Invalid depth. Please enter an integer value.")
        return

    # Error handling for requests
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to get {url}: {e}")
        return

    # Error handling for BeautifulSoup
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        print(f"An error occurred while parsing HTML: {e}")
        return

    # Error handling for file operations
    try:
        with open('scrapedpage.txt', 'a') as file:
            file.write(str(soup.prettify()))
    except Exception as e:
        print(f"An error occurred while writing to file: {e}")
        return

    # Recursive error handling
    if depth > 0:
        link_tags = soup.find_all('a')
        for link in link_tags:
            try:
                if 'href' in link.attrs:
                    new_url = link.get('href')
                    web_scraper(new_url, depth - 1)
            except Exception as e:
                print(f"An error occurred while processing link {link}: {e}")
                continue
