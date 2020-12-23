# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags
import re


class ShopeeItem(scrapy.Item):
    prod_name = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst()
    )
    price = scrapy.Field(
        input_processor = MapCompose(lambda val: 
            float(re.search(r'[0-9]{1,6}', remove_tags(val)).group(0))),
        output_processor = TakeFirst()
    )
