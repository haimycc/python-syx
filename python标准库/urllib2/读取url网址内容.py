import urllib
import time

hosts=["http://www.baidu.com","http://www.qq.com"]
start=time.time()

for host in hosts:
    url=urllib.urlopen(host)
    print(url.read(1024))

print("Elapsed Times:%s " % (time.time()-start))