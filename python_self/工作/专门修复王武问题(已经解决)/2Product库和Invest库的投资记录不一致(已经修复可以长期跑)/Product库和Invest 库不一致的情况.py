import os
import mysql.connector

new_conn = mysql.connector.connect(host='192.168.50.151', user='search', password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

if __name__ == "__main__" :
    for suffix in range(0,100):
        sql="select financial_plan_id,asset_id,investment_id,state from invest.t_investment_%02d " % (suffix)
        new_cursor.execute(sql)
        assets = new_cursor.fetchall()
        for asset in assets:
            fId=asset["financial_plan_id"]
            aId=asset["asset_id"]
            investId=asset["investment_id"]
            state1=asset["state"]
            otherSql="select state from product.t_investment_%02d where asset_id = %d and investment_id = %d "  % (int(str(aId)[-2:]),aId,investId)
            new_cursor.execute(otherSql)
            states = new_cursor.fetchall()
            for state in states:
                state2=state["state"]
                if state1 != state2 :
                    print("asset id is "+str(aId)+",investment id is "+str(investId)+",state1 is "+str(state1)+",state2 is "+str(state2))


