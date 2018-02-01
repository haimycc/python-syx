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

def handler():
    with open("247万散标初始化模板.csv", "a+") as f:
        f.write("投资人姓名,投资人手机号,借款标题,借款金额,投资金额,回款期数,最后一期回款日,预计本息,已收本息,待收本息\n")
        sql="SELECT asset_id FROM invest.t_investments WHERE investor_uid = 201611040000002025 AND asset_type =0 AND asset_pool = 1 and state in (2,4) GROUP BY asset_id  ; "
        new_cursor.execute(sql)
        rows=new_cursor.fetchall()
        for row in rows:
            assetId=row["asset_id"]
            sql="select * from invest.t_investments where asset_id = %d order by asset_id,investment_id" % (assetId)
            new_cursor.execute(sql)
            invests=new_cursor.fetchall()
            for invest in invests:
                investId=invest["investment_id"]
                investorUid=invest["investor_uid"]

                #投资人信息
                investorName=""
                investorMobile=""
                sql="select mobile from user.t_user where id = %d " % (investorUid)
                new_cursor.execute(sql)
                mobiles=new_cursor.fetchall()
                for mobile in mobiles:
                    investorMobile=mobile["mobile"]
                sql="select real_name from user.t_user_detail where userId = %d " % (investorUid)
                new_cursor.execute(sql)
                names=new_cursor.fetchall()
                for name in names:
                    investorName=name["real_name"]

                #标的信息
                assetName=""
                totalAmount=0
                sql="select asset_name,total_amount from product.t_assets where asset_id = %d " % (assetId)
                new_cursor.execute(sql)
                assets=new_cursor.fetchall()
                for asset in assets:
                    assetName=asset["asset_name"]
                    totalAmount=asset["total_amount"]

                #投资信息
                investAmount=invest["amount"]
                investTime=invest["create_time"]

                expectMoney=0
                receiveMoney=0
                restMoney=0
                maxPhase=0
                expectDate=""
                sql="select " \
                    "ifnull(sum(expect_principal+expect_interest+expect_add_interest+expect_pay_platform),0) as expect_money," \
                    "ifnull(sum(actual_principal+actual_interest+actual_add_interest+actual_pay_platform),0) as received_money, " \
                    "max(phase) as max_phase," \
                    "max(expect_date) as expect_date " \
                    "from " \
                    "invest.t_investment_payoffs " \
                    "where " \
                    "investment_id = %d " % (investId)
                new_cursor.execute(sql)
                payoffs=new_cursor.fetchall()
                for payoff in payoffs:
                    expectMoney=payoff["expect_money"]
                    receiveMoney=payoff["received_money"]
                    restMoney=expectMoney-receiveMoney
                    maxPhase=payoff["max_phase"]
                    expectDate=payoff["expect_date"]

                f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"
                        % (str(investorName),str(investorMobile),str(assetName),str(totalAmount),str(investAmount),str(maxPhase),str(expectDate),str(expectMoney),str(receiveMoney),str(restMoney)))


handler()
