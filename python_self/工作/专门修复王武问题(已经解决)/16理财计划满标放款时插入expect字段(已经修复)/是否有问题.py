import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.51.145',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)


def findDiff():
    sql="select count(1) from invest.t_investments a,specialDB.t_new_financial_yaoff b on a.asset_id=b.asset_id and a.investment_id=b.investment_id " \
        " where a.expect_interest!=b.expect_interest or a.expect_add_interest!=b.expect_add_interest;"