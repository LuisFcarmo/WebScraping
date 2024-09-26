import scrapy
from ..items import MercadolivreItem
import logging
class OfertasSpider(scrapy.Spider):
    name = "ofertas"
    allowed_domains = ["mercadolivre.com.br"]
    start_urls = ["https://www.mercadolivre.com.br/ofertas#nav-header"]

    def parse(self, response):
        produtos = response.xpath(".//div[@class = 'andes-card poly-card poly-card--grid-card andes-card--flat andes-card--padding-0 andes-card--animated']")
        for prod in produtos:
            item = MercadolivreItem()
            item["url_image_prod"] = prod.xpath(".//div[@class = 'poly-card__portada']/img/@data-src").get()
            item["title_prod"] = prod.xpath(".//div[@class = 'poly-card__content']/a[@class = 'poly-component__title']/text()").get()
            item["seller_prod"] = prod.xpath(".//div[@class = 'poly-card__content']/span[@class = 'poly-component__seller']/text()").get()
            item["high_light_prod"] = prod.xpath(".//div[@class = 'poly-card__content']/span[@class = 'poly-component__highlight']/text()").get()
            item["price_prod"] = prod.xpath(".//div[@class = 'poly-card__content']/div[@class = 'poly-component__price']").css(".andes-money-amount__fraction::text").get()
            item["price_cents_prod"] = prod.xpath(".//div[@class = 'poly-price__current']").css(".andes-money-amount__cents::text").get()
            item["price_symbol"] = prod.xpath(".//div[@class = 'poly-price__current']").css(".andes-money-amount__currency-symbol::text").get()

            yield item
        next_page = response.xpath(".//a[@title  = 'Siguiente']/@href").get()
        if(next_page is not None):
            logging.info(f'Iniciando o scraping para a URL: {next_page}')
            yield response.follow(next_page, callback = self.parse)
