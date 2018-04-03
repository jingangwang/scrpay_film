# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrpayFilmItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    film_name = scrapy.Field()
    film_score = scrapy.Field()
    film_download_urls = scrapy.Field()

