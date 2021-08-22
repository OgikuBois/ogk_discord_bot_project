from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import pandas as pd
import time
from datetime import datetime

def getCases():
    # timeNowRaw = datetime.now(tz_victoria)
    # current_time = timeNowRaw.strftime("%H:%M:%S")

    # #DEBUG
    # print("Current time in Victoria: {}".format(current_time)

    html_vic = requests.get('https://www.coronavirus.vic.gov.au/victorian-coronavirus-covid-19-data').text
    soupM = BeautifulSoup(html_vic, 'lxml')
    casesMelb = soupM.find('div', class_ = 'ch-daily-update__statistics-item-text').text
    timeMelb = soupM.find('div', class_ = 'rpl-markup__inner').text
    melbResult = (casesMelb + " cases acquired in Victoria (last 24 hours) (" + timeMelb +")")

    DRIVER_PATH = 'C:\Program Files (x86)\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    URL = "https://nswdac-covid-19-postcode-heatmap.azurewebsites.net/Localcases.html"
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')

    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get(URL)
    driver.implicitly_wait(5)
    page_source = driver.page_source
    soupS = BeautifulSoup(driver.page_source, 'lxml')
    casesSyd = soupS.find("p", {"id": "Number"}).text
    sydResult = (casesSyd + " cases acquired in NSW (last 24 hours)") 
    driver.quit()
    
    return [melbResult, sydResult]
