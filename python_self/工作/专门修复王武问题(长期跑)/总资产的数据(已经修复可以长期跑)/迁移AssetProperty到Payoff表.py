import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def genPayoff():
    maps={}
    with open("updatePayoffSql2.20170214", "a+") as f:
        for idx in range(0,100):
            sql="update invest.t_investment_payoff_%02d a,product.t_assets b set a.asset_property = b.asset_property where a.asset_id=b.asset_id ;\n" % (idx)
            f.write(sql)
        sql="update invest.t_investment_payoffs a,product.t_assets b set a.asset_property = b.asset_property where a.asset_id=b.asset_id ;\n"
        f.write(sql)

genPayoff()