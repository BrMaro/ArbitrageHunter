from scrapers.betika_scraper import BetikaScraper
from scrapers.sportpesa_scraper import SportPesaScraper
import time

def test_scraper(scraper, name):
    print(f"\nTesting {name}...")
    try:
        start_time = time.time()
        results = scraper.scrape()
        duration = time.time() - start_time
        
        if results and len(results) > 0:
            print(f"✅ Success! Found {len(results)} matches")
            print(f"Sample match: {results[0]['home_team']}")
            print(f"Sample odds: {results[0]['odd_1']} - {results[0]['odd_x']} - {results[0]['odd_2']}")
        else:
            print("❌ No matches found")
        print(f"Duration: {duration:.2f} seconds")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    test_scraper(BetikaScraper(), "Betika")
    test_scraper(SportPesaScraper(), "SportPesa")