from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import datetime
import random
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
try:
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    url = "https://u.gg/leaderboards/ranking?region=euw1"
    url = "https://u.gg/leaderboards/ranking?region=euw1&page=2214" #CHANGE TO CHANGE CRAWLING PAGE
    page = 2214 #CHANGE TO CHANGE CRAWLING PAGE
    driver.get(url)
    time.sleep(10) #wait for the page to load
    data = 0
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
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "flex-center"))) #wait for page to load
            #^^from selenium docs, "how to use explicit wait", wait for element to load... is said to be faster than time.sleep()
            players_stats = {} # stats dict

            #check if u.gg is trolling us:
            player_not_found = driver.find_elements(By.CLASS_NAME, "white-bold")
            if player_not_found:
                if "Oh no! We couldn't find summoner" in player_not_found[0].text:
                    driver.back()
                    time.sleep(10)
                    continue
            rank = driver.find_element(By.CLASS_NAME, "rank-text").find_element(By.TAG_NAME, "strong").text
            if rank == "Unranked":
                driver.find_element(By.CLASS_NAME, "flex-center").click() #update the rank
                time.sleep(10)
                rank = driver.find_element(By.CLASS_NAME, "rank-text").find_element(By.TAG_NAME, "strong").text  #get his ranking info
            else:
                players_stats["Rank"] = rank
            #ranking

            #stats page
            stats = driver.find_elements(By.CLASS_NAME, "nav-tab-link")
            stats[1].click() #get to stats page
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "champion-rates"))) #wait for page to load
            ads = driver.find_elements(By.ID, "desktop-anchor-close") #find ads
            if len(ads) > 0:
                for ad in range(len(ads)):
                    ads[ad].click()
            #w/r
            WinRate = driver.find_elements(By.CLASS_NAME, "champion-rates") #w/r + games
            if len(WinRate) > 0:
                win_rate = WinRate[0].text.split("/")[0].split("%")[0] #w/r
                win = WinRate[0].text.split("/")[1].split("W")[0] #wins
                loss = WinRate[0].text.split("/")[1].split("W")[1].split("L")[0] #losses
                games = int(win)+int(loss)
                players_stats["WinRate"] = int(win_rate)
                players_stats["Games"] = games
            else: #player has the weird no-info bug on his stat page (very rare, happened once in many players we checked)
                driver.back()
                driver.back()
                time.sleep(10) #wait for page to load. as this happens VERY rarely and in uncertain situations, we will not be using explicit waits here.
                continue
            #kda
            kda_stats = driver.find_elements(By.CLASS_NAME, "kda")[0].find_elements(By.TAG_NAME, "strong")
            players_stats["KDA"] = float(kda_stats[0].text)
            players_stats["AVG_kills"] = float(kda_stats[1].text)
            players_stats["AVG_deaths"] = float(kda_stats[2].text)
            players_stats["AVG_assists"] = float(kda_stats[3].text)
            #cs
            players_stats["Creep_Score"] = float(driver.find_elements(By.CLASS_NAME, "cs-cell")[1].text)

            #damage
            dmg = driver.find_elements(By.CLASS_NAME, "damage-cell")[1].text
            if "," in dmg:
                dmg = dmg.split(",")
                players_stats["Damage"] = int(dmg[0] + dmg[1])
            else:
                players_stats["Damage"] = int(dmg) #apparently some ppl have below 1k dmg/gold per game. we won't be using them, but need to filter them to not crash the crawling.
            #gold
            gold = driver.find_elements(By.CLASS_NAME, "gold-cell")[1].text
            if "," in gold:
                gold = gold.split(",")
                players_stats["Gold"] = int(gold[0]+gold[1])
            else:
                gold = int(gold)
            #multi-kill
            players_stats["Multi_Kill"] = 0

            for kill in range(4): #combine the 4 multi kill types into 1 multi-kill
                if driver.find_elements(By.CLASS_NAME, "multikill-cell")[kill+4].text != "—": #needs to be kill+4
                    multis = driver.find_elements(By.CLASS_NAME, "multikill-cell")[kill+4].text
                    if len(multis) > 3:
                        multis = multis.split(",")
                        multis = int(multis[0]+multis[1])
                    players_stats["Multi_Kill"] += int(multis)

            df = pd.DataFrame([players_stats])
            data += 1
            with open("Data.csv", "a") as file:
                df.to_csv(file, index=False, header=False)

            driver.back()
            driver.back()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "summoner")))

        if curr_player >= len(players_list): #check if done with page
            if page <= 20:
                page += 1
            elif page <= 100:
                page += 6
            elif page <= 1000:
                page += 112
            elif page <= 10000:
                page += 202
            elif page <= 20000:
                page += 452
            else:
                page += 666

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")  # https://www.programiz.com/python-programming/datetime/current-time

            print(f"going to page {page} at {current_time}, currently have {data*11} data")
            driver.get(url+f"&page={page}")
            curr_player = -1
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "summoner")))

        stop = driver.find_elements(By.CLASS_NAME, "content-section leaderboard_table_error") #check for no-content error (means we are overflowing players pages, no content left)
        if stop != []:
            break

    driver.close()

except Exception as e:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f'crashed at page {page} at {current_time} with {data*11} data\n Cause of crash: {e}')
