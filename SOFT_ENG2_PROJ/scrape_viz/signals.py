from django.dispatch import Signal, receiver
from scrapy.crawler import CrawlerProcess
from ....scraper.forecast_scrape.spiders.forecast import ForecastScrape

scrapy_signal = Signal()

@receiver(scrapy_signal) # sender = ?
def scrape_weather(sender, **kwargs):
    process = CrawlerProcess()
    process.crawl(ForecastScrape)
    process.start()
