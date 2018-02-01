import mysql.connector

new_conn = mysql.connector.connect(host='192.168.31.222', user='root', password='123456', database='product')
new_cursor = new_conn.cursor(dictionary=True)
file = open("D:\回款总表.txt", "w")
f = open('D:\回款分表.txt', "w")


def handler():
    sql3 = "SELECT " \
           " a.asset_id,a.expect_date,a.phase, b.investment_id,b.expect_date as oldTime " \
           " FROM" \
           " product.t_repayments a," \
           " invest.t_investment_payoffs b" \
           " WHERE" \
           " a.asset_id = b.asset_id" \
           " AND a.phase = b.phase" \
           " AND DATE(a.expect_date) != date(b.expect_date)" \
           " AND a.state in (0,4)" \
           " AND b.state = 0" \
           " AND a.create_time > '2017-06-01 00:00:00'" \
           " AND b.actual_date = '0000-00-00 00:00:00'" \
           " AND a.actual_date = '0000-00-00 00:00:00'" \
           " ORDER BY a.create_time"

    new_cursor.execute(sql3)
    results = new_cursor.fetchall()
    count = 0
    for res in results:
        # print(res['expect_date'])
        updateSqlAll = "update invest.t_investment_payoffs set expect_date='%s' where asset_id='%d' AND phase='%d' and investment_id='%d' and expect_date='%s';\n " % (
        res['expect_date'], res['asset_id'], res['phase'], res['investment_id'], res['oldTime'])
        selectSql = "select expect_date from invest.t_investment_payoffs where asset_id='%d' AND phase='%d' and investment_id='%d' and expect_date='%s'; " % (
        res['asset_id'], res['phase'], res['investment_id'], res['oldTime'])

        updateSqlFen = "update invest.t_investment_payoff_%02d set expect_date='%s' where asset_id='%d' AND phase='%d' and investment_id='%d' and expect_date='%s' ;\n " % (
        res['investment_id'] % 100, res['expect_date'], res['asset_id'], res['phase'], res['investment_id'],
        res['oldTime'])

        # selectSql="select expect_date from invest.t_investment_payoff_%02d where asset_id='%d' AND phase='%d' and investment_id='%d'   and expect_date='%s' ; " % (res['investment_id']%100,res['asset_id'],res['phase'],res['investment_id'],res['oldTime'])
        file.write(updateSqlAll)
        f.write(updateSqlFen)
        new_cursor.execute(selectSql)
        fetchall = new_cursor.fetchall()
        # print(selectSql)
        count += 1
        print(str(count) + "=" + str(len(fetchall)) + selectSql)
        # count += 1
        # print(count)

    f.close()
    file.close()
handler()
