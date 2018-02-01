import mysql.connector

new_conn = mysql.connector.connect(host='192.168.31.222', user='root', password='123456', database='product')
new_cursor = new_conn.cursor(dictionary=True)
file = open("D:\修复投资人回款状态sql.txt", "w")

def handler():
    sql1 = "update invest.t_investment_payoffs set state=3,update_time=now() where " \
           "asset_id=%d and asset_name='%s' and investor_uid=%d " \
           "and repayment_id=%d and phase=%d and payoff_id=%d and expect_date='%s'; "
    sql2 = "update invest.t_investment_payoff_%s set state=3,update_time=now() where " \
           "asset_id=%d and asset_name='%s' and investor_uid=%d " \
           "and repayment_id=%d and phase=%d and payoff_id=%d and expect_date='%s'; "

    selectSql = "SELECT asset_id,asset_name,investor_uid,repayment_id,phase,payoff_id,expect_date "\
                " FROM invest.t_investment_payoffs " \
                " WHERE state=0 and asset_pool in (2,4) AND DATE(expect_date) < DATE(NOW()) GROUP BY payoff_id ORDER BY repayment_id ;"
    new_cursor.execute(selectSql)
    results = new_cursor.fetchall()
    for res in results:
        file.write(sql1 % (res["asset_id"], res["asset_name"], res["investor_uid"], res["repayment_id"], res["phase"], res["payoff_id"], str(res["expect_date"].strftime('%Y-%m-%d %H:%M:%S'))) + "\n")
        file.write(sql2 % (str(res["investor_uid"])[-2:], res["asset_id"], res["asset_name"], res["investor_uid"], res["repayment_id"], res["phase"], res["payoff_id"],str(res["expect_date"].strftime('%Y-%m-%d %H:%M:%S'))) + "\n")
    file.close()

handler()