from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import pandas as pd
import time
from datetime import datetime, date, timedelta
import datetime as dt
import numpy as np

def time_check():
    now = datetime.now()
    cases_cock = open("cases_cuh.txt", "r")
    cock_content = cases_cock.readline()
    cases_cock.close() 
    timeDiff = now - datetime.strptime(cock_content, "%Y-%m-%d %H:%M:%S.%f")
    if timeDiff > timedelta(hours=1):
        cases_peen = open("cases_cuh.txt", "w")   
        cases_peen.write(str(now))
        cases_peen.close()
        return True
    return False # return boolean based on difference

def scrapeCases():
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
    return [melbResult, sydResult] # returns 2D array

def mainCases():
    if time_check():
        cases = scrapeCases()
        with open("cases_bruh", "wb") as f:
            np.save(f , np.array(cases))
        return cases
    else:
        return np.load("cases_bruh") 