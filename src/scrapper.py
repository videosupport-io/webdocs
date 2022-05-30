import requests
from bs4 import BeautifulSoup


def scrap_paragraphs(url):
    def __getdata(url):
        r = requests.get(url)
        return r.text

    htmldata = __getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')
    return [data.get_text() for data in soup.find_all("p")]