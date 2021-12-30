from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import datetime
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
### selenium set-up
driver = webdriver.Firefox()
url = "https://u.gg/leaderboards/ranking?region=euw1"
driver.get(url)
page = 0 #CHANGE TO CHANGE CRAWLING PAGE
time.sleep(5) #wait for the page to load
curr_player = -1
### end selenium set-up
while True:
    try:
        ### get player-list (in page)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "summoner")))
        curr_player += random.randint(1, 6) #increase players search number randomly (1-5)
        players_list = driver.find_elements(By.CLASS_NAME, "summoner") #get all players in page

        ### end get player-list
        ##deal with ads
        ads = driver.find_elements(By.ID, "desktop-anchor-close") #find ads
        if len(ads) > 0:
            for ad in range(len(ads)):
                ads[ad].click() #close ad
        ### end deal with ads

        ###enter player page
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

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "update-button"))) #wait for page to load
            rank = driver.find_element(By.CLASS_NAME, "rank-text").find_element(By.TAG_NAME, "strong").text  #get his ranking info
            players_stats["Rank"] = rank

            #stats page
            ### get his stats
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
            with open("Data3.csv", "a") as file:
                df.to_csv(file, index=False, header=False)

            driver.back()
            driver.back()
        #end player page, go to next player
        if curr_player >= len(players_list): #check if done with page
            if page <= 10:
                page += 1
            elif page <= 20:
                page += 2
            elif page <= 100:
                page += 4
            elif page <= 1000:
                page += 100
            elif page <= 10000:
                page += 150
            elif page <= 20000:
                page += 200
            else:
                page += 330

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")  # https://www.programiz.com/python-programming/datetime/current-time

            print(f"going to page {page} at {current_time}")
            driver.get(url+f"&page={page}")
            curr_player = -1

        if page >= 42000: #last page that has data
            print(f"Done with crawling {current_time}")
            break

    except Exception as e:
        time.sleep(5)
        driver.refresh()
        driver.back()
        time.sleep(1)
        continue
driver.close()
