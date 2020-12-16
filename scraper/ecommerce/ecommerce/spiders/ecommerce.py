import scrapy 
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ecommerce.items import LazadaItem
import re

class LazadaScrape(CrawlSpider):
    name = "lazada"
    allowed_domains = ['lazada.com']
    start_urls = ['https://www.lazada.com.ph/catalog/?q=shoes']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='c2prKC']"), callback='parse_item', follow=True)
    )

    def parse(self,response):
        for product in response.selector.xpath("//div[@class='c2prKC']"):
            loader = ItemLoader(item=LazadaItem(),selector=product,response=response)

            loader.add_xpath('prod_name',".//div[@class='c16H9d']/a")
            loader.add_xpath('price',".//div[@class='c3gUW0']/span")
            loader.add_xpath('ratings',".//span[@class='c3XbGJ']")

            yield loader.load_item()

class ShopeeScrape(CrawlSpider):
    name = "shopee"
    allowed_domains = ['shopee.ph']
    start_urls = ['https://shopee.ph/search?keyword=shoes']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='c2prKC']"), callback='parse_item', follow=True)
    )

    def parse(self,response):
        for product in response.selector.xpath("//div[contains(@class,'_1gkBDw _2O43P5')]"):
            loader = ItemLoader(item=ShopeeItem(),selector=product,response=response)

            loader.add_xpath('prod_name',".//child::div[contains(@class,'_1NoI8_')]")
            
            if len(product.xpath(".//child::div[@class='_2lBkmX']").extract()) > 1:
                loader.add_xpath('price',".//child::div[@class='_2lBkmX']/div[2]/span[2]")
            else:
                loader.add_xpath('price',".//child::div[@class='_2lBkmX']/div[1]")
                
            loader.add_xpath('ratings',".//child::div[contains(@class,'_18SLBt')]")

            yield loader.load_item()