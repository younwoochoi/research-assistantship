import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy import Selector
from selenium import webdriver
import time
import re
import csv
import pandas as pd
from pathlib import Path
import numpy as np

path= Path("ingameid3.csv")
df= pd.read_csv(path)
urls = df['opgg_url'].tolist()


class ProductSpider(scrapy.Spider):
    name = "product_spider"
    allowed_domains = ['op.gg']

    
    
    start_urls= urls
    
        

    def __init__(self):
        self.driver = webdriver.Chrome("/Users/younwoo/Downloads/chromedriver_89")
        self.driver.maximize_window()
    
    def parse(self, response):
        i = 0
        self.driver.get(response.url)

        while True and i < 7:

            try:
                next = self.driver.find_element_by_xpath('//div[@class="GameMoreButton Box"]/a')
                
                next.click()
                time.sleep(3)
                i += 1
            except:
                break
        
        next2 = self.driver.find_elements_by_xpath('//a[@class="Button MatchDetail"]')
        
        
        for button in next2:
            
            button.click()
            
            time.sleep(1)
        next3 = self.driver.find_elements_by_xpath('//li[@data-tab-show-class="MatchDetailContent-teamAnalysis"]//a')
        
        for button in next3:
            
            button.click()
            
            time.sleep(1) 

        next4 = self.driver.find_elements_by_xpath('//li[@data-tab-show-class="TeamAnalysis-TeamTimeLine"]//a')
        
        for button in next4:
            
            button.click()
            
            time.sleep(1)


        self.parse2(self.driver.page_source) 

    def parse2(self, body):
        sel = Selector(text=body)
        
        time.sleep(1)

        game_lists = sel.xpath("//div[@class='GameItemList']")
        
        usrname = sel.xpath("//div[@class='Profile']/div[@class='Information']/span/text()").extract()
        
        for i in range(len(game_lists)):
            game_items = sel.xpath("//div[@class='GameItemList'][{0}]//div[@class = 'GameItemWrap']".format(i+1))
            for j in range(len(game_items)):
                path = "//div[@class='GameItemList'][{0}]//div[@class = 'GameItemWrap'][{1}]".format(i+1, j+1)
                date = sel.xpath("//div[@class='GameItemList'][{0}]//div[@class = 'GameItemWrap'][{1}]//span[@class='_timeago _timeCountAssigned tip']/@title".format(i+1, j+1)).extract()
                players = sel.xpath(path + "//tr[contains(@class, 'Row')]/td[@class='SummonerName Cell']/a/text()").extract()
                game_id = sel.xpath(path + "//div[contains(@class, 'GameItem')]/@data-game-id").extract()
                game_summary = game_id + date + usrname + players
                timelines = sel.xpath(path + "//li[contains(@class, 'Result-')]")
                
                timeline = []
                kills = [0, 0, 0, 0, 0]
                deaths = [0, 0, 0, 0, 0]

                for k in range(len(timelines)):
                    
                    
                    path_2 = path + "//li[contains(@class, 'Result-')][{0}]".format(k+1)
                    
                    who = sel.xpath(path_2 + "//span[1]/text()").extract()
                    what = sel.xpath(path_2 + "//b/text()").extract()
                    whom = sel.xpath(path_2 + "//span[2]/text()").extract()
                    
                    if len(whom) >= 1:
                        if str(who[0]) == str(usrname[0]) and str(what[0]) == 'Killed':
                            if str(whom[0]) == str(players[5]):
                                kills[0] += 1
                            elif str(whom[0]) == str(players[6]):
                                kills[1] += 1
                            elif str(whom[0]) == str(players[7]):
                                kills[2] += 1
                            elif str(whom[0]) == str(players[8]):
                                kills[3] += 1
                            elif str(whom[0]) == str(players[9]):
                                kills[4] += 1
                        elif str(who[0]) == str(players[5]) and str(whom[0]) == usrname[0] and str(what[0]) == 'Killed':
                            deaths[0] += 1
                        elif str(who[0]) == str(players[6]) and str(whom[0]) == usrname[0] and str(what[0]) == 'Killed':
                            deaths[1] += 1
                        elif str(who[0]) == str(players[7]) and str(whom[0]) == usrname[0] and str(what[0]) == 'Killed':
                            deaths[2] += 1
                        elif str(who[0]) == str(players[8]) and str(whom[0]) == usrname[0] and str(what[0]) == 'Killed':
                            deaths[3] += 1
                        elif str(who[0]) == str(players[9]) and str(whom[0]) == usrname[0] and str(what[0]) == 'Killed':
                            deaths[4] += 1

                    
                    
                timeline.extend(kills) 
                timeline.extend(deaths)
                game_summary.append(timeline)
                print(game_summary)
                
               
                
                with open('timeline_output.csv', 'a') as f:
                    wr = csv.writer(f)
                    wr.writerow(game_summary)





                
        
        


        

process2 = CrawlerProcess()
process2.crawl(ProductSpider)
process2.start()



