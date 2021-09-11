from io import DEFAULT_BUFFER_SIZE
from platform import platform
import random
from discord import player
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
from collections import Counter


#DRIVER_PATH = '/usr/local/bin/google-chrome'
#driver = webdriver.Chrome(executable_path=DRIVER_PATH)

URL = "https://lolchess.gg/champions/set5.5/Khazix"
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
driver = webdriver.Chrome(options=options)
#driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
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
originCount=[]
classCount=[]


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
                originCount.append(x)
            else:
                originCount.append(x)
    else:
        if i[1] not in originPool:
            originPool.append(i[1])
            originCount.append(i[1])
        else:
            originCount.append(i[1])

for i in legPool:
    if isinstance(i[2], list):
        for x in i[2]:
            if x not in classPool:
                classPool.append(x)
                classCount.append(x)
            else:
                classCount.append(x)
    else:
        if i[2] not in classPool:
            classPool.append(i[2])
            classCount.append(i[2])
        else:
            classCount.append(i[2])

originCount=Counter(originCount)
classCount=Counter(classCount)

def originGen():
    maxlim=len(originPool)
    output=originPool[random.randrange(0,maxlim)]
    return output

def classGen():
    maxlim=len(classPool)
    output=classPool[random.randrange(0,maxlim)]
    return output

def findKing(trait, choice):
    poss=[]
    if choice ==1: 
        for i in range(len(legPool)):
            if trait in legPool[i][1]:
                poss.append(legPool[i])
            else:
                pass

    chance=random.randrange(0,len(poss))
    output=poss[chance]
    print(output)
    return output




def kingGen(lst):
    for i in lst:
        poss=[]
        chance=random.randrange(1,3)
        if chance==1:
            for j in range(len(legPool)):
                if i[1] in legPool[j][1]:
                    poss.append(legPool[j])
                else:
                    pass    
        elif chance==2:
            for j in range(len(legPool)):
                if i[2] in legPool[j][2]:
                    poss.append(legPool[j])
                else:
                    pass
        chance=random.randrange(0,len(poss))    
        i.append(poss[chance][0])                
    return lst


def main(lst):
    players=lst
    for i in range(len(players)):
        origin=originGen()
        classs=classGen()
        while originCount['{}'.format(origin)]+classCount['{}'.format(classs)]<7:
            origin=originGen()
            classs=classGen()
        players[i]=[players[i],origin,classs]
    players=kingGen(players)      
    return players



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


