from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import pandas as pd
import time
from datetime import datetime, date, timedelta
import datetime as dt
import numpy as np
import pytz
import math

def time_check():
    now = dt.datetime.now()
    melb_tz = pytz.timezone('Australia/Melbourne')
    cases_cock = open("cases_cuh.txt", "r")
    cock_content = cases_cock.readline()
    cases_cock.close() 
    prevTime = datetime.strptime(cock_content, "%Y-%m-%d %H:%M:%S.%f%z")
    now = melb_tz.localize(now)
    timeDiff = now - prevTime
    if timeDiff > timedelta(minutes=10):
        cases_peen = open("cases_cuh.txt", "w")   
        cases_peen.write(str(now))
        cases_peen.close()
        return True
    return False # return boolean based on difference


def scrapeCases():
    html_vic = requests.get('https://www.coronavirus.vic.gov.au/').text
    soupM = BeautifulSoup(html_vic, 'lxml')
    casesMelb = soupM.find_all('div', class_ = 'ch-daily-update__statistics-item-text')[3].text
    vaxProgressText = soupM.find_all('div', class_ = 'ch-daily-update__statistics-item-text')[2].text
    vaxProgress = vaxProgressText.strip('%')
    fillCount = float(vaxProgress) / 70 * 20
    roundCount = math.floor(fillCount)
    block = '\u25a0'
    emptyBlock = '\u25a1'
    progressBar = roundCount*block + (20-roundCount)*emptyBlock
    progressResult = "Lockdown end: " + progressBar + " " + vaxProgressText + " / 70% fully vaccinated"
    melb_tz = pytz.timezone('Australia/Melbourne')
    now = dt.datetime.now()
    now_adj = now.astimezone(melb_tz)
    # print(now_adj)
    timeMelb = now_adj.strftime("%B %d, %Y %I:%M %p")
    # print(timeMelb)
    melbResult = (casesMelb + " cases acquired in Victoria (last 24 hours) (Last updated: " + timeMelb +")")
    # print(progressResult)

    # old = np.load("cases_bruh") 
    # print(old[0])
    # DRIVER_PATH = 'C:\Program Files (x86)\chromedriver.exe'
    # driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    # URL = "https://www.health.nsw.gov.au/Infectious/covid-19/Pages/default.aspx"
    # options = Options()
    # options.headless = True
    # options.add_argument("--window-size=1920,1200")
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--incognito')
    # driver = webdriver.Chrome(options=options)

    # # driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    # driver.get(URL)
    # driver.implicitly_wait(5)
    # page_source = driver.page_source
    # soupS = BeautifulSoup(driver.page_source, 'lxml')
    # casesSyd = soupS.find_all("span", {"class": "number"})[3].text
    # sydResult = (casesSyd + " cases acquired in NSW (last 24 hours)")
    # driver.quit()
    
    return [progressResult, melbResult] # returns 2D array

# scrapeCases()

def mainCases():
    if time_check():
        cases = scrapeCases()
        with open("cases_bruh", "wb") as f:
            np.save(f , np.array(cases))
        return cases
    else:
        return np.load("cases_bruh") 
