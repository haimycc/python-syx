from kazoo.client import KazooClient

# 生产zk
# idcZk = KazooClient(hosts='192.168.9.xxx:2181')
# idcZk.start()


# 开发环境zk
devZk = KazooClient(hosts='192.168.9.173:2181')
devZk.start()


def getDiff(idcZk, nodeName):
    with open("./zkNode20180104.txt", "a+") as f:
        idcNodes = idcZk.get_children(nodeName)
        # 找到idc存在,但是dev不存在的node
        for node in idcNodes:
            path = ""
            value = ""
            if nodeName != "/":
                path = nodeName + "/" + node
            else:
                path = "/" + node
            try:
                if idcZk.get(path)[0] != None:
                    value = str(idcZk.get(path)[0].decode('utf-8'))
                    f.write("key:%s,value:%s\n" % (path, value))
            except UnicodeEncodeError:
                print("path is %s" % (path))
            getDiff(idcZk, path)


getDiff(devZk, "/AppConfig")
devZk.stop()
