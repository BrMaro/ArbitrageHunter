import random
import requests


def betika_arrays():
    betika_arrays = []
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/56.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0.3 Safari/602.3.12",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Mozilla/5.0 (Linux; Android 7.0; Nexus 5X Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36"
    ]
    results = 5000
    betika_api_url = f"https://api.betika.com/v1/uo/matches?page=1&limit={results}&tab=upcoming&sub_type_id=1,186,340&sport_id=14&sort_id=2&period_id=9&esports=false"
    headers = {"User-Agent": random.choice(user_agents)}
    response = requests.get(betika_api_url, headers=headers)
    data = response.json()

    sports_data = data["data"]
    for sport in sports_data:
        sport_name = sport["sport_name"]
        home_team = sport["home_team"]
        away_team = sport["away_team"]
        odd_1 = sport["home_odd"]
        odd_x = sport["neutral_odd"]
        odd_2 = sport["away_odd"]
        start_time = sport["start_time"]
        print(sport_name, start_time, home_team, away_team, odd_1, odd_x, odd_2)

    print(len(sports_data))


print(betika_arrays())
