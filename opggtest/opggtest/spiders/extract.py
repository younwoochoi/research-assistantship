import pandas as pd
from pathlib import Path
path = Path('output.csv')
df = pd.read_csv(path)

class extract:
    
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
                rank = sel.xpath(path + "//tr[contains(@class, 'isRequester')]/td[@class='Tier Cell']/text()").extract()
                players = sel.xpath(path + "//tr[contains(@class, 'Row')]/td[@class='SummonerName Cell']/a/text()").extract()
                t1_t2_baron = sel.xpath(path + "//div[@class='Summary']//div[@class='ObjectScore'][1]/text()").extract()
                t1_t2_drag = sel.xpath(path + "//div[@class='Summary']//div[@class='ObjectScore'][2]/text()").extract()
                t1_t2_towers = sel.xpath(path + "//div[@class='Summary']//div[@class='ObjectScore'][3]/text()").extract()
                t1_kills_totalGold = sel.xpath(path + "//div[@class='Summary']/div[@class='summary-graph']//div[@class='text graph--data graph--data__left']/text()").extract()
                t2_kills_totalGold = sel.xpath(path + "//div[@class='Summary']/div[@class='summary-graph']//div[@class='text graph--data graph--data__right']/text()").extract()
                game_length = sel.xpath(path + "//div[@class='GameLength']/text()").extract()
                op_socres = sel.xpath(path + "//div[contains(@class, 'OPScore Text')]/text()").extract()
                op_rankings = sel.xpath(path + "//div[contains(@class, 'OPScore Badge')]/text()").extract()
                kdas = sel.xpath(path + "//span[contains(@class, 'KDARatio')]/text()").extract()

                game_id = sel.xpath(path + "//div[contains(@class, 'GameItem')]/@data-game-id").extract()
                
                game_summary = usrname+date+champion+result+kda+game_type+rank+players+t1_t2_baron+t1_t2_drag+t1_t2_towers+t1_kills_totalGold+t2_kills_totalGold+game_length+op_socres+op_rankings+kdas +game_id
                
                timelines = sel.xpath(path + "//li[contains(@class, 'Result-')]")
                
                timeline = []
                for k in range(len(timelines)):
                    info = self.extract_timeline(path, sel, k)
                    timeline.append(info)

                game_summary.append(timeline)

                with open('output.csv', 'a') as f:
                    wr = csv.writer(f)
                    wr.writerow(game_summary)
        
    def extract_timeline(self, path, sel, k):
        path_2 = path + "//li[contains(@class, 'Result-')][{0}]".format(k+1)
        when = sel.xpath(path_2 + "//div[@class='Time']/text()").extract()
        who = sel.xpath(path_2 + "//span[1]/text()").extract()
        what = sel.xpath(path_2 + "//b/text()").extract()
        whom = sel.xpath(path_2 + "//span[2]/text()").extract()
        return when + who + what + whom
