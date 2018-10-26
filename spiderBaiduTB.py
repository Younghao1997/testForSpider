# coding=utf-8
import urllib2
import urllib
import random

ua_list = [
    "Mozilla/5.0 (Windows NT 6.1; ) Apple.... ",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0)... ",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X.... ",
    "Mozilla/5.0 (Macintosh; Intel Mac OS... "
]
# https://tieba.baidu.com/f?kw=lol&pn=0
'''
ua_header = random.choice(ua_list)
request1 = urllib2.Request("http://www.baidu.com/")
request1.add_header("User-Agent",ua_header)
response1 = urllib2.urlopen(request1)
print response1.read()
'''
kw = raw_input("请输入需要爬去的贴吧名:")
start_page = int(raw_input("爬取开始的页码:"))
end_page = int(raw_input("爬取结束的页码:"))

url_base = 'https://tieba.baidu.com/f?'
new_kw = urllib.urlencode({'kw': kw})
for page in range(start_page, end_page + 1):
    pn = (page - 1) * 50
    ua_header = random.choice(ua_list)
    url1 = url_base + new_kw + '&' + 'pn=' + str(pn)
    request1 = urllib2.Request(url1)
    request1.add_header("User-Agent", ua_header)
    response1 = urllib2.urlopen(request1)
    filename = kw+"吧第"+str(page) + "页.html"
    with open(filename.decode("utf-8"), "w") as f:
        f.write(response1.read())
    print '爬取完成！'