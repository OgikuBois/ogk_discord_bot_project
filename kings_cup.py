from io import DEFAULT_BUFFER_SIZE
from platform import platform
import random
from discord import player
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
from collections import defaultdict


DRIVER_PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
URL = "https://lolchess.gg/champions/set5.5/Khazix"
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get(URL)
driver.implicitly_wait(5)
page_source = driver.page_source
soup = BeautifulSoup(driver.page_source, 'lxml')
tables = soup.find_all("table",{"class":"guide-champion-table w-100"})
dfs = pd.read_html(str(tables))
driver.quit()

legPool=[None] *len(dfs[0])
originPool=[]
classPool=[]

for i in range(len(dfs[0])):
    output=[]
    output.append(dfs[0]['Champion'][i])
    dsplit=dfs[0]['Origin'][i].split()
    if len(dsplit)> 1:
        output.append([dsplit[0], dsplit[1]])
    else:
        output.append(dfs[0]['Origin'][i])
    dsplit=dfs[0]['Class'][i].split()
    if len(dsplit)> 1:
        output.append([dsplit[0], dsplit[1]])
    else: 
        output.append(dfs[0]['Class'][i])
    legPool[i]=output

for i in legPool:
    if isinstance(i[1], list):
        for x in i[1]:
            if x not in originPool:
                originPool.append(x)
    else:
        if i[1] not in originPool:
                originPool.append(i[1])

for i in legPool:
    if isinstance(i[2], list):
        for x in i[2]:
            if x not in classPool:
                classPool.append(x)
    else:
        if i[2] not in classPool:
                classPool.append(i[2])


def originGen():
    maxlim=len(originPool)
    output=originPool[random.randrange(0,maxlim)]
    return output

def classGen():
    maxlim=len(classPool)
    output=classPool[random.randrange(0,maxlim)]
    return output

def kingGen(lst):
    for i in lst:
        chance=random.randrange(1,3)
        if chance==1:
            kingOut=originGen()
        elif chance==2:
            kingOut=classGen()

        
        
    return lst


def main(lst):
    players=lst
    for i in range(len(players)):
        players[i]=[players[i],originGen(),classGen()]
    players=kingGen(players)         
    # output=kingGen(lst)
    print(players)
    return

main(["a","b","c","d"])
# def whatIsMyKing(traitList):
#     king = ""
#     originOrClass = random.randrange(0,2)
#     if z[0] != "":
#         y = z
#     if originOrClass == 0:
#         originEnd = len(x) # no need to + 1 because of the name at pos 0
#         kingNumber = random.randrange(1, originEnd)
#         king = x[kingNumber]

#     if originOrClass == 1:
#         classEnd = len(y)
#         kingNumber = random.randrange(1, classEnd)
#         king = y[kingNumber]
#     return king

# #===========================================
# # Main Game Function 
# #===========================================
# def main(player_list):
    

#     for player in player_list:
        
#         storedTraits = whatTraits()
        
        
        
#         Origin = storedTraits[0]
#         Class = storedTraits[1]
#         if len(storedTraits) >= 3:
#             thirdOrigin = storedTraits[2]
#         else:
#             thirdOrigin = [""]

#         if len(storedTraits) == 2: 
#             print(player + ":", storedTraits[0], storedTraits[1] + "|| Your King Is:", whatIsMyKing(storedTraits) + "\n")
        
#         # Loop for 3 trait player statement
#         else: 
#             print(player + ":", storedTraits[0] + " " + storedTraits[1] + " " + storedTraits[2] + " || Your King Is:", whatIsMyKing(storedTraits) + "\n")





#     reroll = "y"
#     while reroll == "y":
#         reroll = input("Would you like to reroll y/n? ")
#         if reroll == "n":
#             break
#         elif reroll != "y" or reroll != "n":
#             print("Invalid Input. Try again.")   


#         # for k in people:
#         #     storedTraits = whatTraits()
#         #     Origin = storedTraits[0]
#         #     Class = storedTraits[1]
#         #     if len(storedTraits) >= 3:
#         #         thirdOrigin = storedTraits[2]
#         #     else:
#         #         thirdOrigin = [""]
#         #     print(k + ":", Origin[0], Class[0], thirdOrigin[0], "| Your King Is:", whatIsMyKing(Origin, Class, thirdOrigin))


