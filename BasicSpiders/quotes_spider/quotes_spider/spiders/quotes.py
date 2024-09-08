import scrapy
from quotes_spider.items import QuotesSpiderItem
from quotes_spider.itemloader import QuotesItemLoader

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]
   
    def parse(self, response):
        quotes = response.xpath("//*[@class = 'quote']")
        for quote in quotes:
            quoteLoader = QuotesItemLoader(item = QuotesSpiderItem(), selector = quote)
            quoteLoader.add_xpath('message', './/span[@class = "text"]/text()')
            quoteLoader.add_xpath('author', './/small[@class = "author"]/text()')
            quoteLoader.add_xpath('url', './/a/@href')
            quoteLoader.add_xpath('tags', './/div[@class = "tags"]/a/text()')
            quoteLoader.add_xpath('tags_url', './/div[@class = "tags"]/a/@href')

            yield response.follow(quoteLoader.get_output_value("url"), self.parse_more_author, meta = {"loader": quoteLoader})
    
    def parse_more_author(self, response):
        Loader: QuotesItemLoader = response.meta["loader"]
        value = response.xpath(".//div[@class = 'author-description']/text()").get()
        Loader.add_value("author_description", value)
        value = response.xpath("..//span[@class = 'author-born-date']/text()").get()
        Loader.add_value("born", value)
        
        yield Loader.load_item()