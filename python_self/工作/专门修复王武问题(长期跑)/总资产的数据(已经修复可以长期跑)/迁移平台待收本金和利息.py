import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def genPlatformFee():
    with open("2alterInvestment2.20170215", "a+") as f:
        for idx in range(0,100):
            sql1="alter table invest.t_investment_sum_%02d  Add column loan_pay_platform  bigint not null default 0 comment '定期理财投资管理费' ;\n " % (idx)
            sql2="alter table invest.t_investment_sum_%02d  Add column plan_pay_platform  bigint not null default 0 comment '理财计划' ;\n " % (idx)
            sql3="alter table invest.t_investment_sum_%02d  Add column debt_pay_platform  bigint not null default 0 comment '债权转让' ;\n " % (idx)
            sql4="alter table invest.t_investment_sum_%02d  Add column xrdt_pay_platform  bigint not null default 0 comment '兴融定投投资管理费' ;\n " % (idx)
            f.write(sql1)
            f.write(sql2)
            f.write(sql3)
            f.write(sql4)
        sql1 = "alter table invest.t_investment_sums Add column loan_pay_platform  bigint not null default 0 comment '定期理财投资管理非' ;\n "
        sql2 = "alter table invest.t_investment_sums Add column plan_pay_platform  bigint not null default 0 comment '理财计划' ;\n "
        sql3 = "alter table invest.t_investment_sums Add column debt_pay_platform  bigint not null default 0 comment '债权转让' ;\n "
        sql4 = "alter table invest.t_investment_sums Add column xrdt_pay_platform  bigint not null default 0 comment '兴融定投投资管理费' ;\n "
        f.write(sql1)
        f.write(sql2)
        f.write(sql3)
        f.write(sql4)

genPlatformFee()
