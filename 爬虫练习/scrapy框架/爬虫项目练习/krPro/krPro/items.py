# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KrproItem(scrapy.Item):
    # define the fields for your item here like:
    detail_url = scrapy.Field()
    Title = scrapy.Field()
    img_url = scrapy.Field()

#class DetailItem(scrapy.Item):

    content = scrapy.Field()




