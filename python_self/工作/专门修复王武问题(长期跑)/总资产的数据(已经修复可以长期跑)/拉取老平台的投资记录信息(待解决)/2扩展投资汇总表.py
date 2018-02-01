import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime

#老平台
old_conn = mysql.connector.connect(host='192.168.0.220',user='root',password='123456', database='toulf')
old_cursor = old_conn.cursor(dictionary=True)
#新平台
new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

#用户映射
def getUserMap():
    #用户映射表
    usermap={}
    sql="select * from user.t_userid_rel_olduid "
    new_cursor.execute(sql)
    userRows = new_cursor.fetchall()
    #新平台和老平台用户uid映射
    for userRow in userRows:
        userNewId=userRow["userid"]
        userOldId=userRow["ybuid"]
        usermap[userOldId]=userNewId
    return usermap

#定期理财投资人map
def getLoanInvestorList():
    #找到定期理财的所有投资人列表
    investorList=[]
    sql="select distinct investor from toulf.invest "
    old_cursor.execute(sql)
    investorRows = old_cursor.fetchall()
    for investorRow in investorRows:
        investorList.append(investorRow["investor"])
    return investorList

#理财计划投资人map
def getPlanInvestorList():
    #找到理财计划的所有投资人列表
    investorList=[]
    sql="select distinct uid  from toulf.mission_joins"
    old_cursor.execute(sql)
    investorRows = old_cursor.fetchall()
    for investorRow in investorRows:
        investorList.append(investorRow["uid"])
    return investorList


#生成sql
def genSql():
    with open('./2updateInvestSums', 'a+') as f:
        userMap=getUserMap()
        # 遍历定期理财的所有投资人
        invesorList=getLoanInvestorList()
        for investor in invesorList:
            strloanInvestSum=0          #投资金额
            strloanInvestPayoff=0       #已经赚钱收益
            strinvestCount=0            #投资次数
            #定期理财的投资金额
            sql="SELECT ifnull(SUM(recievedPrincipal)*100,0) as recievedPrincipal FROM toulf.invest WHERE investor = '%s' AND `status` IN (2)" % (investor)
            old_cursor.execute(sql)
            rows = old_cursor.fetchall()
            for row in rows:
                strloanInvestSum=int(row["recievedPrincipal"])

            #定期理财已经赚钱收益
            sql="SELECT ifnull(SUM(hasInterest)*100,0) as hasInterest FROM toulf.invest WHERE investor = '%s' AND `status` IN (2)" % (investor)
            old_cursor.execute(sql)
            rows = old_cursor.fetchall()
            for row in rows:
                strloanInvestPayoff=int(row["hasInterest"])

            #定期理财的投资次数
            sql="SELECT ifnull(count(1),0) as count FROM toulf.invest WHERE investor = '%s' AND `status` IN (2)" % (investor)
            old_cursor.execute(sql)
            rows = old_cursor.fetchall()
            for row in rows:
                strinvestCount=int(row["count"])

            #更新投资记录汇总
            uid=userMap.get(investor,0)
            uidSuffix=int(str(uid)[-2:])
            f.write("update invest.t_investment_sum_%02d "
                    " set "
                    "old_loan_invest_sum=%d,"
                    "old_loan_invest_payoff=%d,"
                    "old_loan_invests=%d"
                    " where "
                    "investor_uid=%d ;\n" % (uidSuffix,strloanInvestSum,strloanInvestPayoff,strinvestCount,uid))


        # 遍历理财计划的所有投资人
        invesorList = getPlanInvestorList()
        for investor in invesorList:
            strplanInvestSum=0          #投资金额
            strplanInvestPayoff=0       #已经撞去收益

            #理财计划投资金额
            sql="select ifnull(SUM(amount)*100,0) as amount from toulf.mission_joins where uid = '%s' AND `status` IN (0, 4)" % (investor)
            old_cursor.execute(sql)
            rows = old_cursor.fetchall()
            for row in rows:
                strplanInvestSum=int(row["amount"])

            #理财计划以赚取收益
            sql="SELECT ifnull(SUM(has_interest)*100,0) as has_interest FROM toulf.mission_invest WHERE investor_id = '%s' AND `status` IN (2)" % (investor)
            old_cursor.execute(sql)
            rows = old_cursor.fetchall()
            for row in rows:
                strplanInvestPayoff=int(row["has_interest"])

            #投资人
            uid=userMap.get(investor,0)
            uidSuffix=int(str(uid)[-2:])
            f.write("update invest.t_investment_sum_%02d "
                    " set "
                    "old_plan_invest_sum=%d,"
                    "old_plan_invest_payoff=%d"
                    " where "
                    "investor_uid=%d ;\n" % (uidSuffix,strplanInvestSum,strplanInvestPayoff,uid))

if __name__ == "__main__" :
    genSql()




