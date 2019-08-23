# import scrapy
# from ..items import ScheduleItem

# class ScheduleSpider(scrapy.Spider):
#   name = "schedule"
#   i = 1
#   teams = ["BUF/buffalo-bills", "MIA/miami-dolphins", "NYJ/new-york-jets", "NE/new-england-patriots", 
#     "DAL/dallas-cowboys" ,"NYG/new-york-giants", "PHI/philadelphia-eagles", "WAS/washington-redskins",
#     "BAL/baltimore-ravens", "CIN/cincinnati-bengals", "CLE/cleveland-browns", "PIT/pittsburgh-steelers",
#     "CHI/chicago-bears", "DET/detroit-lions", "GB/green-bay-packers", "MIN/minnesota-vikings",
#     "HOU/houston-texans", "IND/indianapolis-colts", "JAC/jacksonville-jaguars", "TEN/tennessee-titans",
#     "ATL/atlanta-falcons", "CAR/carolina-panthers", "NO/new-orleans-saints", "TB/tampa-bay-buccaneers",
#     "DEN/denver-broncos", "KC/kansas-city-chiefs", "LAC/los-angeles-chargers", "OAK/oakland-raiders",
#     "ARI/arizona-cardinals", "LAR/los-angeles-rams", "SF/san-francisco-49ers", "SEA/seattle-seahawks"]
  
#   home_teams = ["Buffalo Bills", "Miami Dolphins", "New York Jets", "New England Patriots", 
#     "Dallas Cowboys" ,"New York Giantes", "Philadelphia Eagles", "Washington Redskins",
#     "Baltimore Ravens", "Cinncinnati Bengals", "Cleveland Browns", "Pittsburgh Steelers",
#     "Chicago Bears", "Detroit Lions", "Green Bay Packers", "Minnesota Vikings",
#     "Houston Texans", "Indianapolis Colts", "Jacksonville Jaguars", "Tennessee Titans",
#     "Atlanta Falcons", "Carolina Panthers", "New Oleans Saints", "Tampa Bay Buccaneers",
#     "Denver Broncos", "Kansas City Chiefs", "Los Angeles Chargers", "Oakland Raiders",
#     "Arizona Cardinals", "Los Angeles Rams", "San Francisco 49ers", "Seattle Seahawks"]
   
#   start_urls = [
#     'https://www.cbssports.com/nfl/teams/BUF/buffalo-bills/schedule/'
#     ]
  

#   def parse(self, response):
#     items = ScheduleItem()
#     all_teams = response.css("tr.TableBase-bodyTr")
    
#     for t in all_teams:

#       team = ScheduleSpider.home_teams[ScheduleSpider.i - 1]
#       away_team = t.css(".TeamName a").css("::text").extract()
#       date = t.css(".CellGameDate").css("::text").extract()
#       result = t.css(".CellGame-win").css("::text").extract() 
      
  
#       items['team'] = team
#       items['away_team'] = away_team
#       items['date'] = date
#       items['result'] = result
     
#       yield items

#       next_page = 'https://www.cbssports.com/nfl/teams/' + ScheduleSpider.teams[ScheduleSpider.i] + '/schedule/'
#       if ScheduleSpider.i < 33:
#         ScheduleSpider.i += 1
#         yield response.follow(next_page, callback = self.parse)

