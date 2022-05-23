# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BossproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job = scrapy.Field()
    place = scrapy.Field()
    salary = scrapy.Field()
    year = scrapy.Field()
    c_name = scrapy.Field()
    fuli = scrapy.Field()


class BossproItem2(scrapy.Item):
    zhiweimiaoshu = scrapy.Field()
