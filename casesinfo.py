from bs4 import BeautifulSoup
import requests
import time


html_text = requests.get('https://www.coronavirus.vic.gov.au/victorian-coronavirus-covid-19-data').text
soup = BeautifulSoup(html_text, 'lxml')
cases = soup.find('div', class_ = 'ch-daily-update__statistics-item-text').text
last_time = soup.find('div', class_ = 'rpl-markup__inner').text

result = (cases + " cases acquired in Victoria (last 24 hours) (" + last_time +")")

