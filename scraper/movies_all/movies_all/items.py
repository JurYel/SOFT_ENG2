# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, Join, TakeFirst
from w3lib.html import remove_tags
import re

class MovieItem(scrapy.Item):
    title = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst()
    )
    year = scrapy.Field(
        input_processor = MapCompose(lambda val: int(re.search(r'[0-9]{4}',
                                        remove_tags(val)).group(0))),
        output_processor = TakeFirst()
    )
    ratings = scrapy.Field(
        input_processor = MapCompose(lambda val: float(remove_tags(val))),
        output_processor = TakeFirst()
    )
    metascore = scrapy.Field(
        input_processor = MapCompose(lambda val: int(remove_tags(val))),
        output_processor = TakeFirst()
    )
    votes= scrapy.Field(
        input_processor = MapCompose(lambda val: int(val)),
        output_processor = TakeFirst()
    )
    gross_income = scrapy.Field(
        input_processor = MapCompose(lambda val: float(val.replace(',',''))),
        output_processor = TakeFirst()
    )

