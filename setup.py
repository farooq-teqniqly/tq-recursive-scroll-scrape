"""
Setup module.
"""
from setuptools import setup, find_packages
import tq_recursive_scroll_scrape


def long_description():
    """
    Returns the text of the readme.
    :return: The text of the readme.
    """
    with open("README.md", encoding="utf-8") as file:
        return file.read()


setup(
    name="tq-recursive-scroll-scrape",
    version=tq_recursive_scroll_scrape.__version__,
    description=tq_recursive_scroll_scrape.__doc__.strip(),
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/farooq-teqniqly/tq-recursive-scroll-scrape",
    author=tq_recursive_scroll_scrape.__author__,
    author_email="farooq@teqniqly.com",
    license=tq_recursive_scroll_scrape.__license__,
    packages=find_packages(include=["tq_recursive_scroll_scrape", "tq_recursive_scroll_scrape.*"]),
    python_requires=">=3.9",
    install_requires=["tq-scroll-scrape"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Utilities"
    ],
    project_urls={
        "GitHub": "https://github.com/farooq-teqniqly/tq-recursive-scroll-scrape"
    }
)
