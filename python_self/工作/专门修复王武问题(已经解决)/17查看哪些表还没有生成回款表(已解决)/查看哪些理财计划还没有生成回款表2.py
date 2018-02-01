import os
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.51.145',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def getPayoff():
    sql="select a.asset_id,b.payoff_id from product.t_assets a left join specialDB.t_new_financial_plan_payoff b on a.asset_id=b.asset_id where a.asset_type=1 and a.asset_property & 65536 != 65536 and a.state = 8 and IsNull(b.payoff_id);"
    new_cursor.execute(sql)
    results = new_cursor.fetchall()


if __name__ == "__main__" :
    getPayoff()
