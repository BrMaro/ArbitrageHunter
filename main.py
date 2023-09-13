from mozzartbet import mozzart_arrays
from betika import betika_arrays
from sportpesa import sportpesa_arrays

mozzart_objects = mozzart_arrays()
betika_objects = betika_arrays()
sportpesa_objects = sportpesa_arrays()

all_matches = []
all_matches.extend(mozzart_objects)
all_matches.extend(betika_objects)
all_matches.extend(sportpesa_objects)


def find_potential_bets(match_to_compare,matches):
    similar_matches = []
    for match in matches:
        if match_to_compare.home_team == match.home_team:
            similar_matches.append(match)

    #finds the largest odds
    match_with_max_odds_1 = max(similar_matches, key=lambda x: x.odd_1)
    match_with_max_odds_2= max(similar_matches, key=lambda x: x.odd_2)
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
    find_potential_bets(match,all_matches)
























# def arbitrable(site_a_teams, site_a_odds_1, site_b_odds_1, site_a_odds_x, site_b_odds_x, site_a_odds_2, site_b_odds_2):
#     site_a_arbitrable_matches = []
#     for match_no_site_a, match_no_site_b in zip(site_a_commons, site_b_commons):
#         percentage = (1 / (max(site_a_odds_1[match_no_site_a], site_b_odds_1[match_no_site_b])) + 1 / (
#             max(site_a_odds_x[match_no_site_a], site_b_odds_x[match_no_site_b])) + 1 / (
#                           max(site_a_odds_2[match_no_site_a], site_b_odds_2[match_no_site_b]))) * 100
#         if percentage < 100:
#             site_a_arbitrable_matches.append(site_a_teams[match_no_site_a])
#             print(percentage, (max(site_a_odds_1[match_no_site_a], site_b_odds_1[match_no_site_b])),
#                   (max(site_a_odds_x[match_no_site_a], site_b_odds_x[match_no_site_b])),
#                   (max(site_a_odds_2[match_no_site_a], site_b_odds_2[match_no_site_b])))

#   return site_a_arbitrable_matches


#print("Arbitrable = ", arbitrable())
