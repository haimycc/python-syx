# -*- coding:utf-8 -*-

import os
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.51.145',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

#读取新老数据库投资记录ID
def readFile():
    infos=[]
    with open('./depositRepay', 'r',encoding="utf-8") as f:
        for line in f.readlines():
            info=line.split(",")
            infos.append(info)
    return infos

#更新代偿记录为已还
def UpdateDepositToRepay(lists):
    for list in lists:
        assetName=list[0]
        assetId=0
        repayId=0
        borrowerName=list[1]
        borrowerMobile=list[2]
        borrowerUid=0
        depositMoney=list[3]
        idepositMoney=int(float(depositMoney)*100)
        depositTime=list[4]

        #找到该还款人uid
        sql="select id from user.t_user where mobile=%s" % (borrowerMobile)
        new_cursor.execute(sql)
        results = new_cursor.fetchall()
        if len(results) > 1 :
            print("error :result > 1 ,sql is "+sql)
        for result in results:
            borrowerUid=int(result["id"])

        #找到标的的id
        sql="select asset_id,deposit_phase from product.t_assets where asset_name ='%s' and borrower_uid=%d " % (assetName,borrowerUid)
        new_cursor.execute(sql)
        results = new_cursor.fetchall()
        if len(results) > 1 :
            print("error :result > 1 ,sql is "+sql)
        for result in results:
            assetId=int(result["asset_id"])
            depositPhase=int(result["deposit_phase"])
            #print(depositPhase)
            #if depositPhase > 1 :
            #    print("!!!!!!!!!!!!!!!!!!!!!!!!!! asset id is %d" % (depositPhase))

        #找到这条还款计划
        sql="select repayment_id from product.t_repayments where asset_id = %d and date(guarantee_date)=date('%s') " % (assetId,depositTime)
        new_cursor.execute(sql)
        results = new_cursor.fetchall()
        if len(results) > 1 :
            print("error :result > 1 ,sql is "+sql)
        for result in results:
            repayId=int(result["repayment_id"])

        #分表
        tableSuffix=int(str(assetId)[-2:])
        updateSql1="update product.t_repayment_%02d set actual_principal=guarantee_principal,actual_interest=guarantee_interest,actual_pay_fee=guarantee_pay_fee  where asset_id=%d and repayment_id=%d and  borrower_uid=%d and state=3 and (guarantee_principal+guarantee_interest+guarantee_pay_fee)= %d;" % \
            (tableSuffix,assetId,repayId,borrowerUid,idepositMoney)
        updateSql2="update product.t_repayment_%02d set guarantee_principal=0,guarantee_interest=0,guarantee_pay_fee=0,guarantee_role=0,guarantee_name=''  where asset_id=%d and repayment_id=%d and  borrower_uid=%d and state=3 and (guarantee_principal+guarantee_interest+guarantee_pay_fee)= %d;" % \
            (tableSuffix,assetId,repayId,borrowerUid,idepositMoney)
        updateSqls="update product.t_repayments set actual_principal=guarantee_principal,actual_interest=guarantee_interest,actual_pay_fee=guarantee_pay_fee  where asset_id=%d and repayment_id=%d and  borrower_uid=%d and state=3 and (guarantee_principal+guarantee_interest+guarantee_pay_fee)= %d;" % \
            (assetId,repayId,borrowerUid,idepositMoney)
        updateSqls2="update product.t_repayments set guarantee_principal=0,guarantee_interest=0,guarantee_pay_fee=0,guarantee_role=0,guarantee_name=''  where asset_id=%d and repayment_id=%d and  borrower_uid=%d and state=3 and (guarantee_principal+guarantee_interest+guarantee_pay_fee)= %d;" % \
            (assetId,repayId,borrowerUid,idepositMoney)
        #如果是最后一期还款,那么更新标的表
        updateAssetSql1="update product.t_assets set deposit_phase = deposit_phase-1,repay_phase=repay_phase+1 where asset_id = %d and state = 9 and deposit_phase >= 1 ;" % (assetId)
        updateAssetSql2="update product.t_assets set state=8 where asset_id=%d and  deposit_phase=0;" % (assetId)
        updateAssetSql3="update product.t_assets set state=10 where asset_id=%d and repay_phase=phase_total and deposit_phase=0;" % (assetId)
        #print(updateSql1)
        #print(updateSql2)
        #print(updateSqls)
        #print(updateSqls2)
        print(updateAssetSql1)
        print(updateAssetSql2)
        print(updateAssetSql3)

if '__main__' == __name__:
    UpdateDepositToRepay(readFile())


