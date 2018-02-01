import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def selectInvestId():
    with open("updatesql.20170123", "a+") as f:
        #找到已经完标的标的
        sql="select asset_id,create_time,bid_time,finish_time,phase_total,phase_mode,state  from product.t_assets where create_time >='2017-01-21' and asset_type = 1 and phase_total=1 "
        new_cursor.execute(sql)
        assetIdLists = new_cursor.fetchall()
        for assetIdList in assetIdLists:
            assetId=assetIdList["asset_id"]
            finishtime=assetIdList["finish_time"]
            sql=str.format("select financial_plan_id,investment_id,asset_state from product.t_investment_%s where asset_id = %d and asset_state != 10" % (str(assetId)[-2:],assetId))
            new_cursor.execute(sql)
            investLists = new_cursor.fetchall()
            for invest in investLists:
                finId=invest["financial_plan_id"]
                investId=invest["investment_id"]
                assetState = invest["asset_state"]
                #状态不为完标状态
                if assetState != 10 :
                    #找到投资记录ID
                    updateSql1="update product.t_investment_%s set asset_state = 10,finish_time='%s' where asset_id = %d and investment_id = %d ;\n" % (str(assetId)[-2:],finishtime,assetId,investId)
                    updateSql2="update financial_plan.t_investment_%02d set asset_state=10,finish_time='%s' where asset_id=%d and investment_id= %d ;\n" % (int(str(finId)[-2:]),finishtime,assetId,investId)
                    updateSql3="update invest.t_investment_%s set asset_state =10,finish_time='%s' where asset_id=%d and investment_id=%d ;\n" % (str(investId)[-2:],finishtime,assetId,investId)
                    updateSqls="update invest.t_investments set asset_state = 10,finish_time= '%s' where asset_id=%d and investment_id=%d ;\n " % (finishtime,assetId,investId)
                    f.write(updateSql1)
                    f.write(updateSql2)
                    f.write(updateSql3)
                    f.write(updateSqls)



if __name__ == "__main__":
    selectInvestId()