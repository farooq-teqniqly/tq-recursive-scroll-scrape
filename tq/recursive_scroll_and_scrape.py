from functools import partial
from typing import Callable, Optional

from teqniqly.scroll_and_scrape import ScrollAndScrape


class RecursiveScrollScrape:
    def __init__(self):
        self.scroll_scraper = ScrollAndScrape()

    def download(
            self,
            url: str,
            on_after_download: Optional[Callable[[str], None]],
            get_next_url: Callable[[str], Optional[str]]):
        self.scroll_scraper.download(
            url,
            partial(self._download_recursive, on_after_download, get_next_url))

    def _download_recursive(
            self,
            on_after_download: Optional[Callable[[str], None]],
            get_next_url: Callable[[str], Optional[str]],
            content: str):
        on_after_download(content)
        next_url = get_next_url(content)

        if next_url is None:
            return

        self.scroll_scraper.driver.close()
        self.scroll_scraper.driver.quit()

        self.scroll_scraper.download(
            next_url,
            partial(self._download_recursive, on_after_download, get_next_url))
