import scrapy
from ..items import NflItem

class RosterSpider(scrapy.Spider):
  name = "roster"
  page_number = 2
  start_urls = [
    'https://www.foxsports.com/nfl/players?teamId=0&season=2019&position=0&page=1&country=0&grouping=0&weightclass=0'
    ]

  def parse(self, response):
    items = NflItem()

    all_players = response.css("tr.wisbb_fvStand")

    for player in all_players:
      name = player.css(".wisbb_fullPlayer span").css("::text").extract()  
      team = player.css(".wisbb_priorityColumn a").css("::text").extract()  
      number = player.css("td:nth-child(3) ").css("::text").extract()
      position = player.css("td:nth-child(4)").css("::text").extract()
      height = player.css("td:nth-child(6)").css("::text").extract()
      weight = player.css("td:nth-child(7)").css("::text").extract()
      age = player.css("td:nth-child(8)").css("::text").extract()
      college = player.css(".wisbb_priorityColumn+ td a").css("::text").extract()
      
      items['name'] = name
      items['team'] = team
      items['number'] = number
      items['position'] = position
      items['height'] = height
      items['weight'] = weight
      items['age'] = age
      items['college'] = college

      yield items

    next_page = 'https://www.foxsports.com/nfl/players?teamId=0&season=2019&position=0&page=' + str(RosterSpider.page_number) + '&country=0&grouping=0&weightclass=0'
    if RosterSpider.page_number <= 133:
      RosterSpider.page_number += 1
      yield response.follow(next_page, callback = self.parse)
  