# -*- coding:utf-8 -*-
import http.client

#http connect
conn=http.client.HTTPSConnection("www.python.org")

#request and reponse
conn.request("GET","/zxp")
rep=conn.getresponse()

#status,status reason
print(rep.status,rep.reason)

#request and reponse
conn.request("GET","/")
rep2=conn.getresponse()

#status,status reason
print(rep2.status,rep2.reason)

while not rep2.closed:
    print(rep2.read(200))
