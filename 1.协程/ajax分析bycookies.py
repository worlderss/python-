from lxml import etree

from requests.cookies import RequestsCookieJar
import requests

session = requests.session()
cookiestr='ispass=false;RoneUserName=150109'

cookie_jar = RequestsCookieJar()
for i in cookiestr.split(';'):
    key = i.split('=')[0].strip()
    val = i.split('=')[1].strip()
    cookie_jar.set(key,val)

headers={
    'Host': 'ics.chinasoftosg.com',
    'Connection': 'keep-alive',
    'Content-Length': '103',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://ics.chinasoftosg.com',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://ics.chinasoftosg.com/SignOnServlet',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,und;q=0.8',
}
datastr= 'userid=150109&linkpage=&userName=150109&j_username=150109&password=gllg19950619&j_password=gllg19950619'
data={}


for i in datastr.split('&'):
    key = i.split('=')[0].strip()
    val = i.split('=')[1].strip()
    data[key]= val
session.cookies = cookie_jar
print(session.cookies)
print('######################')
rsp= session.post(url='http://ics.chinasoftosg.com/login',data=data,headers=headers)
print(session.cookies)
print('######################')
session.cookies.update(rsp.cookies)
a= (rsp.cookies.get_dict())
path = a['portal_presuuid']
url = 'http://ics.chinasoftosg.com/page?presuuid='+path
headers={
    'Host': 'ics.chinasoftosg.com',
    'Proxy-Connection': 'keep-alive',
    # 'Content-Length': '103',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://ics.chinasoftosg.com',
    'Upgrade-Insecure-Requests': '1',
    # 'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://ics.chinasoftosg.com/SignOnServlet',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,und;q=0.8',
}
rsp= session.get(url=url,headers=headers)
print(session.cookies)
print('######################')
url ='http://kq.chinasoftosg.com:8000/workAttendance/loginAction'
session.cookies.update(rsp.cookies)
rsp = session.get(url=url,headers=headers)
# print(rsp.text)
print(session.cookies.get_dict())
print('######################')
b= session.cookies.get_dict()['huaweielbsession']
c= session.cookies.get_dict()['ROLTPAToken']
d =session.cookies.get_dict()['JSESSIONID']
cookie_jar = RequestsCookieJar()
print(b,c,d)
cookie_jar.set('huaweielbsession',b,domain='kq.chinasoftosg.com')
cookie_jar.set('ROLTPAToken',c,domain='kq.chinasoftosg.com')
cookie_jar.set('JSESSIONID',d,domain='kq.chinasoftosg.com')

#session.cookies=(cookie_jar)
headers={
'Host': 'kq.chinasoftosg.com:8000',
'Content-Length': '44',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Origin': 'http://kq.chinasoftosg.com:8000',
'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded',
'Referer': 'http://kq.chinasoftosg.com:8000/workAttendance/monthgatherListAction_toPersonalMonthGather',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,und;q=0.8',

}
url ='http://kq.chinasoftosg.com:8000/workAttendance/monthgatherListAction_selectPersonalMonthGather'
data={
    'monthGrather.page': '1',
    'monthGrather.pagesize':10,
}
cookiestr='JSESSIONID=B924B02D38BFDF11FD60EF30A37A0465; huaweielbsession=84b7ad8160ae2ae19e7c11ee78a29596; ROLTPAToken=PExUUEFUb2tlbj48bm9kZT5SMUZyYW1ld29yazQuMDwvbm9kZT48dGltZT4xNTUyNTc1NzczODU1PC90aW1lPjx1c2VyaWQ%2BMTUwMTA5PC91c2VyaWQ%2BPHBlcnNvbnV1aWQ%2BNDAyODgxYzQ2NGQ2MTJlNDAxNjRkNjEzMmUxZDAxMWI8L3BlcnNvbnV1aWQ%2BPHN5c2lkPjI8L3N5c2lkPjwvTFRQQVRva2VuPg%3D%3D'
cookie_jar = RequestsCookieJar()
# cookiestr = ''
for i in cookiestr.split(';'):
    key = i.split('=')[0].strip()
    val = i.split('=')[1].strip()
    cookie_jar.set(key,val)
session.cookies=cookie_jar
print(session.cookies)
rsp = session.post(url=url,data=data,headers=headers)
print(rsp.json())
print(session.cookies)
print('######################')
# rsp = session.get(url='http://kq.chinasoftosg.com:8000/workAttendance/loginAction')
# data = 'importsExamineVo.page=1&importsExamineVo.pagesize=25'
# rsp = session.post(url='http://kq.chinasoftosg.com:8000/workAttendance/loginAction',data=data,headers=headers)
# print(rsp.text)