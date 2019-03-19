import random
import time
from functools import reduce

import redis
import requests
from lxml import etree

from 代理池创建.redis_存储模块 import redis_client


class Crawler(object):

    def get_proxies(self,callback):
        proxies=[]
        for proxy in eval("self."+callback+"()"):
            proxies.append(proxy)
        return proxies

    def crawl_daili66(self,pagecount=1):
        start_url ='http://www.66ip.cn/{}.html'
        urls =[start_url.format(i) for i in range(1,pagecount+1,1)]
        for url in urls:
            r = requests.get(url)
            page = r.content.decode('gbk')
            tree = etree.HTML(page)
            ip = tree.xpath('*//table[@bordercolor="#6699ff"]//tr//td[1]/text()')
            port = tree.xpath('*//table[@bordercolor="#6699ff"]//tr//td[2]/text()')
            ip = ip[1:]
            port = port[1:]
            proxy = [i[0] + ':' + i[1] for i in zip(ip, port)]
            for x in proxy:
                yield x

    def crawl_proxy360(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063',
        }
        start_url='http://www.goubanjia.com/'
        r = requests.get(start_url,headers=headers)
        page = r.content.decode('utf-8')
        tree = etree.HTML(page)
        for i in range(1, 21):
            try:
                ip = tree.xpath('*//tr['+str(i)+']/td[@class="ip"]//*[not(contains(@style,"none")) or not(@style)]/text()')
                ip = ip[:-1]+[':']+[ip[-1]]
                ip= reduce(lambda x,y:x+y,ip)
                type= tree.xpath('*//tr['+str(i)+']/td[2]//a/text()')[0]
                if type== '高匿':
                    yield ip
                else:
                    continue
            except:
                continue

    def get_the_funcs(self):
        return (list(filter(lambda m: m.startswith("crawl_") and callable(getattr(self, m)),dir(self))))

POOL_UPPER_THRESHOLD = 10000


class Getter():
    def __init__(self):
        self.redis =redis_client()
        self.crawler = Crawler()

    def is_over_threshold(self):
        if self.redis.get_proxy_count() >=POOL_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        if not self.is_over_threshold():
            for callback_label in self.crawler.get_the_funcs():
                proxies = self.crawler.get_proxies(callback_label)
                for proxy in proxies:
                    self.redis.add(proxy)

if __name__ == '__main__':
    while True:
        getter = Getter()
        getter.run()
        time.sleep(random.random())



