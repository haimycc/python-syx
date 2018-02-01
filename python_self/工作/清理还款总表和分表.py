import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.2.160', user='mysqluser', password='mysqluser@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)


if __name__ == "__main__" :
    #asset
    sql=str.format("truncate asset.t_asset")
    new_cursor.execute(sql)
    sql=str.format("truncate product.t_assets")
    new_cursor.execute(sql)
    for suffix in range(0,100):
        sql=str.format("truncate product.t_assets_flow_%02d" % suffix)
        new_cursor.execute(sql)

    #fee
    for suffix in range(0,100):
        sql=str.format("truncate product.t_assets_fee_%02d" % suffix)
        new_cursor.execute(sql)

    #invest
    for suffix in range(0,100):
        sql=str.format("truncate invest.t_investment_%02d" % suffix)
        new_cursor.execute(sql)
        sql=str.format("truncate invest.t_investment_flow_%02d" % suffix)
        new_cursor.execute(sql)
        sql=str.format("truncate product.t_investment_%02d" % suffix)
        new_cursor.execute(sql)
        sql=str.format("truncate financial_plan.t_investment_%02d" % suffix)
        new_cursor.execute(sql)
    sql=str.format("truncate invest.t_investments")
    new_cursor.execute(sql)

    #repayment
    for suffix in range(0,100):
        sql=str.format("truncate product.t_repayment_%02d" % (suffix))
        new_cursor.execute(sql)
        sql=str.format("truncate product.t_repayment_flow_%02d" % suffix)
        new_cursor.execute(sql)
    sql=str.format("truncate product.t_repayments")
    new_cursor.execute(sql)






