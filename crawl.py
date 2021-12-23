from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd
import random
try:
    driver = webdriver.Firefox()
    url = "https://u.gg/leaderboards/ranking?region=euw1"
    driver.get(url)
    time.sleep(5)
    p = 0
    i = -1

    while True:
        i += random.randint(1, 11) #increase players search number randomly (1-10)
        players_list = driver.find_elements(By.CLASS_NAME, "summoner") #get all players in page
        ads = driver.find_elements(By.ID, "desktop-anchor-close") #find ads
        if len(ads)>0:
            for k in range(len(ads)):
                ads[k].click() #close ad
        players_list[i].click() #enter player number i page
        time.sleep(5)
        players_stats = {} # stats dict
        #ranking
        rank = driver.find_element(By.CLASS_NAME, "rank-text").find_element(By.TAG_NAME, "strong").text  #get his ranking info
        players_stats["Rank"] = rank

        #stats page
        stats = driver.find_elements(By.CLASS_NAME, "nav-tab-link")
        stats[1].click() #get to stats page

        #w/r
        WinRate = driver.find_element(By.CLASS_NAME, "champion-rates") #w/r + games
        win_rate = WinRate.text.split("/")[0].split("%")[0] #w/r
        win = WinRate.text.split("/")[1].split("W")[0] #wins
        loss = WinRate.text.split("/")[1].split("W")[1].split("L")[0] #losses
        games = int(win)+int(loss)

        players_stats["WinRate"] = int(win_rate)
        players_stats["Games"] = games

        #kda
        kda_stats = driver.find_elements(By.CLASS_NAME, "kda")[0].find_elements(By.TAG_NAME, "strong")

        players_stats["KDA"] = float(kda_stats[0].text)
        players_stats["AVG_kills"] = float(kda_stats[1].text)
        players_stats["AVG_deaths"] = float(kda_stats[2].text)
        players_stats["AVG_assists"] = float(kda_stats[3].text)

        #cs
        players_stats["Creep_Score"] = float(driver.find_elements(By.CLASS_NAME, "cs-cell")[1].text)

        #damage
        dmg = driver.find_elements(By.CLASS_NAME, "damage-cell")[1].text.split(",")
        players_stats["Damage"] = int(dmg[0] + dmg[1])

        #gold
        gold = driver.find_elements(By.CLASS_NAME, "gold-cell")[1].text.split(",")
        players_stats["Gold"] = int(gold[0]+gold[1])

        #multi-kill
        players_stats["Multi_Kill"] = 0
        for i in range(4):
            if driver.find_elements(By.CLASS_NAME, "multikill-cell")[i+4].text != "—":
                players_stats["Multi_Kill"] += int(driver.find_elements(By.CLASS_NAME, "multikill-cell")[i+4].text)

        df = pd.DataFrame([players_stats])
        with open("Data.csv", "a") as file:
            df.to_csv(file, index=False, header=False)

        driver.back()
        time.sleep(5)
        driver.back()
        time.sleep(5)

        if i >= len(players_list): #check if done with page
            if p==0: #if first page
                driver.find_element(By.CLASS_NAME, "skip-to").click() #next page
            if p<=10:
                p += 1
            else:
                if p < 1000:
                    p += 500
                if p >= 1000 and p< 10000:
                    p+=1000
                if p >= 10000 and p< 20000:
                    p += 2000
                if p >= 20000 and p < 30000:
                    p += 3000
                if p >= 30000:
                    p+=4500
            driver.get(url+f"&page={p}")
            i = -1
            time.sleep(6)
        stop = driver.find_elements(By.CLASS_NAME, "content-section leaderboard_table_error") #check for no-content error (means we are overflowing players pages, no content left)
        if len(stop) > 0:
            break

    driver.close()

except Exception as e:
    print(f'crashed at {p}')