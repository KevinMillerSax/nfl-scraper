# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NflItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
     name = scrapy.Field()
     team = scrapy.Field()
     number = scrapy.Field()
     position = scrapy.Field()
     height = scrapy.Field()
     weight = scrapy.Field()
     age = scrapy.Field()
     college = scrapy.Field()
     

# class ScheduleItem(scrapy.Item):
#     team = scrapy.Field()
#     away_team = scrapy.Field()
#     date = scrapy.Field()
#     result = scrapy.Field()
   
class SchedItem(scrapy.Item):
    away_team = scrapy.Field()
    away_team_record = scrapy.Field()
    away_team_score = scrapy.Field()
    home_team = scrapy.Field()
    home_team_record = scrapy.Field()
    home_team_score = scrapy.Field()
    week = scrapy.Field()
    
   

    
    
