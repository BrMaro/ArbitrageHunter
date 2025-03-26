from scrapers.scraper_manager import ScraperManager

scraper_manager = ScraperManager()
all_matches = scraper_manager.run_scrapers()

def find_potential_bets(match_to_compare, matches):
    similar_matches = []
    for match in matches:
        if match_to_compare.home_team == match.home_team:
            similar_matches.append(match)

    match_with_max_odds_1 = max(similar_matches, key=lambda x: x.odd_1)
    match_with_max_odds_2 = max(similar_matches, key=lambda x: x.odd_2)
    match_with_max_odds_x = max(similar_matches, key=lambda x: x.odd_x)

    if 1/match_with_max_odds_1.odd_1 + 1/match_with_max_odds_x.odd_x + 1/match_with_max_odds_2.odd_2 < 1:
        print("Arbitrage opportunity found!")
        print(f"Max odds1: {match_with_max_odds_1.odd_1} (Website: {match_with_max_odds_1.website}) (Home team: {match_with_max_odds_1.home_team})")
        print(f"Max oddsx: {match_with_max_odds_x.odd_x} (Website: {match_with_max_odds_x.website}) (Home team: {match_with_max_odds_x.home_team})")
        print(f"Max odds2: {match_with_max_odds_2.odd_2} (Website: {match_with_max_odds_2.website}) (Home team: {match_with_max_odds_2.home_team})")
        print(f"Expected profit: {100 - (1/match_with_max_odds_1.odd_1 + 1/match_with_max_odds_x.odd_x + 1/match_with_max_odds_2.odd_2)*100}")
    else:
        print("No arbitrage opportunity found.")
    return similar_matches

for match in all_matches:
    find_potential_bets(match, all_matches)
