import os
import mysql.connector
from datetime import datetime, date

#new_conn = mysql.connector.connect(host='192.168.9.151',port="10000",user='root',password='a123456', database='invest')
#new_cursor = new_conn.cursor(dictionary=True)

def truncate():
    for idx in range(0,100):
        #print("truncate product.t_investment_%02d ;" % (idx))
        #print("truncate invest.t_investment_%02d ;" % (idx))
       # print("truncate invest.t_investment_flow_%02d ;" % (idx))
        print("truncate financial_plan.t_investment_%02d ;" % (idx))
       # print("truncate invest.t_investments ;")

def delete():
    asset_id = 3015838991320821
    for idx in range(0,100):
        sql0="delete from product.t_assets_flow_%02d where asset_id = %d ;\n" % (idx,asset_id)
        sql1="delete from product.t_investment_%02d where asset_id = %d ;\n" % (idx,asset_id)
        sql2="delete from invest.t_investment_%02d where asset_id = %d ;\n" % (idx,asset_id)
        sql3="delete from financial_plan.t_investment_%02d where asset_id = %d ;\n" % (idx,asset_id)
        sql4="delete from invest.t_investment_flow_%02d where asset_id = %d ;\n" % (idx,asset_id)
        print(sql0)
        print(sql1)
        print(sql2)
        print(sql3)
    sqls="delete from invest.t_investments where asest_id = %d ;\n" % (asset_id)
    sqls2= "update product.t_assets set state=5 where asset_id= %d ;\n" % (asset_id)
    print(sqls2)
    print(sqls)


if __name__ == "__main__" :
    delete()
