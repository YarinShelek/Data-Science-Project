from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import datetime
import random
try:
    driver = webdriver.Firefox()
    url = "https://u.gg/leaderboards/ranking?region=euw1"
    driver.get(url)
    time.sleep(8) #wait for the page to load

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
            time.sleep(8) #wait for player page to load
            players_stats = {} # stats dict

            #check if u.gg is trolling us:
            player_not_found = driver.find_elements(By.CLASS_NAME, "white-bold")
            if player_not_found:
                if "Oh no! We couldn't find summoner" in player_not_found[0].text:
                    driver.back()
                    time.sleep(8)
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
            time.sleep(8)
            driver.back()
            time.sleep(8)

        if curr_player >= len(players_list): #check if done with page
            if page <= 10:
                page += 1
            elif page <= 1000:
                page += 500
            elif page <= 10000:
                page += 1000
            elif page <= 20000:
                page += 2000
            else:
                page += 3000

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")  # https://www.programiz.com/python-programming/datetime/current-time

            print(f"going to page {page} at {current_time}")
            driver.get(url+f"&page={page}")
            curr_player = -1
            time.sleep(8)

        stop = driver.find_elements(By.CLASS_NAME, "content-section leaderboard_table_error") #check for no-content error (means we are overflowing players pages, no content left)
        if stop:
            break

    driver.close()

except Exception as e:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f'crashed at page {page} at {current_time}')
