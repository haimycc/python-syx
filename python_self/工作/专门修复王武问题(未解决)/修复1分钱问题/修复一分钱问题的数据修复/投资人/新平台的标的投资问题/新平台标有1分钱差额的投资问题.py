import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime
import xlrd
import xlwt


new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)


def genSql():
    #修复待收本金不符合
    # for idx in range(0,100):
    #     sql="select " \
    #         " a.investment_id,a.amount,a.money1,b.money2 " \
    #         " from " \
    #         "(select amount,ifnull(sum(expect_principal),0) as money1,investment_id from invest.t_investment_%02d where asset_property & 65536 != 65536 group by investment_id)  a," \
    #         "(select ifnull(sum(expect_principal),0) as money2,investment_id from invest.t_investment_payoff_%02d group by investment_id) b " \
    #         "where " \
    #         "a.investment_id=b.investment_id and a.money1!=b.money2 " % (idx,idx)
    #     new_cursor.execute(sql)
    #     rows = new_cursor.fetchall()
    #     for row in rows:
    #         #if row["money1"] < row["money2"]:
    #         #    print("%d < %d" % (row["money1"],row["money2"]))
    #         print("investment id is %d,amount is %d,money1 is %d,money2 is %d\n" % (row["investment_id"],row["amount"],row["money1"],row["money2"]))

    #修复待收利息不符合
    # for idx in range(0,100):
    #     sql="select " \
    #         " a.investment_id,a.amount,a.money1,b.money2 " \
    #         " from " \
    #         "(select amount,ifnull(sum(expect_interest),0) as money1,investment_id from invest.t_investment_%02d where asset_property & 65536 != 65536 group by investment_id)  a," \
    #         "(select ifnull(sum(expect_interest),0) as money2,investment_id from invest.t_investment_payoff_%02d group by investment_id) b " \
    #         "where " \
    #         "a.investment_id=b.investment_id and a.money1!=b.money2 " % (idx,idx)
    #     new_cursor.execute(sql)
    #     rows = new_cursor.fetchall()
    #     for row in rows:
    #         #if row["money1"] < row["money2"]:
    #         #    print("%d < %d" % (row["money1"],row["money2"]))
    #         if row["money1"] > row["money2"]:
    #             print("investment id is %d,amount is %d,money1 is %d,money2 is %d\n" % (row["investment_id"],row["amount"],row["money1"],row["money2"]))

    #修复待收加息
    # for idx in range(0, 100):
    #     sql = "select " \
    #           " a.investment_id,a.amount,a.money1,b.money2 " \
    #           " from " \
    #           "(select amount,ifnull(sum(expect_add_interest),0) as money1,investment_id from invest.t_investment_%02d where asset_property & 65536 != 65536 group by investment_id)  a," \
    #           "(select ifnull(sum(expect_add_interest),0) as money2,investment_id from invest.t_investment_payoff_%02d group by investment_id) b " \
    #           "where " \
    #           "a.investment_id=b.investment_id and a.money1!=b.money2 " % (idx, idx)
    #     new_cursor.execute(sql)
    #     rows = new_cursor.fetchall()
    #     for row in rows:
    #         # if row["money1"] < row["money2"]:
    #         #    print("%d < %d" % (row["money1"],row["money2"]))
    #         if row["money1"] < row["money2"]:
    #             print("investment id is %d,amount is %d,money1 is %d,money2 is %d\n" % ( row["investment_id"], row["amount"], row["money1"], row["money2"]))

    #预计平台管理费
    for idx in range(0, 100):
        sql = "select " \
              " a.investment_id,a.amount,a.money1,b.money2 " \
              " from " \
              "(select amount,ifnull(sum(expect_pay_platform),0) as money1,investment_id from invest.t_investment_%02d where asset_property & 65536 != 65536 group by investment_id)  a," \
              "(select ifnull(sum(expect_pay_platform),0) as money2,investment_id from invest.t_investment_payoff_%02d group by investment_id) b " \
              "where " \
              "a.investment_id=b.investment_id and a.money1!=b.money2 " % (idx, idx)
        new_cursor.execute(sql)
        rows = new_cursor.fetchall()
        for row in rows:
            # if row["money1"] < row["money2"]:
            #    print("%d < %d" % (row["money1"],row["money2"]))
            if row["money1"] > row["money2"]:
                print("investment id is %d,amount is %d,money1 is %d,money2 is %d\n" % ( row["investment_id"], row["amount"], row["money1"], row["money2"]))

genSql()