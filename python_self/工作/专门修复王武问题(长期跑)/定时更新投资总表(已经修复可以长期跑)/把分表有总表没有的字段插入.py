import os
import mysql.connector

new_conn = mysql.connector.connect(host='192.168.50.151', user='search', password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)


if __name__ == "__main__" :
    with open("./insertSqls2","a+") as f:
        #找到分表有，总表没有的
        for suffix in range(0,100):
            sql=str.format("select a.investment_id as a_id,b.investment_id as b_id from invest.t_investment_%02d a left join invest.t_investments b on a.investment_id=b.investment_id" % (suffix))
            new_cursor.execute(sql)
            investIds = new_cursor.fetchall()
            for investId in investIds:
                aId=investId["a_id"]
                bId=investId["b_id"]
                if aId != bId :
                    #aId就是investment id
                    sql=str.format("insert into invest.t_investments select * from invest.t_investment_%s where investment_id=%d ;\n" % (str(aId)[-2:],aId))
                    f.write(sql)



