# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class QuotesSpiderItem(scrapy.Item):
    message = scrapy.Field()
    author = scrapy.Field()
    born = scrapy.Field()
    author_description = scrapy.Field()
    url = scrapy.Field()
    tags = scrapy.Field()
    tags_url = scrapy.Field()
   