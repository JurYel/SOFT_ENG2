# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags
import re

def get_night_humidity(value):
    value = remove_tags(value)
    value = re.search(r'[0-9]{2}',value).group(0)  

    if float(value) < 80:
        return float(value)

def get_day_humidity(value):
    value = remove_tags(value)
    value = re.search(r'[0-9]{2}',value).group(0)

    if float(value) > 80:
        return float(value)

class ForecastScrapeItem(scrapy.Item):
    night_period = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst()
    )
    day_period = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst()
    )
    night_temp = scrapy.Field(
        input_processor = MapCompose(lambda val: float(re.search(r'[0-9]{2}',remove_tags(val)).group(0))),
        output_processor = TakeFirst()
    )
    day_temp = scrapy.Field(
        input_processor = MapCompose(lambda val: float(re.search(r'[0-9]{2}',remove_tags(val)).group(0))),
        output_processor = TakeFirst()
    )
    night_humidity = scrapy.Field(
        input_processor = MapCompose(get_night_humidity),
        output_processor = TakeFirst()
    )

    day_humidity = scrapy.Field(
        input_processor = MapCompose(get_day_humidity),
        output_processor = TakeFirst()
    )
