import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def genPayoff():
    with open("updatePayoffSql.20170214", "a+") as f:
        for idx in range(0,100):
            sql="alter table invest.t_investment_payoff_%02d  Add column asset_property bigint not null default 0 comment '标的属性' ;\n " % (idx)
            f.write(sql)
        sql="alter table invest.t_investment_payoffs  Add column asset_property bigint not null default 0 comment '标的属性' ;\n"
        f.write(sql)

genPayoff()

