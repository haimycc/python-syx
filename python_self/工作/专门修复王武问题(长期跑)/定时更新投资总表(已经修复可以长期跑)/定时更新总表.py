import os
import mysql.connector

new_conn = mysql.connector.connect(host='192.168.50.151', user='search', password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

if __name__ == "__main__" :
    with open("./updateSqls", "a+") as f:
        for suffix in range(0,100):
            sql=str.format("update invest.t_investments a,invest.t_investment_%02d b SET "
                           "a.asset_state=b.asset_state ,"
                           "a.state=b.state,"
                           "a.rest_phase=b.rest_phase,"
                           "a.received_principal=b.received_principal,"
                           "a.received_interest=b.received_interest,"
                           "a.received_add_interest=b.received_add_interest,"
                           "a.actual_pay_platform=b.actual_pay_platform,"
                           "a.received_money=b.received_money,"
                           "a.next_payoff_day=b.next_payoff_day,"
                           "a.lock_day=b.lock_day,"
                           "a.update_time=b.update_time,"
                           "a.finish_time=b.finish_time,"
                           "a.full_time=b.full_time,"
                           "a.invest_property=b.invest_property,"
                           "a.debt_property=b.debt_property "
                           "WHERE "
                           "a.asset_id=b.asset_id and "
                           "a.investment_id=b.investment_id"
                           " ;\n" % (suffix))
            f.write(sql)
