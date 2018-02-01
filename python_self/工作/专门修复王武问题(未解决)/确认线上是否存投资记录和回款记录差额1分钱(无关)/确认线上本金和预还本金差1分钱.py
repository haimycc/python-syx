import os
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def getPayoffState():
    with open("getInvestStateSql.20161219","a+") as f:
        for suffix in range(0,100):
            sql=str("select investment_id,asset_state from invest.t_investment_%02d where state=7 " % (suffix))
            new_cursor.execute(sql)
            invests = new_cursor.fetchall()
            for invest in invests:
                investId=invest["investment_id"]
                assetState=invest["asset_state"]
                f.write(str(investId)+","+str(assetState)+"\n")
                if assetState != 10 :
                    print("assetState is !=10.assetId is "+str(investId))

if __name__ == "__main__" :
    getPayoffState()