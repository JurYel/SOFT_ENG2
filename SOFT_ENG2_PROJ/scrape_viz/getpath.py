import os
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings   
import importlib.util

print(os.getcwd())

if os.getcwd().find('SOFT_ENG2') != -1:
    file_path = os.path.join(os.getcwd(), 'scraper/forecast_scraper/spiders/forecast.py')
    os.chdir(file_path)
    print(True)
    print(os.getcwd())
else:
    file_path = os.path.join(os.getcwd(), "SOFT_ENG2\scraper\\forecast_scrape\\forecast_scrape\spiders\\")
    os.chdir(file_path)
    print(False)
    print(os.getcwd())
    spec = importlib.util.spec_from_file_location("forecast.py",os.path.join(file_path,'forecast.py'))
    forecast = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(forecast)

    crawler_settings = get_project_settings()
    crawler = CrawlerRunner(crawler_settings)
    crawler.crawl(forecast)
    

    