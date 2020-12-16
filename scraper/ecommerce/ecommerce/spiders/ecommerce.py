import scrapy 
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ecommerce.items import ZaloraItem
import re

class ZaloraScrape(scrapy.Spider):
    name = "zalora"
    
    def start_requests(self):
        url = "https://www.zalora.com.ph/_c/v1/desktop/list_catalog_full?url=%2F\
        shoes&sort=popularity&dir=desc&offset=0&limit=48&category_id=120&special_price=false&\
        all_products=false&new_products=false&top_sellers=false&catalogtype=Main&lang=en&\
        is_brunei=false&sort_formula=sum(product(0.2%2Cscore_simple_availability)\
        %2Cproduct(0.0%2Cscore_novelty)%2Cproduct(0.8%2Cscore_product_boost)\
        %2Cproduct(0.0%2Cscore_random)%2Cproduct(1.0%2Cscore_personalization))\
        &search_suggest=false&enable_visual_sort=true&enable_filter_ads=true\
        &compact_catalog_desktop=false&name_search=false&solr7_support=true\
        &pick_for_you=false&learn_to_sort_catalog=false&user_query=shoes\
        &is_multiple_source=true"
        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        for product in response.selector.xpath("//div[@class='c2prKC']"):
            loader = ItemLoader(item=ZaloraItem(),selector=product,response=response)

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