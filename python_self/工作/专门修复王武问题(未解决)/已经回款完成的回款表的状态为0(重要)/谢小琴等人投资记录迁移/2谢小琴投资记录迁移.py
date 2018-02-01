import os
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def genSql():
    with open("updatesql.20170227","a+") as f:
        sql="select investor_uid,investment_id,asset_name,count(1)  " \
            "from " \
            "invest.t_investment_payoffs  " \
            "where " \
            "investor_uid in (201609010000003071,201609010000001110,201609010000000098) group by investor_uid,investment_id "
        new_cursor.execute(sql)
        payoffs = new_cursor.fetchall()
        for payoff in payoffs:
            #投资人
            investorUid=payoff["investor_uid"]
            investorUidSuffix=str(investorUid)[-2:]
            #投资记录ID
            oldInvestId=payoff["investment_id"]
            oldInvestIdSuffix=str(oldInvestId)[-2:]
            #新投资记录ID
            newInvestId=str(oldInvestId)[:-2]+investorUidSuffix
            newInvestId=int(newInvestId)+10000000
            newInvestIdSuffix=int(str(newInvestId)[-2:])


            #新增投资回款表
            insertSql1="insert into invest.t_investment_payoff_%02d (select * from invest.t_investment_payoffs where investment_id = %d ) ;\n" \
                       % (newInvestIdSuffix,oldInvestId)
            delSql1="delete from invest.t_investment_payoff_%02d where investment_id = %d ;\n" \
                    % (int(investorUidSuffix),oldInvestId)
            updateSql1="update invest.t_investment_payoff_%02d set investment_id= %d where investment_id = %d ;\n" \
                       % (newInvestIdSuffix,newInvestId,oldInvestId)
            delSqls="delete from invest.t_investment_payoffs where investment_id=%d ;\n" \
                    % (oldInvestId)
            f.write(insertSql1)
            f.write(delSql1)
            f.write(updateSql1)
            f.write(delSqls)
            #插入投资记录

genSql()





