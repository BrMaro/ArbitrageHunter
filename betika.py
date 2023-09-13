from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

class Match:
    def __init__(self, website,home_team,odd_1,odd_x,odd_2):
        self.website = website
        self.home_team = home_team
        self.odd_1 = odd_1
        self.odd_x = odd_x
        self.odd_2 = odd_2


def betika_arrays():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    url = "https://www.betika.com/en-ke/"
    driver.get(url)
    driver.implicitly_wait(10)

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        # Check if the page has reached the bottom
        current_scroll_position = driver.execute_script("return window.pageYOffset;")
        browser_height = driver.execute_script("return window.innerHeight;")
        document_height = driver.execute_script("return document.body.scrollHeight;")
        if current_scroll_position + browser_height >= document_height:
            break

    odd_elements = driver.find_elements(By.XPATH, "//span[@class='prebet-match__odd__odd-value bold']")
    home_teams = driver.find_elements(By.XPATH, "//span[@class='prebet-match__teams__home']")

    # Extract the text from the element
    odds_1 = []
    odds_x = []
    odds_2 = []
    teams = []
    betika_objects = []

    for team in home_teams:
        teams.append(team.text)

    for odd in range(0, len(odd_elements), 3):
        odds_1.append(float(odd_elements[odd].text))
        odds_x.append(float(odd_elements[odd + 1].text))
        odds_2.append(float(odd_elements[odd + 2].text))

    for no in range(len(teams)):
        instance = Match(url,teams[no],odds_1[no],odds_x[no],odds_2[no])
        #print(instance.home_team,instance.odd_1,instance.odd_x,instance.odd_2)
        betika_objects.append(instance)

    driver.quit()
    return betika_objects

