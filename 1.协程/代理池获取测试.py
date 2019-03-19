
import requests
from lxml import etree

headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
}
proxies = {
    "http": "http://39.134.65.206:8080",
    # "https": "https://221.228.17.172:8181",
}
r= requests.get('http://www.66ip.cn/2.html',headers=headers,proxies=proxies)
page = r.content.decode('gbk')
tree = etree.HTML(page)
ip = tree.xpath('*//table[@bordercolor="#6699ff"]//tr//td[1]/text()')
port = tree.xpath('*//table[@bordercolor="#6699ff"]//tr//td[2]/text()')
ip = ip[1:]
port = port[1:]

proxy= [i[0]+':'+i[1] for i in zip(ip,port)]

print(proxy)