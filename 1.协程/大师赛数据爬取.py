import json
import requests


headers={
    'Host': 'm.pvp.xoyo.com',
    'Accept': 'application/json',
    'Accept-Language': 'zh-cn',
    'Accept-Encoding': 'br, gzip, deflate',
    'token': 'b9d30c731fce406a8b9087d30f6d1a10:13043605259:qyqGjqVdFR+ln5tNw1v88A==',
    'Cache-Control': 'no-cache',
    'deviceid': 'yqGjqVdFR+ln5tNw1v88A==',
    'User-Agent': 'SeasunGame/13 CFNetwork/976 Darwin/18.2.0',
    'Connection': 'keep-alive',
    'Content-Length': '129',
    'clientkey': '1',
    'Content-Type': 'application/json',
}
jsonstr='{"matchCode":"DSS","title":"第四届竞技大师赛","ts":"20190317070313178","sign":"d6349f9efdadbb572c3ea828c862fa1e4ee15877"}'
j = json.loads(jsonstr)
data =j

# import json


# headers = {'Content-Type': 'application/json'}    ## headers中添加上content-type这个参数，指定为json格式
response = requests.post(url='http://m.pvp.xoyo.com/master/app/sea-election/', headers=headers, data=json.dumps(data))
# print(response)
j = json.loads(response.text)
out=[]
import pandas as pd

a = [[i['corpsId'],i['zone'], i['server'],i['corpName']]for i in j['data']]

for i in a :
    try:
        headers={
        'Host': 'm.pvp.xoyo.com',
        'Accept': 'application/json',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'br, gzip, deflate',
        'token': 'b9d30c731fce406a8b9087d30f6d1a10:13043605259:qyqGjqVdFR+ln5tNw1v88A==',
        'Cache-Control': 'no-cache',
        'deviceid': 'qyqGjqVdFR+ln5tNw1v88A==',
        'User-Agent': 'SeasunGame/13 CFNetwork/976 Darwin/18.2.0',
        'Connection': 'keep-alive',
        'Content-Length': '141',
        'clientkey': '1',
        'Content-Type': 'application/json',
        }
        jsonstr='{"corpId":"'+i[0]+'","zone":"'+i[1]+'","server":"'+i[2]+'","ts":"","sign":""}'
        j = json.loads(jsonstr)
        data =j
        response = requests.post(url='http://m.pvp.xoyo.com/3s/mine/arena/find-self-corp-info-now', headers=headers,
                                 data=json.dumps(data))
        # print(response)
        j_val = json.loads(response.text)
        val = [j_val['data']['corpName'],j_val['data']['score']+'分', j_val['data']['winRate']]
        out.append(val)
    except:
        print(i[3]+'failed')
        continue
df= pd.DataFrame(out)
df.columns= ['corpName','score','winRate']
df = df.sort_values(by='score',ascending=False)
df.to_csv('jjc.csv')
# print(len(j['data']))
