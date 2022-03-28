# Recursive-Scroll-Scraper

Python library for automating scrolling and downloading web pages via Selenium. Scrolling and downloading functionality
is provided by the [tq-scroll-scrape](https://pypi.org/project/tq-scroll-scrape/) package.

Recursive-Scroll-Scraper provides the ability to download a paginated site, i.e. starting at the root page, getting the
next page url, downloading that page, and so on until the end is reached.

`sample_app.py` demonstrates this use case using the Trulia real estate listings site.

## Usage

## Using ChromeDriver

Download ChromeDriver from https://chromedriver.chromium.org/downloads. Choose the version that matches the Chrome
browser running on your system.

## Using GeckoDriver for Firefox

Download GeckoDriver for Firefox from https://github.com/mozilla/geckodriver/releases.

### Install Package

Install the package by running `pip install tq-recursive-scroll-scrape`.

### Use the Package

Here is sample code demonstrating how to crawl a paginated site.

#### Create the RecursiveScrollScrape instance

```python
from tq_recursive_scroll_scrape.recursive_scroll_and_scrape import RecursiveScrollScrape

root_url = "https://www.trulia.com"
first_url = f"{root_url}/WA/Renton"
driver_path = "PATH TO DRIVER EXECUTABLE"
scroll_scraper = RecursiveScrollScrape(driver_path)
```

#### Define the Logic to Get the Next Page Links

Provide a callback containing the logic to get the next page links. Since this function is called recursively, be sure
to provide a terminating condition to avoid infinite loops.

```python
from bs4 import BeautifulSoup
from typing import Optional


def get_next_url(content: str) -> Optional[str]:
    soup = BeautifulSoup(content, "html.parser")

    links = [a for a in soup.find_all("a")
             if a.get("aria-label")
             and "Next" in a.get("aria-label")]

    # Terminates recursion if the last page is reached.
    if len(links) == 0:
        return None

    next_url = f"{root_url}{links[0].get('href')}"
    return next_url
```

#### Optional Post-Download Callback

Provide an optional callback containing the logic to perform after each page download such as saving the content to
disk.

```python
def on_after_download(content: str):
    with open("some_file.html", "w", encoding="utf-8") as file:
        file.write(content)
```

#### Start the Download

```python
scroll_scraper.download(first_url, on_after_download, get_next_url)
```

### Scroll and Download Options

Refer to the [tq-scroll-scrape](https://pypi.org/project/tq-scroll-scrape/) documentation for details on controlling
scroll and download options. For example, the default wait time between scrolls is two seconds but can be changed. By
default, the entire page is scrolled at once but can be scrolled by a specific number of pixels if desired.