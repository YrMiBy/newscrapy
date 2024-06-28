import scrapy


class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["https://holodilnik.ru"]
    start_urls = ["https://www.holodilnik.ru/search/?search_provider=anyquery&strategy=advanced,zero_queries&search=светильник"]

    def parse(self, response):


