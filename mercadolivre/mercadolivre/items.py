# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MercadolivreItem(scrapy.Item):
    url_image_prod = scrapy.Field()
    title_prod = scrapy.Field()
    seller_prod = scrapy.Field()
    high_light_prod = scrapy.Field()
    price_prod = scrapy.Field()
    price_cents_prod = scrapy.Field()
    price_symbol = scrapy.Field()
    
    pass
