from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst

base_url = "quotes.toscrape.com"

def process_tags(tags):
    processed_tags = [tag.strip().lower() for tag in tags]
    unique_tags = list(set(processed_tags))
    return unique_tags
def process_tags_url(tags_urls):
    unique_url_tags = list(set(tags_urls))
    return unique_url_tags

class QuotesItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    message_in = MapCompose(lambda x : x)
    author_in = MapCompose(lambda x : x)
    born_in = MapCompose(lambda x: x)
    author_description_in = MapCompose(lambda x: x)
    url_in = MapCompose(lambda x : x)
    tags_in = MapCompose(lambda x: x.strip())
    tags_out = process_tags
    tags_url_in = MapCompose(lambda x: base_url + x.strip())
    tags_url_out = process_tags_url
  