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
> Use the name that you've set in the name attribute in the spider class, for instance, if you've set name = 'quotes' then use the command above to run the spider.

3. Export the scraped data using the command line
  - The simplest way to store the scraped data is by using [Feed exports](https://docs.scrapy.org/en/latest/topics/feed-exports.html#topics-feed-exports), with the following command:
```
scrapy crawl quotes -O quotes.json
```

4. Changing spider to recursively follow links
  - Locate where the next link is in the page
  - Use css or xpath selector to fetch it
  - add the next the page in the parse function

## Details about: ``` follow ```, ```follow_all``` ##

- As a shortcut for creating Request objects you can use ```response.follow```:
```python
next_page = response.css('li.next a::attr(href)').get()
       if next_page is not None:
           yield response.follow(next_page, callback=self.parse)
```
Unlike ```scrapy.Request```, ```response.follow``` supports relative URLs directly - no need to call ```urljoin```. Note that ```response.follow``` just returns a Request instance; you still have to ```yield``` this Request.

- You can also pass a selector to response.follow instead of a string; this selector should extract necessary attributes:
```python
for href in response.css('ul.pager a::attr(href)'):
    yield response.follow(href, callback=self.parse)
```

- For ```<a>``` elements there is a shortcut: ```response.follow``` uses their ```href``` attribute automatically. So the code can be shortened further:
```python
for a in response.css('ul.pager a'):
    yield response.follow(a, callback=self.parse)
```

- To create multiple requests from an iterable, you can use ```response.follow_all``` instead:
```python
anchors = response.css('ul.pager a')
yield from response.follow_all(anchors, callback=self.parse)
```
