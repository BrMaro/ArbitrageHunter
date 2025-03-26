from scrapers.betika_scraper import BetikaScraper
from scrapers.sportpesa_scraper import SportPesaScraper
# Import other scrapers here

class ScraperManager:
    def __init__(self):
        self.scrapers = [
            BetikaScraper(),
            SportPesaScraper(),
            # Add other scrapers here
        ]

    def run_scrapers(self):
        all_matches = []
        for scraper in self.scrapers:
            all_matches.extend(scraper.scrape())
        return all_matches
