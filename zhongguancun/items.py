# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhongguancunItem(scrapy.Item):
    """定义要存储的字段"""

    # define the fields for your item here like:
    # name = scrapy.Field()

    # 手机名
    photoName = scrapy.Field()
    # 副标题
    subhead = scrapy.Field()
    # 手机参考价格
    originalPrice = scrapy.Field()
    # 手机商家报价
    shopPrice = scrapy.Field()
    # 手机主图
    mainPhoto = scrapy.Field()
    # 手机小图
    photo = scrapy.Field()
    # 规格名称
    baseConfiguration = scrapy.Field()
    # 手机类型
    phoneType = scrapy.Field()
    # 评论
    comment = scrapy.Field()
