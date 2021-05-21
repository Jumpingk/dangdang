# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    goods_link = scrapy.Field()
    shop_link = scrapy.Field()
    comment_count = scrapy.Field()
    price = scrapy.Field()
    shop_name = scrapy.Field()


    
