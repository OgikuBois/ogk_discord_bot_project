import random
#Origins
Abomination = ["Abomination", "Kalista", "Brand", "Nunu", "Fiddlesticks"]
Dawnbringer = ["Dawnbringer", "Gragas", "KhaZix", "Soraka", "Nidalee", "Riven", "Karma", "Garen"]
Draconic = ["Draconic", "Udyr", "Sett", "Ashe", "Zyra", "Galio", "Heimerdinger"]
Forgotten = ["Forgotten", "Vayne", "Hecarim", "Thresh", "MissFortune", "Draven", "Viego"]
Hellion = ["Hellion", "Kled", "Poppy", "Ziggs", "Kennen", "Tristana", "Lulu", "Teemo"]
Ironclad = ["Ironclad", "Nautilus", "Jax", "Rell"]
Nightbringer = ["Nightbringer", "Vladimir", "Sejuani", "LeeSin", "Yasuo", "Aphelios", "Diana"]
Redeemed = ["Redeemed", "Aatrox", "Leona", "Syndra", "Varus", "Lux", "Rell", "Velkoz", "Kayle"]
Revenant = ["Revenant", "Nocturne", "Fiddlesticks", "Ivern", "Volibear"]
Sentinel = ["Sentinel", "Olaf", "Senna", "Irelia", "Pyke", "Rakan", "Galio", "Lucian", "Akshan"]
#Classes
Assassin = ["Assassin", "Khazix", "Pyke", "Nocturne", "Diana", "Viego"]
Brawler = ["Brawler", "Gragas", "Sejuani", "Sett", "Nunu", "Volibear"]
Cannoneer = ["Cannoneer", "Senna", "Tristana", "MissFortune", "Lucian"]
Cavalier = ["Cavalier", "Kled", "Hecarim", "Sejuani", "Rell"]
Invoker = ["Invoker", "Syndra", "Ivern", "Karma", "Teemo"]
Knight = ["Knight", "Leona", "Poppy", "Nautilus", "Thresh", "Galio", "Garen"]
Legionnaire = ["Legionnaire", "Aatrox", "Kalista", "Irelia", "Riven", "Yasuo", "Draven", "Kayle"]
Mystic = ["Mystic", "Lulu", "Lux", "Fiddlesticks", "Gwen"]
Ranger = ["Ranger", "Vayne", "Varus", "Ashe", "Aphelios", "Akshan"]
Renewer = ["Renewer", "Vladimir", "Soraka", "Rakan", "Ivern", "Heimerdinger"]
Skirmisher = ["Skirmisher", "Udyr", "Olaf", "Irelia", "Kennen", "LeeSin", "Nidalee", "Jax", "Viego"]
Spellweaver = ["Spellweaver", "Ziggs", "Brand", "Zyra", "Velkoz"]

def whatTraits():
    output = []
    rngPleaseFirst = random.randrange(1,11)
#Origins
    if rngPleaseFirst == 1:
        output.append(Abomination)
    if rngPleaseFirst == 2:
        output.append(Dawnbringer)
    if rngPleaseFirst == 3:
        output.append(Draconic)
    if rngPleaseFirst == 4:
        output.append(Forgotten)
    if rngPleaseFirst == 5:
        output.append(Hellion)
    if rngPleaseFirst == 6:
        output.append(Ironclad)
    if rngPleaseFirst == 7:
        output.append(Nightbringer)
    if rngPleaseFirst == 8:
        output.append(Redeemed)
    if rngPleaseFirst == 9:
        output.append(Revenant)
    if rngPleaseFirst == 10:
        output.append(Sentinel)

    if rngPleaseFirst == 6 or rngPleaseFirst == 9:
        rngPleaseFirst = random.randrange(1, 21)
        if rngPleaseFirst == 1:
            output.append(Abomination)
        if rngPleaseFirst == 2:
            output.append(Dawnbringer)
        if rngPleaseFirst == 3:
            output.append(Draconic)
        if rngPleaseFirst == 4:
            output.append(Forgotten)
        if rngPleaseFirst == 5:
            output.append(Hellion)
        if rngPleaseFirst == 6:
            output.append(Nightbringer)
        if rngPleaseFirst == 7:
            output.append(Redeemed)
        if rngPleaseFirst == 8:
            output.append(Sentinel)
        if rngPleaseFirst == 9:
            output.append(Assassin)
        if rngPleaseFirst == 10:
            output.append(Brawler)
        if rngPleaseFirst == 11:
            output.append(Cannoneer)
        if rngPleaseFirst == 12:
            output.append(Cavalier)
        if rngPleaseFirst == 13: 
            output.append(Invoker)
        if rngPleaseFirst == 14:
            output.append(Knight)
        if rngPleaseFirst == 15:
            output.append(Legionnaire)
        if rngPleaseFirst == 16:
            output.append(Mystic)
        if rngPleaseFirst == 17:
            output.append(Ranger)
        if rngPleaseFirst == 18:
            output.append(Renewer)
        if rngPleaseFirst == 19:
            output.append(Skirmisher)
        if rngPleaseFirst == 20:
            output.append(Spellweaver)

