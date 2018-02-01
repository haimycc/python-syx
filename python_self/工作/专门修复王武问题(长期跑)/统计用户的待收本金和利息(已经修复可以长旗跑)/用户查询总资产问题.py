import os
import datetime, time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151', user='search', password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)


def genCsv(mobile):
    allAmount=0
    with open('./用户待收表2', 'a+') as f:
        f.write("用户姓名,手机号码,投资标的,投资时间,投资金额,已回本息,待收本息（含加息）\n")
        sql = "select id from user.t_user where mobile = %d" % (mobile)
        new_cursor.execute(sql)
        users = new_cursor.fetchall()
        for user in users:
            uid = user["id"]
            uidSuffix = int(str(uid)[-2:])
            sql = "select real_name from user.t_user_detail where userid = %d" % (uid)
            new_cursor.execute(sql)
            users = new_cursor.fetchall()
            for user in users:
                realName = user["real_name"]
                # 定期理财投资中
                sql = "select *  from invest.t_investment_%02d where state=2 and investor_uid = %d and asset_type = 0 and asset_pool = 1" % (
                uidSuffix, uid)
            new_cursor.execute(sql)
            invests = new_cursor.fetchall()
            for invest in invests:
                investId = invest["investment_id"]
                assetName = invest["asset_name"]
                creatTime = invest["create_time"]
                amount = invest["amount"]
                f.write("%s,%s,%s,%s,%s,%s,%s\n" % (realName, mobile, assetName, creatTime, amount, 0, amount))
                allAmount=allAmount+amount
            # 定期理财回款中
            sql = "select *  from invest.t_investment_%02d where state=4 and investor_uid = %d and asset_type = 0 and asset_pool = 1" % (
            uidSuffix, uid)
            new_cursor.execute(sql)
            invests = new_cursor.fetchall()
            for invest in invests:
                investId = invest["investment_id"]
                assetName = invest["asset_name"]
                creatTime = invest["create_time"]
                amount = invest["amount"]
                sql = "select ifnull(sum(actual_principal+actual_interest+actual_add_interest+actual_pay_platform),0) as receivedMoney from invest.t_investment_payoffs where investment_id=%d and state = 3" % (
                investId)
                new_cursor.execute(sql)
                payoffs = new_cursor.fetchall()
                for payoff in payoffs:
                    receivedMoney = payoff["receivedMoney"]
                    sql = "select ifnull(sum(expect_principal+expect_interest+expect_add_interest+expect_pay_platform),0) as waitMoney from invest.t_investment_payoffs where investment_id=%d and state = 0" % (
                        investId)
                    new_cursor.execute(sql)
                    payoffs = new_cursor.fetchall()
                    for payoff in payoffs:
                        waitMoney = payoff["waitMoney"]
                        f.write("%s,%s,%s,%s,%s,%s,%s\n" % (
                        realName, mobile, assetName, creatTime, amount, receivedMoney, waitMoney))
                        allAmount = allAmount + waitMoney

            # 理财计划投资中
            sql = "select *  from invest.t_investment_%02d where state=2 and investor_uid = %d and asset_type = 1 " % (
            uidSuffix, uid)
            new_cursor.execute(sql)
            invests = new_cursor.fetchall()
            for invest in invests:
                investId = invest["investment_id"]
                assetName = invest["asset_name"]
                creatTime = invest["create_time"]
                amount = invest["amount"]
                f.write("%s,%s,%s,%s,%s,%s,%s\n" % (realName, mobile, assetName, creatTime, amount, 0, amount))
                allAmount = allAmount + amount


            # 理财计划回款中
            sql = "select *  from invest.t_investment_%02d where state=4 and investor_uid = %d and asset_type = 1" % (
            uidSuffix, uid)
            new_cursor.execute(sql)
            invests = new_cursor.fetchall()
            for invest in invests:
                investId = invest["investment_id"]
                assetName = invest["asset_name"]
                creatTime = invest["create_time"]
                amount = invest["amount"]
                sql = "select ifnull(sum(actual_principal+actual_interest+actual_add_interest),0) as receivedMoney from specialDB.t_new_financial_plan_payoff  where investment_id=%d and state = 3" % (
                investId)
                new_cursor.execute(sql)
                payoffs = new_cursor.fetchall()
                for payoff in payoffs:
                    receivedMoney = payoff["receivedMoney"]
                    sql = "select ifnull(sum(expect_principal+expect_interest+expect_add_interest),0) as waitMoney from specialDB.t_new_financial_plan_payoff where investment_id=%d and state = 0" % (
                        investId)
                    new_cursor.execute(sql)
                    payoffs = new_cursor.fetchall()
                    for payoff in payoffs:
                        waitMoney = payoff["waitMoney"]
                        f.write("%s,%s,%s,%s,%s,%s,%s\n" % (
                        realName, mobile, assetName, creatTime, amount, receivedMoney, waitMoney))
                        allAmount=allAmount+waitMoney
    print(allAmount)


genCsv(18664688515)
