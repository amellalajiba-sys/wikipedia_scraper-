import re
import requests
from bs4 import BeautifulSoup


class WikipediaScraper:
    def __init__(self):
        #We keep one session open for all wikipedia requests so it is faster than fresh requests each time.
        self.session = requests.Session()
        self.headers = {"User-Agent": "Mozilla/5.0"}#Wikipedia wants a user-agent or it may block the request.

    def fetch_html(self, url):
        #This only download the html of one wikipedia page.
        response = self.session.get(url, headers=self.headers)
        return response.text

    def get_first_paragraph(self, html):
        #BeautifulSoup parse the raw html so we can search inside it more easily.
        soup = BeautifulSoup(html, "html.parser")
        paragraphs = soup.find_all("p")#Wikipedia text is usually inside p tags.

        first_paragraph = ""
        for paragraph in paragraphs:
            if paragraph.find("b"):#Usually the first real intro paragraph has the name in bold.
                first_paragraph = paragraph.text
                break

        return first_paragraph

    def clean_text(self, text):
        #We clean the usual wikipedia noise with a few regex.
        text = re.sub(r"\[[^\]]*\]", "", text)
        text = re.sub(r"Écouter\s*ⓘ", "", text)
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"\s+([,.;:])", r"\1", text)
        return text.strip()

    def scrape_first_paragraph(self, url):
        #This is the full shortcut: fetch the page, get the first paragraph, clean it, return it.
        html = self.fetch_html(url)
        paragraph = self.get_first_paragraph(html)
        return self.clean_text(paragraph)
