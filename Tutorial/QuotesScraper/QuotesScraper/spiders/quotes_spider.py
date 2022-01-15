import scrapy

class QuotesSpider(scrapy.Spider):
    """
    start_urls is a class attribute with a list of URLs

    start_urls list will then be used by the default implementation of start_requests() to create the initial requests for your spider
    """
    name = 'quotes'

    start_urls = [
    'http://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response):
        quotes = response.xpath("//div[@class='quote']")
        for quote in quotes:
            yield {
                'text' : quote.css('span.text::text').get(),
                'author' : quote.css('small.author::text').get(),
                'tags' : quote.css('div.tags a.tag::text').getall()
            }
        next_page =response.xpath("//li[@class='next']/a/@href").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
