from typing import Optional

from bs4 import BeautifulSoup
from tq.recursive_scroll_and_scrape import RecursiveScrollScrape
import sys


def main():
    root_url = "https://www.trulia.com"
    first_url = f"{root_url}/WA/Renton"

    scroll_scraper = RecursiveScrollScrape()

    def _on_after_download(content: str):
        print(f"on_after_download ==> content length ==> {len(content)}")

    def _get_next_url(content: str) -> Optional[str]:
        soup = BeautifulSoup(content, "html.parser")

        links = [a for a in soup.find_all("a") if a.get("aria-label") and "Next" in a.get("aria-label")]

        if len(links) == 0:
            return None

        next_url = f"{root_url}{links[0].get('href')}"
        print(f"_get_next_url ==> {next_url}")
        return next_url

    scroll_scraper.download(first_url, _on_after_download, _get_next_url)


if __name__ == "__main__":
    sys.exit(main())
