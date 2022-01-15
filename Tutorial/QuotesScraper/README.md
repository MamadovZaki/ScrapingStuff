# QuotesScraper #

A web scraper to scrape quotes from this website [Quotes to Scrape](http://quotes.toscrape.com/)

## Tasks ##

1. Create a new Scrapy Project:
```
scrapy startproject QuotesScraper
```

2. Write a spider to crawl a site and extract data
  - Save your spiders in ```spider/``` directory.
  - Save each spider in a seperate class, and in a seperate files

## How to Run the spider ##

Use this command to put the spider to work, go to the project’s top level directory and run::
```
scrapy crawl quotes
```

3. Export the scraped data using the command line
  - The simplest way to store the scraped data is by using [Feed exports](https://docs.scrapy.org/en/latest/topics/feed-exports.html#topics-feed-exports), with the following command:
```
scrapy crawl quotes -O quotes.json
```
