from kazoo.client import KazooClient

zk = KazooClient(hosts='192.168.2.160:2181')
zk.start()
node=zk.get("/AppConfig/ZYXR/Common/YunYing/SpecialYunYinUser")
print(node)
zk.set("/AppConfig/ZYXR/Common/YunYing/SpecialYunYinUser",b"111\n222\n")


zk.stop()
