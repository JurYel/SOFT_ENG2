import scrapy 
from lazada.items import LazadaItem
from scrapy.loader import ItemLoader
from .config import API_KEY

class LazadaScrape(scrapy.Spider):
    name = "lazada"
    # Next Page: li[title='Next Page'] a.ant-pagination-item-link
    def start_requests(self):
       url = "https://www.lazada.com.ph/catalog/?q=shoes"
       start_url = 'http://api.scraperapi.com/?api_key='+ API_KEY + '&url='+ url + '&render=true'
       yield scrapy.Request(url=start_url,callback=self.parse)


    def parse(self,response):
        if response.selector.xpath("//div[@class='ant-col-20 ant-col-push-4 c1z9Ut']") is not None:
            for product in response.selector.xpath("//div[@class='c2prKC']"):
                loader = ItemLoader(item=LazadaItem(), selector=product, response=response)

                loader.add_xpath('prod_name', ".//div[@class='c16H9d']/a")
                loader.add_xpath('price', ".//div[@class='c3gUW0']/span")

                yield loader.load_item()
