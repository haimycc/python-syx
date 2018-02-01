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

def getInvestorOneCons():
    # 创建工作簿
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建sheet
    data_sheet = workbook.add_sheet('投资记录表维度')
    row0 = [u'投资记录ID',u'标的ID',u'是否老平台的标',u'预计本金',u'payoff预计本金',u'预计利息',u'payoff预计利息',u'预计加息',u'payoff预计加息',u'预计平台管理费',u'payoff预计平台管理费']
    for i in range(len(row0)):
        data_sheet.write(0, i, row0[i])
    rownum=1

    for idx in range(0,100):
        #从投资记录触发,找到回款表
        sql="select " \
            "investment_id," \
            "asset_id," \
            "asset_property," \
            "expect_principal," \
            "expect_interest," \
            "expect_add_interest," \
            "expect_pay_platform," \
            "received_principal," \
            "received_interest," \
            "received_add_interest," \
            "actual_pay_platform," \
            "received_money" \
            " from " \
            "invest.t_investment_%02d " \
            "where asset_type = 0 and asset_pool = 1 and state = 4 " % (idx)
        new_cursor.execute(sql)
        investRows = new_cursor.fetchall()
        for investRow in investRows:
            assetId=investRow["asset_id"]
            investId=investRow["investment_id"]
            investIdSuffix=int(str(investId)[-2:])
            property=investRow["asset_property"]
            ePrincipal=investRow["expect_principal"]
            eInterest=investRow["expect_interest"]
            eAddInterest=investRow["expect_add_interest"]
            ePayPlatform=investRow["expect_pay_platform"]
            rPrincipal=investRow["received_principal"]
            rInterest=investRow["received_interest"]
            rAddInterest=investRow["received_add_interest"]
            rReceivedMoney=investRow["received_money"]

            sql="select " \
                "ifnull(sum(expect_principal),0) as expect_principal," \
                "ifnull(sum(expect_interest),0) as expect_interest," \
                "ifnull(sum(expect_add_interest),0) as expect_add_interest," \
                "ifnull(sum(expect_pay_platform),0) as expect_pay_platform," \
                "ifnull(sum(actual_principal),0) as actual_principal," \
                "ifnull(sum(actual_interest),0) as actual_interest," \
                "ifnull(sum(actual_add_interest),0) as actual_add_interest," \
                "ifnull(sum(actual_pay_platform),0) as actual_pay_platform" \
                "  from " \
                "invest.t_investment_payoff_%02d " \
                "where investment_id = %d " % (investIdSuffix,investId)
            new_cursor.execute(sql)
            payoffs = new_cursor.fetchall()
            for payoff in payoffs:
                payoffEPrincipal=payoff["expect_principal"]
                payoffEInterest=payoff["expect_interest"]
                payoffEAddInterest=payoff["expect_add_interest"]
                payoffEPayPlatform=payoff["expect_pay_platform"]

                payoffAPrincipal=payoff["actual_principal"]
                payoffAInterest=payoff["actual_interest"]
                payoffAAddInterest=payoff["actual_add_interest"]
                payoffAPayPlatform=payoff["actual_pay_platform"]

                rownum=rownum+1
                isOld=False
                if property & 65536 == 65536 :
                    isOld=True
                else:
                    isOld=False
                row=[str(investId),str(assetId),str(isOld),str(ePrincipal),str(payoffEPrincipal),str(eInterest),str(payoffEInterest),str(eAddInterest),str(payoffEAddInterest),str(ePayPlatform),str(payoffEPayPlatform)]
                for i in range(len(row)):
                    data_sheet.write(rownum, i, row[i])

    # 保存文件
    workbook.save('demo.xls')



getInvestorOneCons()


