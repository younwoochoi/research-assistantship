import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy import Selector
from selenium import webdriver
import time
import re
infolst = []
usrlst = []
detail = []
dict = {}
class ProductSpider(scrapy.Spider):
    name = "product_spider"
    allowed_domains = ['na.op.gg']
    start_url= 'https://na.op.gg/summoner/userName=knitting+måster'

    def __init__(self):
        driver = webdriver.Chrome("/Users/younwoo/Downloads/chromedriver")
        driver.get(self.start_url)
        while True:
            #next = driver.find_element_by_xpath('//div[@class="GameMoreButton Box"]/a')
            #next2 = driver.find_elements_by_xpath('//a[@class="Button MatchDetail"]')

            try:
                next = driver.find_element_by_xpath('//div[@class="GameMoreButton Box"]/a')
                #next2 = driver.find_elements_by_xpath('//a[@class="Button MatchDetail"]')
                #for button in next2:
                    #time.sleep(1)
                    #button.click()
                
                #self.parse(driver.page_source)
                #for button in next2:
                    #time.sleep(1)
                    #button.click()
                next.click()
                time.sleep(2)
            except:
                break
        time.sleep(2)
        next2 = driver.find_elements_by_xpath('//a[@class="Button MatchDetail"]')
        
        for button in next2:
            button.click()
            time.sleep(1)
             
            
        self.parse(driver.page_source) 

        driver.close()

    def parse(self, body):
        sel = Selector(text=body)
        print(sel)
        time.sleep(1)
        game_result = sel.xpath("//div[@class='GameResult']/text()").extract()
        time.sleep(1)
        #user_name = sel.xpath("//tr[@class='Row first  isRequester']/td[@class='SummonerName Cell']/a/text()").extract()
        #usrlst.append(user_name)
        infolst.append(game_result)
        game_contents = sel.xpath("//tbody[@class='Content']")
        

        for game in game_contents:
            levels = game.xpath("//tr/td[contains(@class, 'Tier Cell')]/text()").extract()
            #for level in levels:
                
                #level = level.replace("\n", "")
                #level = level.replace("\t", "")
                #print(level)
            print(levels)
            #usrname = game.xpath('/tr[@class="Row first  isRequester"]/td[@class="SummonerName Cell"]/a/text()').extract()
            #print(usrname)
        #print(game_contents)
        #for game in game_contents:
            #usrlst.append(game)
            
            
        #xtract()
        #for game in game_detail:
            #if sel.xpath('/tr/@class').extract() == "Row first  isRequester":
                #name = sel.xpath('/tr[@class="Row first  isRequester"]/td[@class="SummonerName Cell"]/a/text()').extract()
                #detail.apeend(name)
    
        


        
        
        

process2 = CrawlerProcess()
process2.crawl(ProductSpider)
process2.start()
print(usrlst)
print(infolst)


