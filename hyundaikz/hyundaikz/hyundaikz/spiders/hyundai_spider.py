import scrapy
from scrapy import Request
from scrapy import Selector
from scrapy.exceptions import CloseSpider
from datetime import date



class HyundaiSpiderSpider(scrapy.Spider):
    name = "hyundai"
    start_urls = ["https://hyundai-astana.kz/cars/"]

    def parse(self, response):
        for car in response.css(".carItem"):
            yield {
                "name": car.css(".carName::text").get(),
                "price": car.css(".carPrice::text").get(),
                "url": car.css("a::attr(href)").get(),
                "parseDate": date.today(),

            }

