import scrapy
from scrapy.http import FormRequest
#como fazer logins simples usando scrapy
class LoginSpider(scrapy.Spider):
    name = "login"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/login"]

    def parse(self, response):
        csrf_token = response.xpath('.//*[@name = "csrf_token"]/@value').get()
        #basicamente um form data normal do javascript para realizar login6
        yield FormRequest("https://quotes.toscrape.com/login",
                formdata = {
                    'csrf_token': csrf_token,
                    'username': 'foobar',
                    'password': 'foobar'},
                callback = self.parse_after_login)
        
    def parse_after_login(self, response):
        value = response.xpath(".//a[text() = 'Logout']").get()
        print(f"deu certo {value}")
        ...