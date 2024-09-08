import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]
   
    def parse(self, response):
        yield {
            "title": response.xpath("//h1/a/text()").get(),
            "tags": response.xpath("//*[@class='tag-item']/a/text()").extract()
        }
