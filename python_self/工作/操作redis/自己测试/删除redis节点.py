from rediscluster import StrictRedisCluster
import sys

def redis_cluster():
    redis_nodes =  [{'host':'192.168.2.160','port':7000},
                    {'host':'192.168.2.160','port':7001},
                    {'host': '192.168.2.160', 'port': 7002},
                    {'host': '192.168.2.160', 'port': 7003},
                    {'host': '192.168.2.160', 'port': 7004},
                    {'host': '192.168.2.160', 'port': 7005}
                   ]
    try:
        redisconn = StrictRedisCluster(startup_nodes=redis_nodes)
    except Exception as e:
        print("Connect Error!")
        sys.exit(1)
    keys = redisconn.keys()
    for key in keys:
        if str(key).__contains__("Asset.ID_") :
            redisconn.delete(str(key))


redis_cluster()