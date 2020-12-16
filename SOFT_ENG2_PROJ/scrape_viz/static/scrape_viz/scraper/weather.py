from scrapy.crawler import CrawlerProcess
from ....scraper.forecast_scrape.spiders.forecast import ForecastScrape

def scrape_weather():
    process = CrawlerProcess()
    process.crawl(ForecastScrape)
    process.start()