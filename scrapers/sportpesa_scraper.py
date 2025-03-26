import random
import requests
from scrapers.base_scraper import BaseScraper
from scrapers.config import SCRAPER_SETTINGS
from scrapers.Match import Match
from helpers.time_utils import convert_to_eat

class SportPesaScraper(BaseScraper):
    def fetch_data(self):
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/56.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0.3 Safari/602.3.12",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
            "Mozilla/5.0 (Linux; Android 7.0; Nexus 5X Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36"
        ]
        headers = {"User-Agent": random.choice(user_agents)}
        all_highlights_data = []

        # Collect data for highlights 1 through 12
        for highlight_id in range(1, 13):
            sportpesa_highlights_url = f"https://www.ke.sportpesa.com/api/highlights/{highlight_id}"
            response = requests.get(sportpesa_highlights_url, headers=headers)
            highlights_data = response.json()
            all_highlights_data.extend(highlights_data)

        # Extract match IDs as strings
        match_ids = [str(item["id"]) for item in all_highlights_data]

        # Construct the markets URL using the match IDs
        match_ids_str = ",".join(match_ids)
        sportpesa_markets_url = f"https://www.ke.sportpesa.com/api/games/markets?games={match_ids_str}&markets=10"
        markets_response = requests.get(sportpesa_markets_url, headers=headers)
        markets_data = markets_response.json()

        # Combine the markets data into the highlights data
        for highlight in all_highlights_data:
            match_id = str(highlight["id"])
            highlight["markets"] = markets_data.get(match_id, [])

        return all_highlights_data

    # def __init__(self, website, home_team, away_team, match_date=None, sport=None):

    def parse_data(self, data):
        sportpesa_matches = []
        highlights_data = data
        for index, match in enumerate(highlights_data):
            sport = match.get("sport").get("name")
            date = convert_to_eat(match.get("date"))
            markets = match.get("markets", [])
            
            if not markets or not markets[0].get("selections"):
                # Skip if no markets or selections are available
                continue

            selections = markets[0].get("selections", [])
            if len(selections) < 3:
                # Skip if there are not enough selections for home, draw, and away odds
                continue

            home_team = selections[0].get("name")
            odds_1 = selections[0].get("odds")
            odds_x = selections[1].get("odds")
            away_team = selections[2].get("name")
            odds_2 = selections[2].get("odds")

            match_obj = Match("SportPesa", home_team, away_team, date, sport)
            match_obj.odd_1 = odds_1
            match_obj.odd_x = odds_x 
            match_obj.odd_2 = odds_2
            
            sportpesa_matches.append(match_obj)

        return sportpesa_matches


scraper = SportPesaScraper()
matches = scraper.scrape()
for match in matches:
    print(match)
print(len(matches))