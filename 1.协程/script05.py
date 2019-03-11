import time

import gevent.monkey
import requests
import chardet
import pandas as pd
from lxml import etree
# gevent.monkey.patch_all()
"""
    strs = etree.tostring(tree,encoding='gbk').decode('gbk') # 不能正常显示中文
"""


def get_page_num(url):
    page = requests.get(url + '?page=' + str(0)).content.decode('gbk')
    tree = etree.HTML(page)
    tree = tree.xpath('*//div[@class="pagination"]//a/@href')[-1].split('?page=')[1]
    return int(tree)

def get_urls(url,start_num):
    path=''
    try:
        page = requests.get(url+'?page='+str(start_num)).content.decode('GB18030')
    except:
        return [[str(start_num)+'failled!!',str(start_num)+'failled']]
    tree = etree.HTML(page)
    hrefs = tree.xpath('*//tr/td[2]/a[2]/@href')
    texts = tree.xpath('*//tr/td[2]/a[2]/@title')
    try:
        result = [[hrefs[i],texts[i]] for i in range(len(hrefs))]
    except:
        result = [[str(start_num) + 'failled!!', str(start_num) + 'failled']]

    return result
# *//li[@class="sort_div "]//a


def do_job(i):
    lst= []
    for j in i[:100]:
        temp_list = get_urls('http://wz.sun0769.com/index.php/question/report', j)
        lst += temp_list
    df = pd.DataFrame(lst)
    df.columns = ['href', 'text']
    df.to_csv(str(i[0])+'_123123.csv')


if __name__ == '__main__':
    a = get_page_num('http://wz.sun0769.com/index.php/question/report')
    the_source = list(range(0,a+1,30))
    half_source =int(len(the_source)/4)+1
    l =[the_source[i:i + half_source] for i in range(0, len(the_source), half_source)]
    do_job(l[3])
    # gevent.joinall([
    #     gevent.spawn(do_job, l[0]),
    #     gevent.spawn(do_job, l[1]),
    #     gevent.spawn(do_job, l[2]),
    #     gevent.spawn(do_job, l[3]),
    # ])


