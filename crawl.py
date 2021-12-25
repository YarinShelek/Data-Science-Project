from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd
import random
try:
    driver = webdriver.Firefox()
    url = "https://u.gg/leaderboards/ranking?region=euw1"
    driver.get(url)
    time.sleep(5) #wait for the page to load

    page = 0
    curr_player = -1

    while True:
        curr_player += random.randint(1, 11) #increase players search number randomly (1-10)
        players_list = driver.find_elements(By.CLASS_NAME, "summoner") #get all players in page
        ads = driver.find_elements(By.ID, "desktop-anchor-close") #find ads
        if len(ads) > 0:
            for ad in range(len(ads)):
                ads[ad].click() #close ad
        if curr_player < len(players_list):
            players_list[curr_player].click() #enter player number i page
            time.sleep(5) #wait for player page to load
            players_stats = {} # stats dict

            #check if u.gg is trolling us:
            player_not_found = driver.find_element(By.CLASS_NAME, "white-bold").text
            if "Oh no! We couldn't find summoner" in player_not_found:
                continue

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
            for kill in range(4): #combine the 4 multi kill types into 1 multi-kill
                if driver.find_elements(By.CLASS_NAME, "multikill-cell")[kill+4].text != "—": #needs to be kill+4
                    players_stats["Multi_Kill"] += int(driver.find_elements(By.CLASS_NAME, "multikill-cell")[kill+4].text)

            df = pd.DataFrame([players_stats])
            with open("Data.csv", "a") as file:
                df.to_csv(file, index=False, header=False)

            driver.back()
            time.sleep(5)
            driver.back()
            time.sleep(5)

        if curr_player >= len(players_list): #check if done with page
            if page == 0: #if first page
                driver.find_element(By.CLASS_NAME, "skip-to").click() #next page
            if page <= 10:
                page += 1
            else:
                if page < 1000:
                    page += 500
                if 1000 <= page < 10000:
                    page += 1000
                if 10000 <= page < 20000:
                    page += 2000
                if page >= 20000:
                    page += 3000

            driver.get(url+f"&page={page}")
            curr_player = -1
            time.sleep(6)
        stop = driver.find_elements(By.CLASS_NAME, "content-section leaderboard_table_error") #check for no-content error (means we are overflowing players pages, no content left)
        if len(stop) > 0:
            break

    driver.close()

except Exception as e:
    print(f'crashed at page {page}')
