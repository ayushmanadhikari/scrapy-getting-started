import scrapy
from .items import ScrapytutItem


class QuotesSpider(scrapy.Spider):
    #name of tjhe spider
    name = "quote"
    #urls to scrape
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response, **kwargs):
        all_div_quotes = response.css("div.quote")
        items = ScrapytutItem()


        for quote in all_div_quotes:
            title = quote.css("span.text::text").extract()
            author = quote.css("small.author::text").extract()
            tags = quote.css(".tag::text").extract()

            items['title'] = title
            items['author'] = author
            items['tags'] = tags

            yield items
        

