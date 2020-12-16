from scrapy.spiders import CrawlSpider, Rule
import scrapy
from scrapy.linkextractors import LinkExtractor

class ShopeeScrape(CrawlSpider):
    name = "test"
    allowed_domains = ['shopee.ph']
    start_urls = ['https://shopee.ph/search?keyword=shoes']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[contains(@data-sqe,'link')]"),callback='parse_item',follow=True),
    )

    def parse_item(self,response):
        print(response.xpath("//div[@class='qaNIZv']/span/text()").extract_first())