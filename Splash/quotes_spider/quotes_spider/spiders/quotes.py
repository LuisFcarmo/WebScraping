import scrapy
from scrapy_splash import SplashRequest
import os
import glob
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/js"]
    def __init__(self, category):...
        ##é possivel sim passar argumentos para a spider bem parecido com arg and agc da linguagem c
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(
                url=url,
                callback=self.parse,
                endpoint='render.html',
                args={'wait': 2, 'images': 1}
            )

    def parse(self, response):
        self.logger.info('Response URL: %s', response.url)
        # Log the response status
        self.logger.info('Response status: %s', response.status)
        # Print a snippet of the response body to verify it's working
        self.logger.info('Response body snippet: %s', response.body[:500])
        quotes = response.css('div.quote')
        for quote in quotes:
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
        #script para acessar a proxima página
        script = """
                function main(splash)
                assert(splash:go(splash.args.url))
                splash:wait(0.3)
                button = splash:select("li[class=next] a")
                splash:set_viewport_full()
                splash:wait(0.1)
                button:mouse_click()
                splash:wait(1)
                return {url = splash:url(),
                        html = splash:html()}
                end"""
        yield SplashRequest(url=response.url, callback = self.parse, endpoint='execute', args = {'lua_source':script})
        
    ##guardar os items em um arquivo diretamente sem precisar redirecionar
    def close(self, reason):
        csv_file = max(glob.iglob('*.csv'), key = os.path.getctime)
        os.rename(csv_file, 'foobar.csv')