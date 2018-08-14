# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LgspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    title = scrapy.Field()     # 职位
    position = scrapy.Field()  # 工作地点
    salary = scrapy.Field()    # 最低薪资
    company = scrapy.Field()   # 公司名称
    time = scrapy.Field()      # 信息发布时间
    grade = scrapy.Field()     # 学历要求
