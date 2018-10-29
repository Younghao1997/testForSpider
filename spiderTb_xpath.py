# coding=utf-8

from lxml import etree
import requests
import random


class SpiderTB_Xpath():
    ua_list = [
        "Mozilla/5.0 (Windows NT 6.1; ) Apple.... ",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0)... ",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X.... ",
        "Mozilla/5.0 (Macintosh; Intel Mac OS... "
    ]
    headers = {"headers": random.choice(ua_list)}
    url_base = "http://tieba.baidu.com/f?"
    url_base2 = "http://tieba.baidu.com"

    def visit(self, tb_name, page):
        '''
        作用: 返回一个response
        tb_name:贴吧名
        start_page:起始访问页
        end_page:结束访问页
        '''
        pn = (page-1)*50
        param_dict = {"kw": tb_name,"pn":pn}
        response = requests.get(self.url_base, params=param_dict, headers=self.headers)
        #print(response.text)
        html_text = response.text
        return html_text

    def textfilter(self,html_text):
        '''
        作用：文本过滤
        html: html页面文本
        '''
        #将文本转换为xml
        selector = etree.HTML(html_text)
        #选择需要的数据，过滤
        links = selector.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a[@class="j_th_tit "]/@href')
        return links
    def loadtext(self,links,url_base2):
        '''
        作用:进入对应楼层，访问数据
        links:楼层连接后缀
        url_base2:官网连接前缀
        '''
        for link in links:
            ba_url = url_base2 + link
            self.writetext(ba_url)

    def writetext(self,ba_url):
        '''
        作用：将贴吧数据写入到本地
        ba_url:楼层连接
        '''
        response = requests.get(ba_url,headers = self.headers)
        ba_html = response.text
        selector = etree.HTML(ba_html)
        text = selector.xpath('//div[@class="d_post_content j_d_post_content  clearfix"]/text()')
        filename = "江西理工大学南昌校区吧.txt"
        with open(filename,'a',encoding='utf-8') as f:
            f.write("*"*50)
            f.write("\n")
            for a in text:
                f.write(a)
                f.write("\n")



if __name__ == "__main__":
    tb_name = input("请输入你想逛的贴吧:")
    start_page = int(input("起始访问页(数字):"))
    end_page = int(input("结束访问页(数字):"))
    spider = SpiderTB_Xpath()
    for page in range(start_page,end_page+1):
        html_text = spider.visit(tb_name, page)
        links = spider.textfilter(html_text)
        spider.loadtext(links, spider.url_base2)
        print("第%d页打印完成！"%page)
