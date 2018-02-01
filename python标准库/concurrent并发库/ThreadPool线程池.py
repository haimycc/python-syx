from concurrent.futures import ThreadPoolExecutor
import urllib.request

def fetch_url(url):
    u=urllib.request.urlopen(url)
    data=u.read()
    return data


pool=ThreadPoolExecutor(10)

a=pool.submit(fetch_url,"http://www.baidu.com")
b=pool.submit(fetch_url,"http://www.123.com")

x=a.result()
y=b.result()