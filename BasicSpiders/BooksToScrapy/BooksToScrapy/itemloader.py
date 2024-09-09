from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst

class BookItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    img_url_in = MapCompose(lambda x : x)
    title_in = MapCompose(lambda x: x)
    info_url = MapCompose(lambda x: x)
    price_url = MapCompose(lambda x: x)
    stock_in = MapCompose(lambda x: x)
    quantity_in = MapCompose(lambda x: x)
    rating_in = MapCompose(lambda x: x.replace("star-rating ", ""))
    desc_in = MapCompose(lambda x: str.lower(x))
    reviews_in = MapCompose(lambda x: x)
    availability_in = MapCompose(lambda x:x)
    tax_in = MapCompose(lambda x:x)
    UPC_in = MapCompose(lambda x:x)