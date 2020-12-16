import scrapy
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess
from forecast_scrape.items import ForecastScrapeItem
import re

class ForecastScrape(scrapy.Spider):
    name = "forecast_scrape"

    def start_requests(self):
        url = "https://weather.com/weather/tenday/l/2b3272877cc60e81ad25d6b1d2ed866d9ab1229f7d085d5a0cd62de1907c6ff1"
        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        for period in response.selector.xpath("//details[@class='Disclosure--themeList--uBa5q']"):
            loader = ItemLoader(item=ForecastScrapeItem(),selector=period,response=response)
            
            loader.add_xpath('night_period',".//h3[contains(text(),'Night')]//span")
            loader.add_xpath('day_period',".//h3[contains(text(),'Day')]//span")
            loader.add_xpath('night_temp',".//h3[contains(text(),'Night')]/parent::node()//span[contains(@class,'DailyContent--temp')]")
            loader.add_xpath('day_temp',".//h3[contains(text(),'Day')]/parent::node()//span[contains(@class,'DailyContent--temp')]")
            loader.add_xpath('night_humidity',".//h3[contains(text(),'Night')]/ancestor-or-self::node()//span[@class='DetailsTable--value--1F3Ze' and @data-testid='PercentageValue']")
            loader.add_xpath('day_humidity',".//h3[contains(text(),'Day')]/ancestor-or-self::node()//span[@class='DetailsTable--value--1F3Ze' and @data-testid='PercentageValue']")

            yield loader.load_item()