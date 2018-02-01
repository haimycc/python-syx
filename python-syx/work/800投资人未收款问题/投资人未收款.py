import mysql.connector

new_conn = mysql.connector.connect(host='192.168.31.222', user='root', password='123456', database='product')
new_cursor = new_conn.cursor(dictionary=True)
file = open("D:\投资人未收款.xls", "w")
f = open('D:\借款人流水.xls', "w")


def handler():

    selectSql = "SELECT asset_id,asset_name,investor_uid,repayment_id,phase," \
                " expect_date,expect_add_interest,expect_interest,expect_pay_platform,expect_principal," \
                " SUM(expect_interest+expect_add_interest+expect_principal) as expect_money" \
                " FROM invest.t_investment_payoffs " \
                " WHERE state=0 AND DATE(expect_date) < DATE(NOW()) GROUP BY payoff_id ORDER BY repayment_id ;"
    new_cursor.execute(selectSql)
    results = new_cursor.fetchall()
    file.write("标id" + "\t")
    file.write("标名" + "\t")
    file.write("投资人id" + "\t")
    file.write("还款id" + "\t")
    file.write("期数" + "\t")
    file.write("预期还款时间" + "\t")
    file.write("应收加息" + "\t")
    file.write("应收利息" + "\t")
    file.write("应付平台管理费" + "\t")
    file.write("应收本金" + "\t")
    file.write("预计收取本息不含服务费" + "\t")
    file.write("借款人id" + "\t")
    file.write("收取金额" + "\t")
    file.write("流水id" + "\t")
    file.write("收取时间" + "\n")

    for res in results:
        file.write(str(res["asset_id"]) + "\t")
        file.write(str(res["asset_name"]) + "\t")
        file.write(str(res["investor_uid"]) + "\t")
        file.write(str(res["repayment_id"]) + "\t")
        file.write(str(res["phase"]) + "\t")
        file.write(str(res["expect_date"].strftime('%Y-%m-%d %H:%M:%S')) + "\t")
        file.write(str(res["expect_add_interest"]) + "\t")
        file.write(str(res["expect_interest"]) + "\t")
        file.write(str(res["expect_pay_platform"]) + "\t")
        file.write(str(res["expect_principal"]) + "\t")
        file.write(str(res["expect_money"]) + "\t")
        handler2(res["asset_name"], int(res["phase"]))

    print("ok")
    file.close()


def handler2(assetName, phase):
    sql = "select * from account.t_user_account_flow_45 where " \
          " uid=201607190000004045 and bus_type = 9 and remark like '平台收取借款人费用:%s|%d';" % (assetName, phase)
    new_cursor.execute(sql)
    fetchall = new_cursor.fetchall()
    if len(fetchall) <= 0:
        file.write("\n")
    for res in fetchall:
        file.write(str(res["peer_uid"]) + "\t")
        file.write(str(res["amount"]) + "\t")
        file.write(str(res["flow_id"]) + "\t")
        file.write(str(res["create_time"].strftime('%Y-%m-%d %H:%M:%S')) + "\n")


def handler3():
    selectSql = "SELECT asset_id,asset_name,investor_uid,repayment_id,phase," \
                " expect_date,expect_add_interest,expect_interest,expect_pay_platform,expect_principal," \
                " SUM(expect_interest+expect_add_interest+expect_principal) as expect_money" \
                " FROM invest.t_investment_payoffs " \
                " WHERE state=0 AND DATE(expect_date) < DATE(NOW()) GROUP BY repayment_id ORDER BY repayment_id ;"
    new_cursor.execute(selectSql)
    results = new_cursor.fetchall()
    f.write("标id" + "\t")
    f.write("借款人id" + "\t")
    f.write("变动金额" + "\t")
    f.write("收取时间" + "\t")
    f.write("remark" + "\t")
    f.write("流水id" + "\n")

    for res in results:
        sql = "select * from account.t_user_account_flow_45 where " \
              " uid=201607190000004045 and bus_type = 9 and remark like '平台收取借款人费用:%s|%d';" % (res["asset_name"], int(res["phase"]))
        new_cursor.execute(sql)
        sql2Res = new_cursor.fetchall()
        for reult in sql2Res:
            f.write(str(reult["loan_id"]) + "\t")
            f.write(str(reult["peer_uid"]) + "\t")
            f.write(str(reult["amount"]) + "\t")
            f.write(str(reult["create_time"].strftime('%Y-%m-%d %H:%M:%S')) + "\t")
            f.write(str(reult["remark"]) + "\t")
            f.write(str(reult["flow_id"]) + "\n")
    f.close()

handler()
handler3()


