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

def getUserInvestSum(uid):
    suffix=int(str(uid)[-2:])
    #定期理财的待收本金
    loanPrincipal=0
    loanInterest=0
    loanAddInterest=0
    loanSql="select " \
            "a.investor_uid," \
            "(a.expect_principal+IFNULL(b.expect_principal,0)) as loan_principal," \
            "IFNULL(b.expect_interest,0) as loan_interest," \
            "IFNULL(b.expect_add_interest,0) as loan_add_interest  " \
            "from " \
            "(select investor_uid,sum(amount) as expect_principal " \
            "from " \
            "invest.t_investment_%02d where  asset_state=5 and state = 2 and asset_type =0  and asset_pool=1 and investor_uid=%d group by investor_uid " \
            ") a " \
            "left join " \
            "(select investor_uid,sum(expect_principal) as expect_principal," \
            "sum(expect_interest) as expect_interest," \
            "sum(expect_add_interest) as expect_add_interest " \
            "from invest.t_investment_payoff_%02d where state = 0 and asset_type =0 and asset_pool=1 and investor_uid=%d  group by investor_uid " \
            ") b " \
            "on " \
            "a.investor_uid = b.investor_uid  " \
            "union " \
            "select " \
            "b.investor_uid," \
            "(IFNULL(a.expect_principal,0)+b.expect_principal) as loan_principal," \
            "b.expect_interest as loan_interest," \
            "b.expect_add_interest as loan_add_interest  " \
            "from " \
            "(select investor_uid,sum(amount) as expect_principal " \
            "from " \
            "invest.t_investment_%02d where  asset_state=5 and state = 2 and asset_type =0 and asset_pool=1 and investor_uid=%d group by investor_uid " \
            ") a " \
            "right join " \
            "(select investor_uid,sum(expect_principal) as expect_principal," \
            "sum(expect_interest) as expect_interest," \
            "sum(expect_add_interest) as expect_add_interest " \
            "from invest.t_investment_payoff_%02d where state = 0 and asset_type =0 and asset_pool=1 and investor_uid=%d group by investor_uid " \
            ") b " \
            "on " \
            "a.investor_uid = b.investor_uid ;" % (suffix,uid,suffix,uid,suffix,uid,suffix,uid)
    new_cursor.execute(loanSql)
    loanRows = new_cursor.fetchall()
    for loan in loanRows:
        loanPrincipal=loan["loan_principal"]
        loanInterest=loan["loan_interest"]
        loanAddInterest=loan["loan_add_interest"]
        print(str.format("定期理财:待收本金:%d,待收利息:%d,待收加息:%d" % (loanPrincipal, loanInterest, loanAddInterest)))

    #理财计划的待收本金
    planPrincipal=0
    planInterest=0
    planAddInterest=0
    plansql = "select " \
              "a.investor_uid," \
              "(a.expect_principal+IFNULL(b.expect_principal,0)) as plan_principal," \
              "IFNULL(b.expect_interest,0) as plan_interest," \
              "IFNULL(b.expect_add_interest,0) as plan_add_interest " \
              "from " \
              "(select investor_uid,sum(amount) as expect_principal " \
              "from " \
              "invest.t_investment_%02d where asset_state=5 and state = 2 and asset_type = 1  and investor_uid=%d group by investor_uid " \
              ") a " \
              "left join " \
              "(select investor_uid," \
              "sum(expect_principal) as expect_principal," \
              "sum(expect_interest) as expect_interest," \
              "sum(expect_add_interest) as expect_add_interest " \
              "from " \
              "specialDB.t_new_financial_plan_payoff where state = 0 and investor_uid=%d group by investor_uid " \
              ") b " \
              "on " \
              "a.investor_uid = b.investor_uid " \
              "union " \
              "select b.investor_uid," \
              "(IFNULL(a.expect_principal,0)+b.expect_principal) as plan_principal, " \
              "IFNULL(b.expect_interest,0) as plan_interest," \
              "IFNULL(b.expect_add_interest,0) as plan_add_interest " \
              "from " \
              "(select investor_uid,sum(expect_principal) as expect_principal " \
              "from " \
              "invest.t_investment_%02d where asset_state=5 and state = 2 and asset_type = 1  and investor_uid=%d group by investor_uid " \
              ") a " \
              "right join " \
              "(select investor_uid," \
              "sum(expect_principal) as expect_principal," \
              "sum(expect_interest) as expect_interest," \
              "sum(expect_add_interest) as expect_add_interest " \
              "from " \
              "specialDB.t_new_financial_plan_payoff where state = 0 and investor_uid=%d group by investor_uid " \
              ") b " \
              "on " \
              "a.investor_uid = b.investor_uid " % (suffix,uid,uid,suffix,uid,uid)
    new_cursor.execute(plansql)
    planRows = new_cursor.fetchall()
    for plan in planRows:
        planPrincipal = plan["plan_principal"]
        planInterest = plan["plan_interest"]
        planAddInterest = plan["plan_add_interest"]
        print(str.format("理财计划:待收本金:%d,待收利息:%d,待收加息:%d" % (planPrincipal,planInterest,planAddInterest)))

    loan=loanPrincipal+loanInterest+loanAddInterest
    plan=planPrincipal+planInterest+planAddInterest
    print(loan)
    print(plan)
    print(loan+plan)


if __name__ == "__main__" :
    getUserInvestSum(201609010008908097)