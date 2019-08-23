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
    
class StandingsItem(scrapy.Item):
    divisions = scrapy.Field()
    team_one_name = scrapy.Field()
    team_one_wins = scrapy.Field()
    team_one_loses = scrapy.Field()
    team_one_ties = scrapy.Field()
    team_one_percentage = scrapy.Field()
    team_one_points_for = scrapy.Field()
    team_one_points_against = scrapy.Field()
    team_one_division_record = scrapy.Field()
    team_one_streak = scrapy.Field()
    team_two_name = scrapy.Field()
    team_two_wins = scrapy.Field()
    team_two_loses = scrapy.Field()
    team_two_ties = scrapy.Field()
    team_two_percentage = scrapy.Field()
    team_two_points_for = scrapy.Field()
    team_two_points_against = scrapy.Field()
    team_two_division_record = scrapy.Field()
    team_two_streak = scrapy.Field()
    team_three_name = scrapy.Field()
    team_three_wins = scrapy.Field()
    team_three_loses = scrapy.Field()
    team_three_ties = scrapy.Field()
    team_three_percentage = scrapy.Field()
    team_three_points_for = scrapy.Field()
    team_three_points_against = scrapy.Field()
    team_three_division_record = scrapy.Field()
    team_three_streak = scrapy.Field()
    team_four_name = scrapy.Field()
    team_four_wins = scrapy.Field()
    team_four_loses = scrapy.Field()
    team_four_ties = scrapy.Field()
    team_four_percentage = scrapy.Field()
    team_four_points_for = scrapy.Field()
    team_four_points_against = scrapy.Field()
    team_four_division_record = scrapy.Field()
    team_four_streak = scrapy.Field()


    
    
