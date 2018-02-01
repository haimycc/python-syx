import os
import mysql.connector

new_conn = mysql.connector.connect(host='192.168.50.151', user='search', password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

if __name__ == "__main__" :
    with open("./updateSqls", "a+") as f:
        for suffix in range(0,100):
            sql=str.format("update invest.t_investment_payoffs a,invest.t_investment_payoff_%02d b SET "
                            "a.actual_principal = b.actual_principal,"
                            "a.actual_interest = b.actual_interest,"
                            "a.actual_add_interest = b.actual_add_interest,"
                            "a.actual_pay_platform = b.actual_pay_platform,"
                            "a.actual_date = b.actual_date,"
                            "a.state = b.state,"
                            "a.property = b.property,"
                            "a.update_time = b.update_time"
                           "  WHERE "
                           " a.asset_id=b.asset_id and "
                           " a.payoff_id=b.payoff_id"
                           " ;\n" % (suffix))
            f.write(sql)
