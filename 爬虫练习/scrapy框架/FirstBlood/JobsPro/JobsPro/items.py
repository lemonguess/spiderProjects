# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsproItem(scrapy.Item):
    job = scrapy.Field()
    place = scrapy.Field()
    salary =scrapy.Field()
    year = scrapy.Field()
    c_name = scrapy.Field()

