from scrapers.scraper_manager import ScraperManager

scraper_manager = ScraperManager()
all_matches = scraper_manager.run_scrapers()

no_arbitrage_count = 0  # Counter for no arbitrage situations


def calculate_stakes(amount, odd_1, odd_x, odd_2):
    """
    Calculates the stakes to distribute a given amount across outcomes to guarantee arbitrage profit.
    """
    total_inverse_odds = (1 / odd_1) + (1 / odd_x) + (1 / odd_2)
    stake_1 = (amount / total_inverse_odds) * (1 / odd_1)
    stake_x = (amount / total_inverse_odds) * (1 / odd_x)
    stake_2 = (amount / total_inverse_odds) * (1 / odd_2)

    guaranteed_payout = amount / total_inverse_odds

    print("\n💰 Stake Distribution:")
    print(f"Stake on 1: {stake_1:.2f}")
    print(f"Stake on X: {stake_x:.2f}")
    print(f"Stake on 2: {stake_2:.2f}")
    print(f"Total Stake: {stake_1 + stake_x + stake_2:.2f}")
    print(f"Guaranteed Payout: {guaranteed_payout:.2f}")
    print(f"Guaranteed Profit: {guaranteed_payout - amount:.2f}")


def find_potential_bets(match_to_compare, matches):
    """
    Finds potential arbitrage opportunities for a given match by comparing odds across all matches.
    Handles both 3-way and 2-way bets.
    """
    similar_matches = [
        match for match in matches
        if match_to_compare.home_team == match.home_team
           and match_to_compare.away_team == match.away_team
           # and match_to_compare.match_date == match.match_date  # Ensure the same start time
    ]

    if not similar_matches:
        return

    try:
        # Find the matches with the highest odds for each outcome
        match_with_max_odds_1 = max(similar_matches, key=lambda x: float(x.odd_1))
        match_with_max_odds_2 = max(similar_matches, key=lambda x: float(x.odd_2))

        if hasattr(match_to_compare, 'odd_x') and match_to_compare.odd_x is not None:
            # Handle 3-way bets
            match_with_max_odds_x = max(similar_matches, key=lambda x: float(x.odd_x))
            arbitrage_condition = (
                    1 / float(match_with_max_odds_1.odd_1) +
                    1 / float(match_with_max_odds_x.odd_x) +
                    1 / float(match_with_max_odds_2.odd_2)
            )
        else:
            # Handle 2-way bets
            arbitrage_condition = (
                    1 / float(match_with_max_odds_1.odd_1) +
                    1 / float(match_with_max_odds_2.odd_2)
            )

        if arbitrage_condition < 1:
            print("\n🎉 Arbitrage opportunity found!")
            print(f"Match: {match_to_compare.home_team} vs {match_to_compare.away_team}")
            print(f"Max odds for 1: {match_with_max_odds_1.odd_1} (Website: {match_with_max_odds_1.website})")
            if hasattr(match_to_compare, 'odd_x') and match_to_compare.odd_x is not None:
                print(f"Max odds for X: {match_with_max_odds_x.odd_x} (Website: {match_with_max_odds_x.website})")
            print(f"Max odds for 2: {match_with_max_odds_2.odd_2} (Website: {match_with_max_odds_2.website})")
            print(f"Arbitrage condition: {arbitrage_condition:.4f}")
            print(f"Expected profit: {100 - arbitrage_condition * 100:.2f}%")

            # Call the calculate_stakes function
            calculate_stakes(1000, float(match_with_max_odds_1.odd_1), float(match_with_max_odds_x.odd_x),
                             float(match_with_max_odds_2.odd_2))
        else:
            global no_arbitrage_count
            no_arbitrage_count += 1  # Increment the counter for no arbitrage situations

    except ValueError as e:
        print(f"Error finding arbitrage opportunities: {e}")


for match in all_matches:
    find_potential_bets(match, all_matches)

print(f"\nNumber of situations with no arbitrage opportunities: {no_arbitrage_count}")
