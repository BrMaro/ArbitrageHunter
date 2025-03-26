import random
import requests
from scrapers.base_scraper import BaseScraper
from scrapers.config import SCRAPER_SETTINGS
from scrapers.Match import Match


class BetikaScraper(BaseScraper):
    def fetch_data(self):
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/56.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0.3 Safari/602.3.12",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
            "Mozilla/5.0 (Linux; Android 7.0; Nexus 5X Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36"
        ]
        headers = {"User-Agent": random.choice(user_agents)}
        response = requests.get(SCRAPER_SETTINGS["betika"]["url"], headers=headers, params=SCRAPER_SETTINGS["betika"]["params"])
        return response.json()

    def parse_data(self, data):
        betika_matches = []
        sports_data = data["data"]
        for sport in sports_data:
            match = Match(
                website="Betika",
                home_team=sport["home_team"],
                away_team=sport["away_team"],
                match_date=sport["start_time"],
                sport=sport["sport_name"]
            )
            match.odd_1 = sport["home_odd"]
            match.odd_x = sport["neutral_odd"]
            match.odd_2 = sport["away_odd"]
            betika_matches.append(match)
        return betika_matches

scraper = BetikaScraper()
matches = scraper.scrape()
for match in matches:
    print(match)