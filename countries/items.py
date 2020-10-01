# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CountriesItem(scrapy.Item):
    book_title = scrapy.Field()
    link_to_download = scrapy.Field()

