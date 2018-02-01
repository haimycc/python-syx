import os
import mysql.connector
from datetime import datetime, date

idc_conn = mysql.connector.connect(host='192.168.51.145',user='search',password='search@zyxr.com', database='invest')
idc_cursor = idc_conn.cursor(dictionary=True)




def getFlowId():
    TransIdList=[
        201701040000000000,
        201701040000000000,
        201701040000001000,
        201701040000001000,
        201701040000289000,
        201701040000289000,
        201701040000290000,
        201701040000290000,
        201701040000291000,
        201701040000291000,
        201701040000341000,
        201701040000341000,
        201701040000345000,
        201701040000345000,
        201701040000346000,
        201701040000346000,
        201701040000349000,
        201701040000349000,
        201701040000509000,
        201701040000509000,
        201701040000515000,
        201701040000515000
    ]
    TransIds = ""
    num=1
    for transId in TransIdList:
        TransIds+=str(transId)
        if num < len(TransIdList) :
            TransIds+=","
        num+=1
    print(TransIds)

    myset=set()
    #遍历所有费率表
    for suffix in range(0,100):
        sql="select trans_id,flow_id,asset_id,investment_id,amount,operation from invest.t_investment_flow_%02d where trans_id in (%s)" % (suffix,TransIds)
        idc_cursor.execute(sql)
        lists = idc_cursor.fetchall()
        for list in lists:
            AssetId=list["asset_id"]
            myset.add(AssetId)
            InvestId=list["investment_id"]
            TransId=list["trans_id"]
            Amount=list["amount"]
            Operation=list["operation"]
            TableName="invest.t_investment_flow_%02d" % (suffix)
            print("table_name is %s,asset_id is %d,invest_id is %d,trans_id is %d,money is %d,operation is %d" % \
                  (TableName,AssetId,InvestId,TransId,Amount,Operation))
    print(myset)

if __name__ == "__main__" :
    getFlowId()
