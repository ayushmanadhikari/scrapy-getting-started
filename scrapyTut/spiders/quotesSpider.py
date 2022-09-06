import scrapy
from ..items import ScrapytutItem


class QuotesSpider(scrapy.Spider):
    #name of tjhe spider
    name = "quote"
    #urls to scrape
    start_urls = [
        'https://quotes.toscrape.com/login'
    ]

    def parse(self, response, **kwargs):
        token = "uVTfURYFsrAqbKcGvayCNOMIdWheDxmXnESHigJtlpBwQLjzPZko"
        

