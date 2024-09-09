import scrapy
from quotes_spider.items import QuotesSpiderItem
from quotes_spider.itemloader import QuotesItemLoader
from urllib.parse import urljoin

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        quotes = response.xpath("//*[@class='quote']")
        for quote in quotes:
            quoteLoader = QuotesItemLoader(item=QuotesSpiderItem(), selector=quote)
            quoteLoader.add_xpath('message', './/span[@class="text"]/text()')
            quoteLoader.add_xpath('author', './/small[@class="author"]/text()')
            quoteLoader.add_xpath('url', './/a/@href')
            quoteLoader.add_xpath('tags', './/div[@class="tags"]/a/text()')
            quoteLoader.add_xpath('tags_url', './/div[@class="tags"]/a/@href')

            author_url = quoteLoader.get_output_value('url')
            if author_url:
                full_url = urljoin(response.url, author_url)
                #yield response.follow(full_url, self.parse_more_author, meta={"loader": quoteLoader})
            yield quoteLoader.load_item()
        next_page_url = response.xpath("//li[@class='next']/a/@href").get()
        if next_page_url:
            next_page_url = urljoin(response.url, next_page_url)
            yield response.follow(next_page_url, callback=self.parse)
    
    def parse_more_author(self, response):
        loader = response.meta.get("loader")
        if not loader:
            self.logger.error("Loader not found in meta data.")
            return
        
        author_description = response.xpath(".//div[@class='author-description']/text()").get(default='').strip()
        born_date = response.xpath(".//span[@class='author-born-date']/text()").get(default='').strip()
        
        loader.add_value("author_description", author_description)
        loader.add_value("born", born_date)
        
        yield loader.load_item()
