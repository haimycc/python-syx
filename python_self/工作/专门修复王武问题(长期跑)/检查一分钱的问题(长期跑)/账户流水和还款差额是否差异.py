import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime
import xlrd
import xlwt

new_conn = mysql.connector.connect(host='192.168.2.160', user='root', password='123456', database='invest')
new_cursor = new_conn.cursor(dictionary=True)


def handler(assetId):
    # 前面n-1次入账给平台
    sql = "select * from product.t_repayments where asset_id = %d order by phase desc limit 1,100 " % (assetId)
    new_cursor.execute(sql)
    repays = new_cursor.fetchall()
    for repay in repays:
        repayId = repay["repayment_id"]
        assetName = repay["asset_name"]
        phase = repay["phase"]
        expectPrincipal = repay["expect_principal"]
        expectInterest = repay["expect_interest"]
        expectPayPlatform = repay["expect_pay_platform"]

        sql = "select ifnull(sum(expect_principal),0) as a,ifnull(sum(expect_interest),0) as b,ifnull(sum(expect_pay_platform),0) as c from invest.t_investment_payoffs where repayment_id = %d " % (
        repayId)
        new_cursor.execute(sql)
        payoffs = new_cursor.fetchall()
        for payoff in payoffs:
            payoffPrincipal = payoff["a"]
            payoffInterest = payoff["b"]
            payoffPayPlatform = payoff["c"]
            # 差额
            repayMoney = expectPrincipal + expectInterest + expectPayPlatform
            payoffMoney = payoffPrincipal + payoffInterest + payoffPayPlatform
            if repayMoney >= payoffMoney:
                diff = repayMoney - payoffMoney
                print("标的:%d,第%d期还款,借款人/代偿方转入平台%d分" % (assetId, phase, diff))
                # 查账户流水
                sql = "select * from account.t_user_account_flow_45 where uid= 201607190000004045 and operation = 2 and remark = '平台收取借款人费用:%s|%d' " % (
                assetName, phase)
                new_cursor.execute(sql)
                flows = new_cursor.fetchall()
                for flow in flows:
                    amount = flow["amount"]
                    if amount != diff:
                        print("标的:%d,第%d期还款,借款人/代偿方转入平台金额不对称,预计转入%d分,实际转入%d分" % (assetId, phase, diff, amount))
                    else:
                        print("标的:%d,第%d期还款,借款人/代偿方转入平台金额对称,预计转入%d分,实际转入%d分" % (assetId, phase, diff, amount))
            else:
                print("标的:%d,第%d还款,回款金额大于接口金额")

    # 最后一次平台出账
    sql = "select * from product.t_repayments where asset_id = %d order by phase desc limit 0,1" % (assetId)
    new_cursor.execute(sql)
    repays = new_cursor.fetchall()
    for repay in repays:
        repayId = repay["repayment_id"]
        assetName = repay["asset_name"]
        phase = repay["phase"]
        expectPrincipal = repay["expect_principal"]
        expectInterest = repay["expect_interest"]
        expectPayPlatform = repay["expect_pay_platform"]

        sql = "select ifnull(sum(expect_principal),0) as a,ifnull(sum(expect_interest),0) as b,ifnull(sum(expect_pay_platform),0) as c from invest.t_investment_payoffs where repayment_id = %d " % (
        repayId)
        new_cursor.execute(sql)
        payoffs = new_cursor.fetchall()
        for payoff in payoffs:
            payoffPrincipal = payoff["a"]
            payoffInterest = payoff["b"]
            payoffPayPlatform = payoff["c"]
            # 差额
            repayMoney = expectPrincipal + expectInterest + expectPayPlatform
            payoffMoney = payoffPrincipal + payoffInterest + payoffPayPlatform
            if payoffMoney >= repayMoney:
                diff = payoffMoney - repayMoney
                print("标的:%d,第%d期还款,平台转出%d分" % (assetId, phase, diff))
                # 查账户流水
                sql = "select * from account.t_user_account_flow_45 where uid= 201607190000004045 and operation = 3 and remark like '平台转账冻结:%s|%d'" % (
                assetName, phase)
                new_cursor.execute(sql)
                flows = new_cursor.fetchall()
                for flow in flows:
                    amount = flow["amount"]
                    if amount != diff:
                        print("标的:%d,第%d期还款,平台金额转出不对称,预计转出%d分,实际转出%d分" % (assetId, phase, diff, amount))
                    else:
                        print("标的:%d,第%d期还款,平台金额转出对称,预计转出%d分,实际转出%d分" % (assetId, phase, diff, amount))
            else:
                print("标的:%d,第%d还款,回款金额大于接口金额")


handler(20170324000001071)
