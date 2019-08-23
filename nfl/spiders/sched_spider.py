# only for preseason, update for regular season, and run again, we compiled during games so info was changing

import scrapy
from ..items import SchedItem

class SchedSpider(scrapy.Spider):
  name = "sched"
  page_number = 3
  start_urls = [
    'https://www.foxsports.com/nfl/schedule?season=2019&seasonType=3&week=2'
    ]

  def parse(self, response):
    items = SchedItem()

    all_games = response.css("tr")

    for date in all_games:
      away_team = date.css(".wisbb_firstTeam span:nth-child(3)").css("::text").extract_first()
      away_team_record = date.css(".wisbb_firstTeam .wisbb_teamRecord").css("::text").extract_first()
      away_team_score = date.css(".wisbb_firstTeam .wisbb_score").css("::text").extract()  
      home_team = date.css(".wisbb_secondTeam span:nth-child(3)").css("::text").extract_first()
      home_team_record = date.css(".wisbb_secondTeam .wisbb_teamRecord").css("::text").extract_first() 
      home_team_score = date.css(".wisbb_secondTeam .wisbb_score").css("::text").extract_first() 
      week = response.css(".wisbb_pageInfoSecondaryText").css("::text").extract_first()
      
    
      items['away_team'] = away_team
      items['away_team_record'] = away_team_record
      items['away_team_score'] = away_team_score
      items['home_team'] = home_team
      items['home_team_record'] = home_team_record
      items['home_team_score'] = home_team_score
      items['week'] = week
      
      
      yield items

      next_page = 'https://www.foxsports.com/nfl/schedule?season=2019&seasonType=3&week=' + str(SchedSpider.page_number)
      if SchedSpider.page_number <= 5:
        SchedSpider.page_number += 1
        yield response.follow(next_page, callback = self.parse)