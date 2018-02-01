import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime
import xlrd
import xlwt

#new_conn = mysql.connector.connect(host='192.168.51.145', user='search', password='search@zyxr.com', database='invest')
new_conn = mysql.connector.connect(host='192.168.31.222', user='root', password='123456', database='invest')

new_cursor = new_conn.cursor(dictionary=True)


def handler(assetId):
    sql = "select * from invest.t_investments where asset_id = %d " % (assetId)
    new_cursor.execute(sql)
    invests = new_cursor.fetchall()
    for invest in invests:
        investId = invest["investment_id"]
        expectPrincipal = invest["expect_principal"]
        expectInterest = invest["expect_interest"]
        expectPayPlatform = invest["expect_pay_platform"]

        payoffPrincipal = 0
        payoffInterest = 0
        payoffPayPlatform = 0
        sql = "select ifnull(sum(expect_principal),0) as a,ifnull(sum(expect_interest),0) as b,ifnull(sum(expect_pay_platform),0) as c from invest.t_investment_payoffs where investment_id = %d" \
              % (investId)
        new_cursor.execute(sql)
        payoffs = new_cursor.fetchall()
        for payoff in payoffs:
            payoffPrincipal = payoff["a"]
            payoffInterest = payoff["b"]
            payoffPayPlatform = payoff["c"]

        if expectPrincipal != payoffPrincipal:
            print("error:本金对不齐,asset_id is %d,investment_id is %d,投资表预计本金 is %d,回款表预计本金 is %d" % (
            assetId, investId, expectPrincipal, payoffPrincipal))

        if expectInterest != payoffInterest:
            print("error:利息对不齐,asset_id is %d,investment_id is %d,投资表预计利息 is %d,回款表预计利息 is %d" % (
            assetId, investId, expectInterest, payoffInterest))

        if expectPayPlatform != payoffPayPlatform:
            print("error:平台管理费对不齐,asset_id is %d,investment_id is %d,投资表预计管理费 is %d,回款表预计管理费 is %d" % (
            assetId, investId, expectPayPlatform, payoffPayPlatform))


handler(20170623000109147)
