import scrapy
from ..items import ScrapytutItem
from scrapy.http import FormRequest

#to check if login is working or not
from scrapy.utils.response import open_in_browser

class QuotesSpider(scrapy.Spider):
    #name of tjhe spider
    name = "quote"
    #urls to scrape
    start_urls = [
        'https://quotes.toscrape.com/login'
    ]


    def parse(self, response, **kwargs):
        token = response.css("form input::attr(value)").extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': 'ayusman@gmail.com',
            'password': 'somegibberish'
        }, callback=self.start_scraping)



    def start_scraping(self, response):
        open_in_browser(response)
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