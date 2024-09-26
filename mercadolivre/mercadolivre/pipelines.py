# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .items import MercadolivreItem

class MercadolivrePipeline:
    def process_item(self, item: MercadolivreItem , spider):
        if item['price_cents_prod'] == None:
            item['price_cents_prod'] = 0
        if item['high_light_prod'] == None:
            item['high_light_prod'] = 'Nenhum'
        if item['seller_prod'] == None:
            item['seller_prod'] = "Mercado Livre"
        return item