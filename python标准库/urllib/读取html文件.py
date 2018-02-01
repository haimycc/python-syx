import urllib

fd=urllib.urlopen("http://www.baidu.com")
op=open("out.html","wb")

while True:
    s=url_fd.read(4069*2)
    if not s:
        break
    op.write(s)
    n=n+len(s)

op.close()
fd.close()

for key,value in fp.headers.items():
    print("key:"+key+"=>value:"+value)

