import random
import requests
import json
from helpers.time_utils import convert_to_eat

class Match:
    def __init__(self, website, home_team, away_team, odd_1, odd_x, odd_2):
        self.website = website
        self.home_team = home_team
        self.away_team = away_team
        self.odd_1 = odd_1
        self.odd_x = odd_x
        self.odd_2 = odd_2


def sportpesa_arrays():
    sportpesa_arrays = []
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/56.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0.3 Safari/602.3.12",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Mozilla/5.0 (Linux; Android 7.0; Nexus 5X Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36"
    ]

    sportpesa_highlights_url = "https://www.ke.sportpesa.com/api/highlights/1"
    headers = {"User-Agent": random.choice(user_agents)}

    # Request the highlights data
    response = requests.get(sportpesa_highlights_url, headers=headers)
    highlights_data = response.json()

    # Extract match IDs as strings
    match_ids = [str(item["id"]) for item in highlights_data]

    # Construct the markets URL using the match IDs
    match_ids_str = ",".join(match_ids)
    sportpesa_markets_url = (
        f"https://www.ke.sportpesa.com/api/games/markets?games={match_ids_str}&markets=10"
    )

    # Request the markets data (returns a dict keyed by match_id)
    markets_response = requests.get(sportpesa_markets_url, headers=headers)
    markets_data = markets_response.json()

    # Combine the markets data into the highlights data
    for highlight in highlights_data:
        match_id = str(highlight["id"])
        highlight["markets"] = markets_data.get(match_id, [])
    # def __init__(self, website, home_team, away_team, match_date=None, sport=None):

    # print(convert_to_eat(highlights_data[0].get("date")))
    print(highlights_data[0].get("sport").get("name"))

    for index, match in enumerate(highlights_data):
        sport = match.get("sport").get("name")
        date = convert_to_eat(match.get("date"))
        markets = match.get("markets", [])
        market_name = markets[0].get("name")
        selections = markets[0].get("selections", [])
        home_team = selections[0].get("name")
        odds_1 = selections[0].get("odds")
        odds_x = selections[1].get("odds")
        away_team = selections[2].get("name")
        odds_2 = selections[2].get("odds")

        print("sportpesa", home_team, away_team, odds_1, odds_x, odds_2, sport,date)
        instance = Match("sportpesa", home_team, away_team, odds_1, odds_x, odds_2)
        sportpesa_arrays.append(instance)


    return sportpesa_arrays

sportpesa_arrays()
