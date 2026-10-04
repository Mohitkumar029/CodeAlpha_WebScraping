# CodeAlpha Task 1: Web Scraping

## About the project
I scraped book data from books.toscrape.com, a practice website made for learning web scraping.

## What I collected
Title, Price, Rating and Availability of 1,000 books from 50 pages.

## Tools used
Python, requests, BeautifulSoup, pandas

## Files
- scrape.py : collects the data from the website
- clean.py : cleans the data (price and rating converted to numbers)
- books_raw.csv : original scraped data
- books_clean.csv : cleaned data used in Task 2 and Task 3

## How to run
1. pip install requests beautifulsoup4 pandas
2. python scrape.py
3. python clean.py

## Author
Mohit