from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Match:
    def __init__(self, website,home_team,odd_1,odd_x,odd_2):
        self.website = website
        self.home_team = home_team
        self.odd_1 = odd_1
        self.odd_x = odd_x
        self.odd_2 = odd_2

def sportpesa_arrays():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    url = "https://www.sportpesa.com/sports/football/"
    esports_url = "https://www.ke.sportpesa.com/esports"
    driver.get(url)
    driver.implicitly_wait(10)

    divs = driver.find_elements(By.CSS_SELECTOR,"div.ng-binding")


    all_odds = []
    home_teams = []

    divs = [divs[div] for div in range(len(divs)) if not (divs[div].text == 1.5 and divs[div - 1].text == 1.2 and divs[div + 1].text == 1.8)]

    for div in range(len(divs)):
        #print(divs[div].text)
        if divs[div].text.isupper():
            home_teams.append(divs[div].text)
        if divs[div].text.replace(".", "").isdigit():
            all_odds.append(divs[div].text)
        if divs[div].text == "" and not divs[div+1].text.isupper():
            all_odds.append(divs[div].text)

    # Remove all sequences of 1.2, 1.5, 1.8 in all_odds array
    i = 0
    while i < len(all_odds) - 2:
        if all_odds[i:i+3] == ['1.20', '1.50', '1.80']:
            del all_odds[i:i+3]
        else:
            i += 1


    home_teams = [x for i, x in enumerate(home_teams) if i % 2 == 0]

    odds_1=[]
    odds_x=[]
    odds_2=[]
    sportpesa_objects = []

    for odd in range(0, len(all_odds), 10):
        odds_1.append(all_odds[odd])
        odds_x.append(all_odds[odd+1])
        odds_2.append(all_odds[odd+2])


    for no in range(len(home_teams)):
        instance = Match(url, home_teams[no], odds_1[no], odds_x[no], odds_2[no])
        if "-" not in [instance.odd_1, instance.odd_x, instance.odd_2]:
            instance.odd_1 = float(instance.odd_1)
            instance.odd_x = float(instance.odd_x)
            instance.odd_2 = float(instance.odd_2)
            sportpesa_objects.append(instance)
    driver.quit()
    return sportpesa_objects
print(sportpesa_arrays()[1].home_team)

