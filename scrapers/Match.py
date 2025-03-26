class Match:
    def __init__(self, website, home_team, away_team, match_date=None, sport=None):
        self.website = website
        self.home_team = home_team
        self.away_team = away_team
        self.match_date = match_date
        self.sport = sport
        self.odd_1 = None
        self.odd_x = None
        self.odd_2 = None

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} ({self.website}) on {self.match_date} in {self.sport}"