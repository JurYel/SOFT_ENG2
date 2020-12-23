# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags
import re 

def convertPrice(value):
    value = remove_tags(value)
    value = value.replace(',','')
    value = float(re.search(r'[0-9]{1,6}',value).group(0))
    return value 

class LazadaItem(scrapy.Item):
    prod_name = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst()
    )
    price = scrapy.Field(
        input_processor = MapCompose(convertPrice),
        output_processor = TakeFirst()
    )
