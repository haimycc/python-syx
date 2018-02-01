import os
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.51.145',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def updateInvests():
    for suffix in range(0,100):
        sql = "update invest.t_investments inner join invest.t_investment_%02d t on invest.t_investments.investment_id=t.investment_id set " \
              "invest.t_investments.asset_state=t.asset_state," \
              "invest.t_investments.asset_property=t.asset_property," \
              "invest.t_investments.annual_rate=t.annual_rate," \
              "invest.t_investments.add_rate =t.add_rate," \
              "invest.t_investments.phase_total =t.phase_total," \
              "invest.t_investments.phase_mode =t.phase_mode," \
              "invest.t_investments.repay_mode =t.repay_mode," \
              "invest.t_investments.amount=t.amount," \
              "invest.t_investments.debt_id=t.debt_id,"\
              "invest.t_investments.debt_name=t.debt_name,"\
              "invest.t_investments.investor_uid=t.investor_uid,"\
              "invest.t_investments.borrower_uid=t.borrower_uid,"\
              "invest.t_investments.valid_amount=t.valid_amount," \
              "invest.t_investments.state=t.state," \
              "invest.t_investments.debt_property=t.debt_property," \
              "invest.t_investments.from_device=t.from_device," \
              "invest.t_investments.rest_phase=t.rest_phase," \
              "invest.t_investments.expect_principal=t.expect_principal," \
              "invest.t_investments.expect_interest=t.expect_interest," \
              "invest.t_investments.expect_add_interest=t.expect_add_interest," \
              "invest.t_investments.expect_pay_platform=t.expect_pay_platform," \
              "invest.t_investments.received_principal=t.received_principal," \
              "invest.t_investments.received_interest=t.received_interest," \
              "invest.t_investments.received_add_interest=t.received_add_interest," \
              "invest.t_investments.actual_pay_platform=t.actual_pay_platform," \
              "invest.t_investments.received_money=t.received_money," \
              "invest.t_investments.next_payoff_day=t.next_payoff_day," \
              "invest.t_investments.lock_day=t.lock_day," \
              "invest.t_investments.update_time=t.update_time," \
              "invest.t_investments.create_time=t.create_time," \
              "invest.t_investments.finish_time=t.finish_time," \
              "invest.t_investments.full_time=t.full_time ; " % (suffix)
        print(sql)

if __name__ == "__main__" :
    updateInvests()