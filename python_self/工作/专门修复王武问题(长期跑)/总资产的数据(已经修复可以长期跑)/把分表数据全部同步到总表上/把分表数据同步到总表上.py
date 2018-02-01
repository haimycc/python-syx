import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime

#老平台
old_conn = mysql.connector.connect(host='192.168.0.220',user='root',password='123456', database='toulf')
old_cursor = old_conn.cursor(dictionary=True)
#新平台
new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def gensql():
    with open('./updateInvestSums', 'a+') as f:
        for idx in range(0,100):
            sql=" select * from invest.t_investment_sum_%02d ;\n" % (idx)
            f.write(sql)

gensql()
