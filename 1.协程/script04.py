import time
import urllib
import gevent.monkey
import selenium.webdriver
from bs4 import BeautifulSoup
import pandas as pd

gevent.monkey.patch_all()

out_df =[]
def download( url ,start,end):
    driver = selenium.webdriver.Chrome()
    driver.get(url)
    # print(driver.page_source)
    for i in range(start,end):
        js = 'javascript:goPage("'+str(i)+'")'
        driver.execute_script(js)

        time.sleep(10)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')
        table = soup.find("table", attrs={'id': 'report'})
        trs = table.find_all("tr")
        lsts = []
        for tr in trs:
            tds = tr.find_all('td')
            lst = []
            for td in tds:
                lst.append(td.text)
            lsts.append(lst)
        col = lsts[0]
        lsts = lsts[1:]
        df = pd.DataFrame(lsts)
        df.columns = col
        out_df.append(df)
    driver.quit()


gevent.joinall([
    gevent.spawn(download,'http://www.hshfy.sh.cn/shfy/gweb2017/ktgg_search.jsp',1,3),
    gevent.spawn(download,'http://www.hshfy.sh.cn/shfy/gweb2017/ktgg_search.jsp',3,5),

])


df = pd.concat(out_df,axis=0)
df.to_csv('1231.csv')