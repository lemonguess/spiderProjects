# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImageproItem(scrapy.Item):
    # define the fields for your item here like:
    src = scrapy.Field()
    img_name= scrapy.Field()


