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


def mozzart_arrays():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    url = "https://www.mozzartbet.co.ke/"
    driver.get(url)
    driver.implicitly_wait(10)

    odd_elements = driver.find_elements(By.XPATH, "//span[@class='odd-font betting-regular-match font-18' ]")
    home_teams = driver.find_elements(By.XPATH, "//div[@class='teams']")

    odds_1 = []
    odds_x = []
    odds_2 = []
    teams = []
    mozzart_objects = []

    for team in range(0, len(home_teams)):
        team_text = home_teams[team].text
        team_text = team_text.split("\n")[0]
        teams.append(team_text)

    for odd in range(0, len(odd_elements), 3):
        odds_1.append(float(odd_elements[odd].text))
        odds_x.append(float(odd_elements[odd + 1].text))
        odds_2.append(float(odd_elements[odd + 2].text))

    for no in range(len(teams)):
        instance = Match(url, teams[no], odds_1[no], odds_x[no], odds_2[no])
        #print(instance.website,instance.home_team,instance.odd_1,instance.odd_x,instance.odd_2)
        mozzart_objects.append(instance)

    driver.quit()
    return mozzart_objects




