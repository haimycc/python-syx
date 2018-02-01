from kazoo.client import KazooClient

#获取zk节点
zk = KazooClient(hosts='192.168.10.101:2181')
zk.start()
node=zk.set("/AppConfig/ZYXR/Common/YunYing/Activity/Activity_Spring/")




zk.stop()