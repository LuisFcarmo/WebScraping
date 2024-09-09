# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookstoscrapyItem(scrapy.Item):
    img_url = scrapy.Field()
    title = scrapy.Field()
    info_url = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    quantity = scrapy.Field()
    rating = scrapy.Field()
    desc = scrapy.Field()
    reviews = scrapy.Field()
    availability = scrapy.Field()
    tax = scrapy.Field()
    UPC = scrapy.Field()
