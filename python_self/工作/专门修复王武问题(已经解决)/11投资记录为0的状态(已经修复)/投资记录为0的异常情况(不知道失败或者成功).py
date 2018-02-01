import os
import datetime,time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)


if __name__ == "__main__" :
    with open("./统计投资状态为0的情况(未知成功或者失败).csv","a+") as f:
        f.write("标的名称,标的ID,投资记录ID,投资人UID,投资人姓名,投资人电话,投资时间,投资金额,是否是理财计划池,是否是定期期理财,是否是理财计划池的小标\n")
        sum=0
        for suffix in range(0,100):
            #找到投资表
            sql=str.format("select financial_plan_id,asset_id,asset_name,investment_id,investor_uid,create_time,amount,asset_type,asset_pool from invest.t_investment_%02d where state = 0 and create_time <='2017-01-09 00:00:00'" % (suffix))
            new_cursor.execute(sql)
            lists = new_cursor.fetchall()
            for list in lists:
                financialId=list["financial_plan_id"]
                assetId=list["asset_id"]
                assetName=list["asset_name"]
                investId=list["investment_id"]
                investorUid=list["investor_uid"]
                createTime=list["create_time"]
                amount=list["amount"]
                assetType=list["asset_type"]
                assetPool=list["asset_pool"]
                #是否有明确成功或者失败的流水
                sql=str.format("select operation from invest.t_investment_flow_%s where investment_id=%d and operation in (3,4)" % (str(investId)[-2:],investId))
                new_cursor.execute(sql)
                results = new_cursor.fetchall()
                #如果没有明确成功或者失败,就是未知是否有冻结
                if len(results) ==  0:
                    sql=str.format("select mobile from user.t_user where id=%d" % (investorUid))
                    new_cursor.execute(sql)
                    results = new_cursor.fetchall()
                    for result in results:
                        mobile=result["mobile"]
                        sql=str.format("select real_name from user.t_user_detail where userid=%d" % (investorUid))
                        new_cursor.execute(sql)
                        realNames = new_cursor.fetchall()
                        for realName in realNames:
                            sum+=1
                            name=realName["real_name"]
                            isFinancialAsset="否"
                            if assetType == 1 :
                                isFinancialAsset="是"
                            isDingqi="否"
                            if assetType == 0 and assetPool == 1 :
                                isDingqi="是"
                            isXiaoSan="否"
                            if assetType == 0 and ( assetPool == 2 or assetPool == 4):
                                isXiaoSan="是"
                            f.write(str.format("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (assetName,str(assetId),investId,str(investorUid),name,mobile,createTime,str(amount),isFinancialAsset,isDingqi,isXiaoSan)))
        print(sum)