#Classes
    if rngPleaseFirst == 11:
        output.append(Assassin)
    if rngPleaseFirst == 12:
        output.append(Brawler)
    if rngPleaseFirst == 13:
        output.append(Cannoneer)
    if rngPleaseFirst == 14:
        output.append(Cavalier)
    if rngPleaseFirst == 15: 
        output.append(Invoker)
    if rngPleaseFirst == 16:
        output.append(Knight)
    if rngPleaseFirst == 17:
        output.append(Legionnaire)
    if rngPleaseFirst == 18:
        output.append(Mystic)
    if rngPleaseFirst == 19:
        output.append(Ranger)
    if rngPleaseFirst == 20:
        output.append(Renewer)
    if rngPleaseFirst == 21:
        output.append(Skirmisher)
    if rngPleaseFirst == 22:
        output.append(Spellweaver)


    rngPleaseSecond = random.randrange(11,23)
    while rngPleaseSecond == rngPleaseFirst:
        rngPleaseSecond = random.randrange(11,23)

#Origins
    if rngPleaseSecond == 1:
        output.append(Abomination)
    if rngPleaseSecond == 2:
        output.append(Dawnbringer)
    if rngPleaseSecond == 3:
        output.append(Draconic)
    if rngPleaseSecond == 4:
        output.append(Forgotten)
    if rngPleaseSecond == 5:
        output.append(Hellion)
    if rngPleaseSecond == 6:
        output.append(Ironclad)
    if rngPleaseSecond == 7:
        output.append(Nightbringer)
    if rngPleaseSecond == 8:
        output.append(Redeemed)
    if rngPleaseSecond == 9:
        output.append(Revenant)
    if rngPleaseSecond == 10:
        output.append(Sentinel)


#Classes  
    if rngPleaseSecond == 11:
        output.append(Assassin)
    if rngPleaseSecond == 12:
        output.append(Brawler)
    if rngPleaseSecond == 13:
        output.append(Cannoneer)
    if rngPleaseSecond == 14:
        output.append(Cavalier)
    if rngPleaseSecond == 15: 
        output.append(Invoker)
    if rngPleaseSecond == 16:
        output.append(Knight)
    if rngPleaseSecond == 17:
        output.append(Legionnaire)
    if rngPleaseSecond == 18:
        output.append(Mystic)
    if rngPleaseSecond == 19:
        output.append(Ranger)
    if rngPleaseSecond == 20:
        output.append(Renewer)
    if rngPleaseSecond == 21:
        output.append(Skirmisher)
    if rngPleaseSecond == 22:
        output.append(Spellweaver)
    return output

def whatIsMyKing(x, y, z):
    king = ""
    originOrClass = random.randrange(0,2)
    if z[0] != "":
        y = z
    if originOrClass == 0:
        originEnd = len(x) # no need to + 1 because of the name at pos 0
        kingNumber = random.randrange(1, originEnd)
        king = x[kingNumber]

    if originOrClass == 1:
        classEnd = len(y)
        kingNumber = random.randrange(1, classEnd)
        king = y[kingNumber]
    return king

retard = True
while retard:
    try:
        numberOfPlayers = int(input("Enter the number of players: "))
        retard = False
    except ValueError:
        print("Are you special?")



people = []
for j in range(int(numberOfPlayers)):
    names = input("Enter player's name: ")
    people.append(names)

for k in people:
    storeTraits = whatTraits()
    Origin = storeTraits[0]
    Class = storeTraits[1]
    if len(storeTraits) >= 3:
        thirdOrigin = storeTraits[2]
    else:
        thirdOrigin = [""]
    print(k + ":", Origin[0], Class[0], thirdOrigin[0], "| Your King Is:", whatIsMyKing(Origin, Class, thirdOrigin))

reroll = "y"
while reroll == "y":
    reroll = input("Would you like to reroll y/n? ")
    if reroll != "y":
        break
    for k in people:
        storeTraits = whatTraits()
        Origin = storeTraits[0]
        Class = storeTraits[1]
        if len(storeTraits) >= 3:
            thirdOrigin = storeTraits[2]
        else:
            thirdOrigin = [""]
        print(k + ":", Origin[0], Class[0], thirdOrigin[0], "| Your King Is:", whatIsMyKing(Origin, Class, thirdOrigin))


