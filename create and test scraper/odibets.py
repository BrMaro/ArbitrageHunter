import random
import requests
from datetime import datetime, timedelta


class Match:
    def __init__(self, website, home_team, away_team, odd_1, odd_x, odd_2):
        self.website = website
        self.home_team = home_team
        self.away_team = away_team
        self.odd_1 = odd_1
        self.odd_x = odd_x
        self.odd_2 = odd_2


def odibet_arrays():
    odibet_arrays = []
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/56.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0.3 Safari/602.3.12",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Mozilla/5.0 (Linux; Android 7.0; Nexus 5X Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36"
    ]

    sports_ids = ["1", "2", "5", "4", "21", "6", "23", "22", "3", "29", "7", "esports", "vsoccer"]
    odibets_api_url = "https://api.odi.site/odi/sportsbook?resource=sportevents&platform=desktop"

    # Fetch the last date from the API
    headers = {"User-Agent": random.choice(user_agents)}
    response = requests.get(f"{odibets_api_url}?resource=sport", headers=headers)
    data = response.json()
    print(data["data"]["days"][-1]["schedule_date"])
    last_date = data["data"]["days"][-1]["schedule_date"]

    # Calculate all dates between today and the last date
    today = datetime.now().date()
    last_date_obj = datetime.strptime(last_date, "%Y-%m-%d").date()
    date_range = [(today + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((last_date_obj - today).days + 1)]
    print(date_range)
    for sport_id in sports_ids:
        for date in date_range:
            params = {
                "sport_id": sport_id,
                "day": date,
                "per_page": 1000,
            }
            response = requests.get(odibets_api_url, headers=headers, params=params)
            if response.status_code != 200:
                continue
            data = response.json()
            leagues = data["data"]["leagues"]

            for league in leagues:
                if "matches" not in league:
                    # Skip if the 'matches' key is missing
                    continue

                matches = league["matches"]
                for match in matches:
                    sport = match["sport_name"]
                    start_time = match["start_time"]
                    home_team = match["home_team"]
                    away_team = match["away_team"]
                    start_time = match["start_time"]
                    markets_per_match = match["markets"]

                    for market in markets_per_match:
                        if market["odd_type"] == "1X2":
                            lines = market["lines"][0]
                            outcomes = lines["outcomes"]

                            if len(outcomes) < 3:
                                continue

                            odd_1 = outcomes[0]["odd_value"]
                            odd_x = outcomes[1]["odd_value"]
                            odd_2 = outcomes[2]["odd_value"]

                            website = "OdiBets"
                            print(website, start_time, sport,start_time, home_team, away_team, odd_1, odd_x, odd_2)


odibet_arrays()
