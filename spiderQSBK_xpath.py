# coding = "utf-8"
'''
    url:https://www.qiushibaike.com/8hr/page/1/
    使用requests获取页面信息，用XPath / re 做数据提取
    获取每个帖子里的用户头像链接、用户姓名、段子内容、点赞次数和评论次数
    保存到 json 文件内
'''
import requests
import json
from lxml import etree

class SpiderQSBK_xpath():
    headers = {"header":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36"}
    url_base = "https://www.qiushibaike.com/8hr/page/1/"

    def visit(self):
        response = requests.get(self.url_base,headers = self.headers)
        html = response.text
        selector = etree.HTML(html)
        data_list = selector.xpath('//div[contains(@id,"qiushi_tag")]')
        #print(len(data_list))
        for site in data_list:
            item = {}
            #用户头像链接：//div[contains(@id,'qiushi_tag')]/div/a[contains(@href,'/users/')]/@href
            imgUrl = site.xpath('./div/a[contains(@href,"/users/")]/@href')[0]
            #用户名：//div[contains(@id,'qiushi_tag')]/div/a/h2
            username = site.xpath('./div/a/h2')[0].text
            # username = site.xpath('.//h2')[0].text
            #内容：//div[contains(@id,'qiushi_tag')]//div[@class="content"]/span
            content = site.xpath('.//div[@class="content"]/span')[0].text
            # 投票次数://div[contains(@id,'qiushi_tag')]//span[@class='stats-vote']/i
            vote = site.xpath('.//span[@class="stats-vote"]/i')[0].text
            # print site.xpath('.//*[@class="number"]')[0].text
            # 评论次数：//div[contains(@id,'qiushi_tag')]//span[@class="stats-comments"]//i
            comments = site.xpath('.//span[@class="stats-comments"]//i')[0].text
            data_dict = {
                "imgUrl":imgUrl,
                "username":username,
                "content":content,
                "vote":vote,
                "comments":comments
            }
            with open("qsbk_json.json",'ab') as f:
                f.write(json.dumps(data_dict,ensure_ascii=False).encode("utf-8")+b"\n")

if __name__ == "__main__":
    spider = SpiderQSBK_xpath()
    spider.visit()
