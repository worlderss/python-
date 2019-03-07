"""
爬取上海高院的数据
import requests

# headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
#                'Accept - Encoding':'gzip, deflate',
#                'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
#                'Connection':'Keep-Alive',
#                'Host':'zhannei.baidu.com',
#                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
# rep = requests.get('http://www.hshfy.sh.cn/shfy/gweb2017/ktgg_search.jsp',headers= headers)

# print(rep.text)
"""
import time

import selenium.webdriver

driver = selenium.webdriver.Chrome()
driver.get('http://www.hshfy.sh.cn/shfy/gweb2017/ktgg_search.jsp')
time.sleep(5)
print(driver.page_source)
js = 'javascript:goPage("2116")'
driver.execute_script(js)
time.sleep(5)
print(driver.page_source)
driver.quit()