import mysql.connector

# new_conn = mysql.connector.connect(host='192.168.50.151', user='root', password='123456', database='product')
# new_cursor = new_conn.cursor(dictionary=True)
file = open("D:\还款总表.txt", "w")
f = open('D:\还款分表.txt', "w")


def handler():
    updateSqlPer = "update product.t_repayments set expect_date='%s' where asset_id='%d' AND phase='%d' and expect_date='%s'"

        # pdateSqlAll = "update invest.t_investment_payoffs set expect_date='%s' where asset_id='%d' AND phase='%d' and investment_id='%d' and expect_date='%s';\n " % (


        # file.write(updateSqlAll)
        # f.write(updateSqlFen)


handler()
