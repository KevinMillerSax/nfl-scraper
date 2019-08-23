# all entries have 8 rows which all correspond to place in division

import scrapy
from ..items import StandingsItem

class StandingsSpider(scrapy.Spider):
  name = "standings"
  start_urls = [
    'https://www.foxsports.com/nfl/standings'
  ]

  def parse(self, response):
    items = StandingsItem()
  
    divisions = response.css(".sorter-false").css("::text").extract()
    team_one_name = response.css(".wisbb_fvStand:nth-child(1) span:first-of-type").css("*::text").extract() 
    team_one_wins = response.css(".wisbb_fvStand:nth-child(1) .wisbb_fixedColumn+ .wisbb_priorityColumn").css("::text").extract() 
    team_one_loses = response.css(".wisbb_fvStand:nth-child(1) .wisbb_priorityColumn:nth-child(3)").css("::text").extract()
    team_one_ties = response.css(".wisbb_fvStand:nth-child(1) .wisbb_priorityColumn:nth-child(4)").css("::text").extract() 
    team_one_percentage = response.css(".wisbb_fvStand:nth-child(1) .wisbb_priorityColumn:nth-child(5)").css("::text").extract()
    team_one_points_for = response.css(".wisbb_fvStand:nth-child(1) td:nth-child(6)").css("::text").extract() 
    team_one_points_against = response.css(".wisbb_fvStand:nth-child(1) td:nth-child(7)").css("::text").extract()
    team_one_division_record = response.css(".wisbb_fvStand:nth-child(1) td:nth-child(11)").css("::text").extract() 
    team_one_streak = response.css(".wisbb_fvStand:nth-child(1) td:nth-child(12)").css("::text").extract()
    team_two_name = response.css(".wisbb_fvStand:nth-child(2) span:first-of-type").css("*::text").extract()
    team_two_wins = response.css(".wisbb_fvStand:nth-child(2) .wisbb_text+ .wisbb_priorityColumn").css("::text").extract()
    team_two_loses = response.css(".wisbb_fvStand:nth-child(2) td:nth-child(3)").css("::text").extract()
    team_two_ties = response.css(".wisbb_fvStand:nth-child(2) td:nth-child(4)").css("::text").extract()  
    team_two_percentage = response.css(".wisbb_fvStand:nth-child(2) td:nth-child(5)").css("::text").extract()
    team_two_points_for = response.css(".wisbb_fvStand:nth-child(2) td:nth-child(6)").css("::text").extract()
    team_two_points_against = response.css(".wisbb_fvStand:nth-child(2) td:nth-child(7)").css("::text").extract()
    team_two_division_record = response.css(".wisbb_fvStand:nth-child(2) td:nth-child(11)").css("::text").extract() 
    team_two_streak = response.css(".wisbb_fvStand:nth-child(2) td:nth-child(12)").css("::text").extract()
    team_three_name = response.css(".wisbb_fvStand:nth-child(3) span:first-of-type").css("*::text").extract()
    team_three_wins = response.css(".wisbb_fvStand:nth-child(3) .wisbb_text+ .wisbb_priorityColumn").css("::text").extract()
    team_three_loses = response.css(".wisbb_fvStand:nth-child(3) td:nth-child(3)").css("::text").extract()
    team_three_ties = response.css(".wisbb_fvStand:nth-child(3) td:nth-child(4)").css("::text").extract()  
    team_three_percentage = response.css(".wisbb_fvStand:nth-child(3) td:nth-child(5)").css("::text").extract()
    team_three_points_for = response.css(".wisbb_fvStand:nth-child(3) td:nth-child(6)").css("::text").extract()
    team_three_points_against = response.css(".wisbb_fvStand:nth-child(3) td:nth-child(7)").css("::text").extract()
    team_three_division_record = response.css(".wisbb_fvStand:nth-child(3) td:nth-child(11)").css("::text").extract() 
    team_three_streak = response.css(".wisbb_fvStand:nth-child(3) td:nth-child(12)").css("::text").extract()
    team_four_name = response.css(".wisbb_fvStand:nth-child(4) span:first-of-type").css("*::text").extract()
    team_four_wins = response.css(".wisbb_fvStand:nth-child(4) .wisbb_text+ .wisbb_priorityColumn").css("::text").extract()
    team_four_loses = response.css(".wisbb_fvStand:nth-child(4) td:nth-child(3)").css("::text").extract()
    team_four_ties = response.css(".wisbb_fvStand:nth-child(4) td:nth-child(4)").css("::text").extract()  
    team_four_percentage = response.css(".wisbb_fvStand:nth-child(4) td:nth-child(5)").css("::text").extract()
    team_four_points_for = response.css(".wisbb_fvStand:nth-child(4) td:nth-child(6)").css("::text").extract()
    team_four_points_against = response.css(".wisbb_fvStand:nth-child(4) td:nth-child(7)").css("::text").extract()
    team_four_division_record = response.css(".wisbb_fvStand:nth-child(4) td:nth-child(11)").css("::text").extract() 
    team_four_streak = response.css(".wisbb_fvStand:nth-child(4) td:nth-child(12)").css("::text").extract()

    items['divisions'] = divisions
    items['team_one_name'] = team_one_name
    items['team_one_wins'] = team_one_wins
    items['team_one_loses'] = team_one_loses
    items['team_one_ties'] = team_one_ties
    items['team_one_percentage'] = team_one_percentage
    items['team_one_points_for'] = team_one_points_for
    items['team_one_points_against'] = team_one_points_against
    items['team_one_division_record'] = team_one_division_record
    items['team_one_streak'] = team_one_streak
    items['team_two_name'] = team_two_name
    items['team_two_wins'] = team_two_wins
    items['team_two_loses'] = team_two_loses
    items['team_two_ties'] = team_two_ties
    items['team_two_percentage'] = team_two_percentage
    items['team_two_points_for'] = team_two_points_for
    items['team_two_points_against'] = team_two_points_against
    items['team_two_division_record'] = team_two_division_record
    items['team_two_streak'] = team_two_streak
    items['team_three_name'] = team_three_name
    items['team_three_wins'] = team_three_wins
    items['team_three_loses'] = team_three_loses
    items['team_three_ties'] = team_three_ties
    items['team_three_percentage'] = team_three_percentage
    items['team_three_points_for'] = team_three_points_for
    items['team_three_points_against'] = team_three_points_against
    items['team_three_division_record'] = team_three_division_record
    items['team_three_streak'] = team_three_streak
    items['team_four_name'] = team_four_name
    items['team_four_wins'] = team_four_wins
    items['team_four_loses'] = team_four_loses
    items['team_four_ties'] = team_four_ties
    items['team_four_percentage'] = team_four_percentage
    items['team_four_points_for'] = team_four_points_for
    items['team_four_points_against'] = team_four_points_against
    items['team_four_division_record'] = team_four_division_record
    items['team_four_streak'] = team_four_streak

    yield items