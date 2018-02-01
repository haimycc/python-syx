# -*- coding:utf-8 -*-
import http.client

BODY="***filecontents***"
conn=http.client.HTTPSConnection("localhost",8080)
conn.request("PUT",)