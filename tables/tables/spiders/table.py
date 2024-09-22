import scrapy


class TableSpider(scrapy.Spider):
    name = "table"
    allowed_domains = ["wikipedia.com"]
    start_urls = ["https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population"]

    def parse(self, response):
        table  = response.xpath(".//table")
        trs = table.xpath(".//tr")[1:]
        for tr in trs:
            rank = tr.xpath(".//td[1]//text()").getall()
            rk = ''.join([t.strip() for t in rank]).strip()
            city = tr.xpath(".//td[3]/a/text()").get()
            population = tr.xpath(".//td[4]/text()").get()
            yield {
                'rank': rk,
                'city': city,
                'population': population
            }