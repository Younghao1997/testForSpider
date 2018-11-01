# coding = "utf-8"
from lxml import etree
import unittest
from selenium import webdriver

class douYuSelenium(unittest.TestCase):
    def setUp(self):
        self.zhubo_num = 0
        self.zhubo_list = []
        self.driver = webdriver.PhantomJS()

    def testspiderdouyu(self):
        self.driver.get("https://www.douyu.com/directory/all")
        while True:
            selector = etree.HTML(self.driver.page_source)
            name_List = selector.xpath('//a[@class="play-list-link"]//span[@class="dy-name ellipsis fl"]')
            number_List = selector.xpath('//a[@class="play-list-link"]//span[@class="dy-num fr"]')
            for name,number in zip(name_List,number_List):
                if name not in self.zhubo_list:
                    self.zhubo_num += 1
                    print("直播间名：%s  -----观众数量：%s"%(name.text,number.text))
                    self.zhubo_list.append(name)

            if self.driver.page_source.find('shark-pager-disable-next') != -1:
                break

            self.driver.find_element_by_class_name('shark-pager-next').click()

    def tearDown(self):
        print('爬取完成...')
        print("斗鱼在线主播：%d位"%self.zhubo_num)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()