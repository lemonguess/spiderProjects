# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DistributedItem(scrapy.Item):
    lazyimg = scrapy.Field()
    title = scrapy.Field()
    resisted_data = scrapy.Field()
    mileage = scrapy.Field()
    city = scrapy.Field()
    price = scrapy.Field()
    detail = scrapy.Field()


class TaocheParamenterConfig(scrapy.Item):
    display = scrapy.Field()
    transmission = scrapy.Field()
