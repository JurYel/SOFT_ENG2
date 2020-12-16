# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags
import re

def shopee_ratings(value):
    value = remove_tags(value)
    value = value.replace(' sold','')

    if value.find('K') != -1:
        value = int(value.replace('K',''))
        value = value * 1000
    else:
        value = value

    return value

class LazadaItem(scrapy.Item):
    prod_name = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst()
    )
    price = scrapy.Field(
        input_processor = MapCompose(lambda val: float(remove_tags(val))),
        output_processor = TakeFirst()
    )
    ratings = scrapy.Field(
        input_processor = MapCompose(lambda val: int(remove_tags(val).replace('(','').replace(')',''))),
        output_processor = TakeFirst()
    )

class ShopeeItem(scrapy.Item):
    prod_name = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst()
    )
    price = scrapy.Field(
        input_processor = MapCompose(lambda val: int(remove_tags(val))),
        output_processor = TakeFirst()
    )
    ratings = scrapy.Field(
        input_processor = MapCompose(shopee_ratings),
        output_processor = TakeFirst()
    )
