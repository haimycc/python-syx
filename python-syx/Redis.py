# -*- coding: utf-8 -*-

# install command：[pip install redis-py-cluster]

from  rediscluster import StrictRedisCluster


class Redis():
    '''Redis 相关操作'''

    def __init__(self):
        self.host_ip = None
        self.redisconn = None

    def connectRedis(self, host_ip):
        '''Redis 操作: 连接Redis\n
           host_ip:  redis主机ip
        '''
        redis_nodes = [{'host': host_ip, 'port': 7000}
                       # {'host':host_ip, 'port': 7001},
                       # {'host':host_ip, 'port': 7002},
                       # {'host':host_ip, 'port': 7003},
                       # {'host':host_ip, 'port': 7004},
                       # {'host':host_ip, 'port': 7005}
                       ]
        try:
            self.redisconn = StrictRedisCluster(startup_nodes=redis_nodes)
            print
            u"连接Redis：" + host_ip + u" 成功！"
        except Exception as e:
            print(u"连接Redis失败!")

    def getKeys(self, *key):
        '''Redis 操作: 模糊匹配指定前缀的Key，并返回key的全名称'''
        return self.redisconn.keys(*key)

    def getValue(self, *key):
        '''Redis 操作: 获取指定Key对应的值'''
        return self.redisconn.get(*key)

    def hgetValue(self, *name):
        '''Redis 操作: 获取指定name对应的值'''
        return self.redisconn.hgetall(*name)

    def getValues(self, *key):
        '''Redis 操作: 获取指定Key对应的值'''
        keys = self.getKeys(*key)
        dict = {}
        for key in keys:
            dict[key] = self.redisconn.get(key)
            # print key+" "+dict[key]
        return dict

    def deleteKeys(self, *keys):
        '''Redis 操作: 删除指定Redis Key'''
        for key in keys:
            ke = self.getKeys(key)
            for k in ke:
                self.redisconn.delete(k)
                print
                k, u"删除成功!"

    def setKeyAndValue(self, key, value):
        '''Redis 操作: 设置Key和value'''
        self.redisconn.set(key, value)

    def hsetKeyAndValue(self, name, key, value):
        '''Redis 操作: 设置name,Key和value'''
        self.redisconn.hset(name, key, value)

    def getLrangeValue(self, name, min=0, max=-1):
        '''Redis 操作: 获取redis队列或LIST列表'''
        return self.redisconn.lrange(name, min, max)

    def delQueueList(self, name, value=None):
        """
        Redis删除队列操作
        :param name:  队列名称
        :param value:  队列内的值，默认为None则删除队列中所有的内容
        """
        queue = self.getLrangeValue(name)
        if value:
            for v in queue:
                if v == value:
                    self.redisconn.lrem(name, 0, v)
        else:
            for v in queue:
                self.redisconn.lrem(name, 0, v)
        print
        u'队列/列表删除完成，删除记录数为:', len(queue)


if __name__ == '__main__':
    host_ip = "127.0.0.1"
    redis = Redis()
    redis.connectRedis(host_ip)
    # print redis.getValues('Trustee:Account:25035135610721002*')
    # print redis.hgetValue('Trustee:Account:AccountOrderQueryRetryKey')
    # redis.deleteKeys('Trustee:Account:250351356107210027')
    # redis.deleteKeys('Trustee:Account:AccountOrderQueryRetryKey')

    # 自动投标的锁
    # redis.getValue('AutoInvestTask')
    # redis.deleteKeys('AutoInvestTask')

    # 自动投标的队列列表
    # a= redis.getLrangeValue('AutoInvestQueue')
    # print u'队列数量：'+str(len(a))
    # print a
    # redis.delQueueList('AutoInvestQueue')

    # 法大大队列列表
    # b= redis.getQueueValue('Fdd_Contract_Init_Queue')
    # c=redis.getQueueValue('Fdd_Contract_Error_Queue')
    # print u'满标未生成队列数量：'+str(len(b))
    # print b
    # print u'生成失败的队列数量：'+str(len(c))
    # print c

    # 银行卡上下架的redis K
    # print redis.getValue('bankKey_all')
    # redis.deleteKeys('bankKey_all')

    # 自动匹配的Key
    # print redis.getValues('Product_matchTask.*')

    # 手工匹配的锁
    # print redis.getValues('RedisLock->PlanMatchServiceImpl.manualMatch')
    # print redis.getValues('RedisLock->PlanMatchServiceImpl.manualLockMatch')
    # redis.deleteKeys('RedisLock->PlanMatchServiceImpl.manualMatch')

    # 银行卡上下架Key
    redis.deleteKeys('contract_template_*')

    # 快速选标债权刷新Key
    # print redis.getLrangeValue('asset.detail.nofinish.display')
    # redis.delQueueList('asset.detail.nofinish.display')

    ##删除短信模板的缓存
    # redis.deleteKeys('SMSTemplate')
