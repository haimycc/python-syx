import os
import datetime,time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
from enum import Enum, unique
import math
import numpy as np
import pandas as pd
import pandas.io.sql as sql


new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def finishPayoff():
    with open("updateSql.20170308.3.2", "a+") as f:
        sql="select * from invest.t_investment_payoffs where state = 0 and asset_type = 0 and asset_pool=1 and date(expect_date)<date(now())  "
        new_cursor.execute(sql)
        rows=new_cursor.fetchall()
        for row in rows:
            payoffId=row["payoff_id"]
            payoffIdSuffix=int(str(payoffId)[-2:])
            investId=row["investment_id"]
            investIdSuffix=int(str(investId)[-2:])
            investorUid=row["investor_uid"]
            assetId=row["asset_id"]
            updateSql1="update invest.t_investment_payoff_%02d set state = 3 where payoff_id = %d and investment_id = %d and asset_id = %d and state = 0 and asset_type = 0 and asset_pool = 1 and date(expect_date)<date(now()) ;\n" \
                % (payoffIdSuffix,payoffId,investId,assetId)
            updateSql2="update invest.t_investment_payoff_%02d set state = 3 where payoff_id = %d and investment_id = %d and asset_id = %d and state = 0 and asset_type = 0 and asset_pool = 1 and date(expect_date)<date(now()) ;\n" \
                % (investIdSuffix,payoffId,investId,assetId)
            updateSqls="update invest.t_investment_payoffs set state = 3 where payoff_id = %d and investment_id = %d and asset_id = %d and state = 0 and asset_type =0 and asset_pool = 1 and date(expect_date)<date(now()) ;\n" \
                % (payoffId,investId,assetId)
            f.write(updateSql1)
            f.write(updateSql2)
            f.write(updateSqls)


finishPayoff()