"""
1.存储模块使用Redis 的有序集合，用来做代理的去重和状态标识，同时它也是中心模块和基
础模块，将其他模块串联起来。
2.获取模块定时从代理网站获取代理，将获取的代理传递给存储模块，并保存到数据库。
3.检测模块定时通过存储模块获取所有代理，并对代理进行检测，根据不同的检测结果对代理
设置不同的标识。
4.接口模块通过WebAPI 提供服务接口，接口通过连接数据库并通过Web 形式返回可用的代理。

"""
from random import choice

import redis


MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10
REDIS_HOST ='127.0.0.1'
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_KEY = 'the_proxies'


class redis_client(object):
    def __init__(self,host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)

    def add(self,proxy,score = INITIAL_SCORE):
        if not self.db.zscore(REDIS_KEY,proxy):
            return self.db.zadd(REDIS_KEY,score,proxy)

    def decrease(self,proxy):
        score = self.db.zscore(REDIS_KEY, proxy)
        if score and (score > MIN_SCORE+1):
            return self.db.zincrby(REDIS_KEY, -1, proxy)
        else:
            return self.db.zrem(REDIS_KEY, proxy)

    def random_getProxy(self):
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)
            if len(result):
                return choice(result)
            else:
                raise FileNotFoundError

    def exist(self,proxy):
        result = self.db.zscore(REDIS_KEY, proxy)
        if result:
            return True
        else:
            return False

