import os
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def getExpectDate():
    sql="select a.payoff_id,b.repayemnt_id,a.expect_date,b.expect_date   from invest.t_investment_payoffs a , product.t_repayments b where a.repayemnt_id=b.repayment_id and a.expect_date != b.expect_date "