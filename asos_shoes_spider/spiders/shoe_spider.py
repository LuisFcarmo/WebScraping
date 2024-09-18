import scrapy
from scrapy.http import Request

class ShoeSpiderSpider(scrapy.Spider):
    name = "shoe_spider"
    allowed_domains = ["asos.com"]
    start_urls = ["https://www.asos.com/men/new-in/new-in-accessories/cat/?cid=27112"]

    def parse(self, response):
        products_urls = response.xpath(".//a[@class = 'productLink_KM4PI']/@href").getall()
        for url in products_urls:
            yield Request(url, callback=self.parse_product)
    
    def parse_product(self, response):
    
        name = response.xpath(".//h1[@class = 'jcdpl']//text()").get()
    