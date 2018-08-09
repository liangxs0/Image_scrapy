# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImageItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    '''            print(img)
        print(describe.extract())
        print(describe_data.extract())
        print(describe_dict)
        print(describe_Size_Inches_S.extract())
        print(describe_Size_Inches_M.extract())
        print(describe_Size_Inches_L.extract())
        print(describe_Size_Cen_S.extract())
        print(describe_Size_Cen_M.extract())
        print(describe_Size_Cen_L.extract())'''
    url = scrapy.Field()
    img = scrapy.Field()
    prices = scrapy.Field()
    describe_dict = scrapy.Field()
    describe_Size_Inches_S = scrapy.Field()
    describe_Size_Inches_M = scrapy.Field()
    describe_Size_Inches_L = scrapy.Field()
    describe_Size_Cen_S = scrapy.Field()
    describe_Size_Cen_M = scrapy.Field()
    describe_Size_Cen_L = scrapy.Field()

