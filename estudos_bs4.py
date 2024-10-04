from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse, parse_qs, urlencode
from dataclasses import dataclass

"""
codigo realizado apenas para fins de aprender a usar bs4
url = "https://books.toscrape.com/"
#configurando o user agents/headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    response.encoding = 'utf-8'  
    soup = BeautifulSoup(response.text, "html.parser")  
    titles = soup.select("h3 a[title]")
    for title in titles:
        print(title.text)
    
    images = soup.find_all('div', class_='image_container')
    for image in images:
        print(image.a['href'])
    
else:
    print(f"Erro ao acessar a página: {response.status_code}")
"""
@dataclass
class produto:
    url_prod = ''
    text = ''
    vendedor = ''
    desconto = ''
    estoque = ''
    def __str__(self) -> str:
        return f"""
--------------------------------------------------------------------            
            url_prod = {self.url_prod}\n
            text = {self.text}\n 
            vendedor = {self.vendedor}\n
            desconto = {self.desconto}\n
            estoque = {self.estoque}
--------------------------------------------------------------------
        """
    
class MercadoScrapy:
    def req_page_ofertas(self, url_page_ofertas):
        return requests.get(url_page_ofertas, self.config_header())
    
    def req_page_detalhes_page(self, url_prod):
        return requests.get(url_prod, self.config_header())
    
    def config_header(self):
        headers = {
             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        }
        return headers

    def cleaned_url(self, url_suja):
        parsed_url = urlparse(url_suja)
        query_params = parse_qs(parsed_url.query)
        query_params.pop('User-Agent', None) 
        cleaned_query = urlencode(query_params, doseq=True)
        cleaned_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}?{cleaned_query}"
        return cleaned_url

    def Scrapy_Home_page(self, url_page):
        response = self.req_page_ofertas(url_page)
        pd = produto()
        if(response.status_code == 200):
            soup = BeautifulSoup(response.text,  'html.parser')
            produtos_div = soup.select('div.items-with-smart-groups div.poly-card__content')

            for prod in produtos_div:
                link_tag = prod.find('a')
                vendedor = prod.select_one('span.poly-component__seller')
                desconto = prod.select_one('div.poly-component__price div.poly-price__current span.andes-money-amount__discount')

                if(link_tag and vendedor and desconto):
                    pd.url_prod = link_tag['href']
                    pd.text = link_tag.text.strip()     
                    pd.vendedor = vendedor.text.strip()  
                    pd.desconto = desconto.text.strip()  
                if(pd.url_prod):
                    self.Scrapy_Detales_page(pd.url_prod, pd)
                
            
            
            pagination = soup.select_one("li.andes-pagination__button.andes-pagination__button--next")
            if "andes-pagination__button--disabled" in pagination['class']:
                return
            print(self.cleaned_url(pagination.a['href']))
            self.Scrapy_Home_page(self.cleaned_url(pagination.a['href']))

            
    def Scrapy_Detales_page(self, url_prod, pd):              
        response = self.req_page_detalhes_page(url_prod)

        if(response.status_code == 200):
            soup = BeautifulSoup(response.text, 'html.parser')
            card_prod = soup.select_one('form#buybox-form')            
            if(card_prod):
                estoque = card_prod.select_one("div.ui-pdp-stock-information")
                if(estoque):
                    pd.estoque = estoque.text
                    print(pd)
        
iniciar = MercadoScrapy()
iniciar.Scrapy_Home_page("https://www.mercadolivre.com.br/ofertas#nav-header")