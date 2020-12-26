import scrapy 
from scrapy_splash import SplashRequest
from scrapy.loader import ItemLoader
from shopee.items import ShopeeItem

class ShopeeScrape(scrapy.Spider):
    name = "shopee"

    script = '''
       function main(splash)
            local num_scrolls = 10
            local scroll_delay = 1

            local scroll_to = splash:jsfunc("window.scrollTo")
            local get_body_height = splash:jsfunc(
                "function() {return document.body.scrollHeight;}"
            )
            assert(splash:go(splash.args.url))
            splash:wait(splash.args.wait)

            for _ = 1, num_scrolls do
                local height = get_body_height()
                for i = 1, 10 do
                    scroll_to(0, height * i/10)
                    splash:wait(scroll_delay/10)
                end
            end
            return {
                html = splash:html(),
            }
        end
    '''

    def start_requests(self):
        url = "https://shopee.ph/search?keyword=shoes"
        yield SplashRequest(url=url, callback=self.parse, endpoint='execute', args={'wait': 2, 'lua_source': self.script})

    def parse(self, response):
        for product in response.selector.xpath("//div[contains(@class,'_1gkBDw _2O43P5')]"):
            loader = ItemLoader(item=ShopeeItem(), selector=product, response=response)

            loader.add_xpath('prod_name', ".//child::div[contains(@class,'_1NoI8_')]")

            if len(product.xpath(".//child::div[@class='_2lBkmX']").extract()) > 1:
                loader.add_xpath('price', ".//child::div[@class='_2lBkmX']/div[2]/span[2]")
            else:
                loader.add_xpath('price', ".//child::div[@class='_2lBkmX']/div[1]")

            yield loader.load_item()