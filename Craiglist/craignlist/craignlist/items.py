# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CraignlistItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()
    job_url = scrapy.Field()