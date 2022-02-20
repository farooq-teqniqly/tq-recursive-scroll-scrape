from functools import partial
from typing import Optional

from tq.recursive_scroll_and_scrape import RecursiveScrollAndScrape
from bs4 import BeautifulSoup

trulia_root_url = "https://www.trulia.com"
trulia_first_url = f"{trulia_root_url}/WA/Renton/"


def test_recursive_download():
    def on_after_download(content: str):
        print(f"on_after_download ==> Length={len(content)}")

    def get_next_url(root_url: str, content: str) -> Optional[str]:
        soup = BeautifulSoup(content, "html.parser")
        links = [a for a in soup.find_all("a") if a.get("aria-label") and "Next" in a.get("aria-label")]

        if len(links) == 0:
            return None

        next_url = f"{root_url}{links[0].get('href')}"
        print(f"get_next_url() ==> {next_url}")
        return next_url

    scroll_scraper = RecursiveScrollAndScrape()

    scroll_scraper.download(
        trulia_first_url,
        on_after_download,
        partial(get_next_url, trulia_root_url))
