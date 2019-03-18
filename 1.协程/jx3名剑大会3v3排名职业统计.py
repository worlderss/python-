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
    'Content-Length': '88',
    'clientkey': '1',
    'Content-Type': 'application/json',
}

jsonstr='{"type":"3c","ts":"20190316141959961","sign":"c05d8db9785b5d39df1bb60854efc01db26ff3b3"}'
data = json.loads(jsonstr)
response = requests.post(url='http://m.pvp.xoyo.com/3c/mine/arena/top200', headers=headers, data=json.dumps(data))
# print(response)
j = json.loads(response.text)
# print(j['data'][0])
role= ([[i['personInfo']['gameRoleId'],i['personInfo']['zone'],i['personInfo']['server'],i['personInfo']['person']['nickName'],i['score']] for i in j['data']])
out=[]
num=0
for i in role:
    id,zooe,server = i[0],i[1],i[2]
    jsonstr = '{"role_id":"' + id + '","zone":"' + zooe + '","server":"' + server + '","ts":"","sign":""}'
    data = json.loads(jsonstr)
    response = requests.post(url='http://m.pvp.xoyo.com/role/indicator', headers=headers, data=json.dumps(data))
    # print(response)
    j = json.loads(response.text)
    indicator= j['data']['indicator']
    a = ''
    for x in indicator:
        # print(len(indicator))
        # print(x['type'])
        if '3'in x['type']:
            try:
                a = x['metrics'][0]['kungfu']
            except:
                break

            # print(a)
            # num+=1
    temp = i.copy()
    temp.append(a)
    out.append(temp)
# print(out)
import pandas as pd

df= pd.DataFrame(out)
df.columns=['id','区','服','名字','分数','心法']
print(df[df['心法']=='xiaochen'])
df.to_csv('33data.csv')


