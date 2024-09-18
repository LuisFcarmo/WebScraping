import scrapy
from craignlist.items import CraignlistItem
from scrapy.loader import ItemLoader

class CraignSpiderSpider(scrapy.Spider):
    name = "craign_spider"
    allowed_domains = ["newyork.craigslist.org"]
    start_urls = ["https://newyork.craigslist.org/search/egr"]
    
    def parse(self, response):
        jobs = response.xpath(".//a")
        for job in jobs:
            jb = ItemLoader(item = CraignlistItem(), selector = job)         
            jb.add_xpath("job_url", ".//@href")
            jb.add_xpath("title", ".//div[@class = 'title']/text()")
            jb.add_xpath("location", ".//div[@class = 'location']/text()")
            yield jb.load_item()