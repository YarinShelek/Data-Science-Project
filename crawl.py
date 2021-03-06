from selenium import webdriver # crawl bot
import time #for sleep
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import datetime # for us to keep track of crawl
import random # for random player select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re #to get only his rank namedo
import threading
import pyautogui
def dont_sleep():
    while True:
        time.sleep(5)
        pyautogui.moveTo(random.randint(1, 2000), random.randint(1, 2000))
        time.sleep(3)
        pyautogui.moveTo(random.randint(1, 2000), random.randint(1, 2000))
        time.sleep(7)
        pyautogui.moveTo(random.randint(1, 2000), random.randint(1, 2000))
def crawl(page):
### selenium set-up
    driver = webdriver.Firefox()
    url = f"https://u.gg/leaderboards/ranking?region=euw1&page={page}"
    driver.get(url)
    #page = 22 #CHANGE TO CHANGE CRAWLING PAGE
    time.sleep(5) #wait for the page to load
    curr_player = -1
    ### end selenium set-up

    while True:
        try:
            ### get player-list (in page)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "summoner")))
            curr_player += random.randint(1, 5) #increase players search number randomly (1-4)
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
                driver.find_element(By.CSS_SELECTOR, ".default-select__control.css-0").click()
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".default-select__control.css-0"))) #wait for page to load
                driver.find_element(By.CSS_SELECTOR, ".default-select__menu.css-l8xc29").click()
                time.sleep(1)
                rank = driver.find_element(By.CLASS_NAME, "rank-text").find_element(By.TAG_NAME, "strong").text  #get his ranking info
                rank_pattern = r"(\w*)\s?\d?" #we are using regex to find only the rank name, as some ranks appear as such: "RANK 1-4" (rank name, division number)
                players_stats["Rank"] = re.findall(rank_pattern, rank)[0]

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
                    time.sleep(6) #wait for page to load. as this happens VERY rarely and in uncertain situations, we will not be using explicit waits here.
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
                    if driver.find_elements(By.CLASS_NAME, "multikill-cell")[kill+4].text != "???": #needs to be kill+4
                        multis = driver.find_elements(By.CLASS_NAME, "multikill-cell")[kill+4].text
                        if len(multis) > 3:
                            multis = multis.split(",")
                            multis = int(multis[0]+multis[1])
                        players_stats["Multi_Kill"] += int(multis)
                df = pd.DataFrame([players_stats])
                with open("DataFromCrawl.csv", "a") as file:
                    df.to_csv(file, index=False, header=False)

                driver.back()
                driver.back()
            #end player page, go to next player
            if curr_player >= len(players_list): #check if done with page
                if page <= 10:
                    page += 1
                elif page <= 20:
                    page += 3
                elif page <= 100:
                    page += 10
                elif page <= 1000:
                    page += 150
                elif page <= 10000:
                    page += 200
                elif page <= 20000:
                    page += 300
                elif page >= 41500:
                    page += 50
                else:
                    page += 400

                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")  # https://www.programiz.com/python-programming/datetime/current-time

                print(f"going to page {page} at {current_time}")
                driver.get(url+f"https://u.gg/leaderboards/ranking?region=euw1&page={page}")
                curr_player = -1

            if page >= 42000 or (page<=14000 and page>=1000) : #last page that has data
                print(f"Done with crawling {current_time}")
                break

        except Exception as e:
            time.sleep(5)
            driver.get(f"https://u.gg/leaderboards/ranking?region=euw1&page={page}")
            continue
    driver.close()
if __name__ == "__main__":
    t1 = threading.Thread(target=crawl, args=[37800])
    t2 = threading.Thread(target=dont_sleep)

    t1.start()
    t2.start()

