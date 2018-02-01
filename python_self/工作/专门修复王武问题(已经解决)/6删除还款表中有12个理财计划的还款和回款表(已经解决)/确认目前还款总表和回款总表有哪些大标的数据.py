import os

import mysql.connector

new_conn = mysql.connector.connect(host='192.168.50.151', user='search', password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def getRepays():
    with open("./updateSqls2", "a+") as f:
        #找到理财计划的还款表
        sql="select * from product.t_repayments where asset_type = 1"
        new_cursor.execute(sql)
        repayRows = new_cursor.fetchall()
        for repay in repayRows:
            #找到还款表
            assetId=repay["asset_id"]
            repayId=repay["repayment_id"]
            f.write("delete from product.t_repayment_%02d where asset_id= %d and repayment_id=%d and asset_type = 1;\n" % (int(str(repayId)[-2:]),assetId,repayId))
            f.write("delete from product.t_repayments where asset_id=%d and repayment_id=%d and asset_type =1;\n" % (assetId,repayId))
            #找到回款表
            sql="select * from invest.t_investment_payoffs where asset_id=%d and repayment_id=%d and asset_type = 1;\n" % (assetId,repayId)
            new_cursor.execute(sql)
            investRows = new_cursor.fetchall()
            for invest in investRows:
                payoffId=invest["payoff_id"]
                investId=invest["investment_id"]
                f.write("delete from invest.t_investment_payoff_%02d where payoff_id=%d and investment_id=%d and asset_id=%d and asset_type=1;\n" % (int(str(payoffId)[-2:]),payoffId,investId,assetId))
                f.write("delete from invest.t_investment_payoffs where payoff_id=%d and investment_id=%d and asset_id=%d and asset_type =1;\n" % (payoffId,investId,assetId))
                #确认有新的回款表记录
                sql="select * from specialDB.t_new_financial_plan_payoff where investment_id= %d" % (investId)
                new_cursor.execute(sql)
                payoffRows = new_cursor.fetchall()
                if len(payoffRows) == 0 :
                    print("错误,investment_id:%d 找不到回款记录" % (investId))
getRepays()