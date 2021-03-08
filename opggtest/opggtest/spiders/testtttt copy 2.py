import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy import Selector
from selenium import webdriver
import time
import re
import csv


class ProductSpider(scrapy.Spider):
    name = "product_spider"
    allowed_domains = ['op.gg']


    start_urls= ["https://www.op.gg/summoner/userName=캬일",
    "https://www.op.gg/summoner/userName=세체우","https://www.op.gg/summoner/userName=Youtube귀배","https://www.op.gg/summoner/userName=현+솔"]
        

    def __init__(self):
        self.driver = webdriver.Chrome("/Users/younwoo/Downloads/chromedriver")
    
    def parse(self, response):
        i = 0
        self.driver.get(response.url)

        while True and i < 3:

            try:
                next = self.driver.find_element_by_xpath('//div[@class="GameMoreButton Box"]/a')
                
                next.click()
                time.sleep(5)
                i += 1
            except:
                break
        time.sleep(3)
        next2 = self.driver.find_elements_by_xpath('//a[@class="Button MatchDetail"]')
        
        for button in next2:
            button.click()
            time.sleep(3)
             
            
        self.parse2(self.driver.page_source) 

        

       # self.driver.close()

    

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
                champion = sel.xpath(path + "//div[@class ='Content']//div[@class ='ChampionName']/a/text()").extract()
                result = sel.xpath(path + "//div[@class='GameStats']/div[@class='GameResult']/text()").extract()
                kda = sel.xpath(path + "//div[@class ='Content']//div[@class='KDARatio']/span/text()").extract()
                game_type = sel.xpath(path + "//div[@class ='Content']//div[@class = 'GameType']/text()").extract()
                rank = sel.xpath(path + "//tr[contains(@class, 'isRequester')]/td[contains(@class, 'Tier Cell')]/text()").extract()
                players = sel.xpath(path + "//tr[contains(@class, 'Row')]/td[@class='SummonerName Cell']/a/text()").extract()
                t1_t2_baron = sel.xpath(path + "//div[@class='Summary']//div[@class='ObjectScore'][1]/text()").extract()
                t1_t2_drag = sel.xpath(path + "//div[@class='Summary']//div[@class='ObjectScore'][2]/text()").extract()
                t1_t2_towers = sel.xpath(path + "//div[@class='Summary']//div[@class='ObjectScore'][3]/text()").extract()
                t1_kills_totalGold = sel.xpath(path + "//div[@class='Summary']/div[@class='summary-graph']//div[@class='text graph--data graph--data__left']/text()").extract()
                t2_kills_totalGold = sel.xpath(path + "//div[@class='Summary']/div[@class='summary-graph']//div[@class='text graph--data graph--data__right']/text()").extract()
                game_length = sel.xpath(path + "//div[@class='GameLength']/text()").extract()

                game_summary = usrname+date+champion+result+kda+game_type+rank+players+t1_t2_baron+t1_t2_drag+t1_t2_towers+t1_kills_totalGold+t2_kills_totalGold+game_length
                print(game_summary)
                
                with open('outputs4.csv', 'a') as f:
                    wr = csv.writer(f)
                    wr.writerow(game_summary)





                
        
        


        
        
        

process2 = CrawlerProcess()
process2.crawl(ProductSpider)
process2.start()



