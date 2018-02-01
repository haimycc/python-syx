from rediscluster import StrictRedisCluster
import sys
import os
import mysql.connector

new_conn = mysql.connector.connect(host='192.168.50.151', user='search', password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def redis_cluster():
    #生产环境的redis集群
    redis_nodes =  [{'host': '192.168.50.162', 'port': 6379},
                    {'host': '192.168.50.163', 'port': 6379},
                    {'host': '192.168.50.165', 'port': 6379},
                    {'host': '192.168.50.160', 'port': 6379},
                    {'host': '192.168.50.161', 'port': 6379},
                    {'host': '192.168.50.164', 'port': 6379},
                    {'host': '192.168.51.167', 'port': 6379},
                    {'host': '192.168.51.168', 'port': 6379},
                    {'host': '192.168.51.169', 'port': 6379},
                   ]
    try:
        redisconn = StrictRedisCluster(startup_nodes=redis_nodes)
        sql = "select asset_id  from product.t_assets "
        new_cursor.execute(sql)
        lists = new_cursor.fetchall()
        for list in lists:
            assetId = list["asset_id"]
            key = "Asset.ID_" + str(assetId)
            redisconn.delete(str(key))
    except Exception as e:
        print("Connect Error!")
        sys.exit(1)



if  __name__ == '__main__' :
    redis_cluster()