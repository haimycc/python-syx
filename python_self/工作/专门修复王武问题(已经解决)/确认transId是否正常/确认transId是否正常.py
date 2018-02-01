import os
import datetime,time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

if __name__ == "__main__" :
    with open("./updateSql","a+") as f:
        sum=0
        for suffix in range(0,100):
            sql=str.format("select trans_id,investment_id,operation from invest.t_investment_flow_%02d b where trans_id in (%d,%d)" % (suffix,201701030002265000,201701040000598000))
            new_cursor.execute(sql)
            lists = new_cursor.fetchall()
            for list in lists:
                transId=list["trans_id"]
                investId=list["investment_id"]
                operation=list["operation"]
                print(str.format("trans id is %d,investment_id is %d,operation is %d" % (transId,investId,operation)))
