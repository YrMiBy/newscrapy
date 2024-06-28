import scrapy

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/search?ProductSearch%5Bname%5D=светильники&categories%5B%5D=2246"]

    def parse(self, response):
        svets = response.css('div._Ud0k')
        for svet in svets:
            yield {
                'name': svet.css('div.lsooF span::text').get(), # название
                'price': svet.css('div.pY3d2 span::text').get() ,  # цена
                'url': svet.css('a').attrib['href']  # ссылка
            }
