import scrapy
from BooksToScrapy.items import BookstoscrapyItem
from BooksToScrapy.itemloader import BookItemLoader
from urllib.parse import urljoin

class BookspiderSpider(scrapy.Spider):
    name = "BookSpider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com"]


    def parse(self, response):
        books_containers = response.xpath(".//div/ol[@class = 'row']/li")

        for book in books_containers:
            BookLoader = BookItemLoader(item = BookstoscrapyItem(), selector = book)
            BookLoader.add_xpath("img_url", ".//div[@class = 'image_container']/a/@href")
            BookLoader.add_xpath("title", ".//h3/a/@title")
            BookLoader.add_xpath("info_url", ".//h3/a/@href")
            BookLoader.add_xpath("price", ".//p[@class = 'price_color']/text()")
            BookLoader.add_xpath("stock", ".//p[@class = 'instock availability']")
            BookLoader.add_xpath("rating", ".//p[contains(@class, 'star-rating')]/@class")
                
            url_in_book_page = urljoin(self.start_urls[0], BookLoader.get_output_value("info_url"))
            print(f"url que vou buscar {url_in_book_page}")
            if(url_in_book_page is not None):
                yield response.follow(url_in_book_page, self.parse_in_book_info, meta = {"loader": BookLoader})

    def parse_in_book_info(self, response):
        loader:BookItemLoader = response.meta["loader"]
        value = response.xpath(".//div[@id='product_description']/following-sibling::p/text()").get()
        loader.add_value("desc",value)
        value = response.xpath(".//th[text() = 'Number of reviews']/following-sibling::td/text()").get()
        loader.add_value("reviews", value)
        value = response.xpath(".//th[text() = 'Availability']/following-sibling::td/text()").get()
        loader.add_value("availability", value)
        value = response.xpath(".//th[text() = 'Tax']/following-sibling::td/text()").get()
        loader.add_value("tax", value)
        value = response.xpath(".//th[text() = 'UPC']/following-sibling::td/text()").get()
        loader.add_value("UPC", value)
        yield loader.load_item()