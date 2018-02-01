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

def genXls():
    #找到所有定期理财的投资记录
    loanFrame=pd.DataFrame([],dtype=int,columns=["investor_uid","loan_principal","loan_interest","loan_add_interest"])
    for suffix in range(0,100):
        loansql="select a.investor_uid,(a.expect_principal+IFNULL(b.expect_principal,0)) as loan_principal,IFNULL(b.expect_interest,0) as loan_interest,IFNULL(b.expect_add_interest,0) as loan_add_interest  from (select investor_uid,sum(expect_principal) as expect_principal from invest.t_investment_%02d where state = 2 and asset_type =0 group by investor_uid ) a left join (select investor_uid,sum(expect_principal) as expect_principal,sum(expect_interest) as expect_interest,sum(expect_add_interest) as expect_add_interest from invest.t_investment_payoff_%02d where state = 0 and asset_type =0 group by investor_uid ) b on a.investor_uid = b.investor_uid " \
            "union " \
            "select b.investor_uid,(IFNULL(a.expect_principal,0)+b.expect_principal) as loan_principal,b.expect_interest as loan_interest,b.expect_add_interest as loan_add_interest  from (select investor_uid,sum(expect_principal) as expect_principal from invest.t_investment_%02d where state = 2 and asset_type =0 group by investor_uid ) a right join (select investor_uid,sum(expect_principal) as expect_principal,sum(expect_interest) as expect_interest,sum(expect_add_interest) as expect_add_interest from invest.t_investment_payoff_%02d where state = 0 and asset_type =0 group by investor_uid ) b on a.investor_uid = b.investor_uid;" % (suffix,suffix,suffix,suffix)
        frame = sql.read_sql(loansql, new_conn)
        loanFrame=pd.concat([loanFrame,frame],ignore_index=True)
        #loanFrame=pd.merge(loanFrame,frame,on="investor_uid",how="outer")
    print(loanFrame.columns,loanFrame.index)
    # 找到所有理财计划的投资记录
    planFrame=pd.DataFrame([],dtype=int,columns=["investor_uid","plan_principal","plan_interest","plan_add_interest"])
    for suffix in range(0,100):
        plansql="select a.investor_uid,(a.expect_principal+IFNULL(b.expect_principal,0)) as plan_principal,IFNULL(b.expect_interest,0) as plan_interest,IFNULL(b.expect_add_interest,0) as plan_add_interest from (select investor_uid,sum(expect_principal) as expect_principal from invest.t_investment_%02d where state = 2 and asset_type = 1 group by investor_uid ) a left join (select investor_uid,sum(expect_principal) as expect_principal,sum(expect_interest) as expect_interest,sum(expect_add_interest) as expect_add_interest from specialDB.t_new_financial_plan_payoff where state = 0 group by investor_uid ) b on a.investor_uid = b.investor_uid" % (suffix)
        frame=sql.read_sql(plansql,new_conn)
        planFrame=pd.concat([planFrame,frame],ignore_index=True)
    print(planFrame.columns,planFrame.index)
    #外链接2张表
    allFrame=pd.merge(loanFrame,planFrame,how="outer",on="investor_uid")
    allFrame=allFrame.fillna(0)
    allFrame=allFrame.astype(np.int64)
    #根据投资人uid找到投资人的姓名和手机号
    userFrame=pd.DataFrame([],columns=["investor_uid","mobile"])
    for uid in allFrame["investor_uid"]:
        usersql="select id as investor_uid,mobile from user.t_user where id= %d " % (uid)
        frame = sql.read_sql(usersql, new_conn)
        userFrame=pd.concat([userFrame,frame],ignore_index=True)
    allFrame = pd.merge(userFrame,allFrame, how="outer", on="investor_uid")
    allFrame = allFrame.fillna(0)
    allFrame = allFrame.astype(np.int64)
    allFrame.to_csv("./所有用户总资产汇总.csv",index=False)







#planFrame=pd.merge(planFrame,frame,on="investor_uid",how="left")
    #找到所有理财计划的投资记录
    #print(dataFrame.columns)
    #print(dataFrame.index)
    #print(loanFrame.columns)
    #print(planFrame.columns)


genXls()


