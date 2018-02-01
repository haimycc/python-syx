import os

import mysql.connector


new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

class Fee(object):
    def __init__(self,mobile):
        self.mobile=mobile
        self.dict={}

    def setAmount(self,assetName,amount):
        if assetName in self.dict:
            self.dict[assetName]+=amount
        else:
            self.dict[assetName]=amount

    def getUnfreeText(self,f1):
        for key,value in self.dict.items():
            f1.write("%s,%d,【%s】还款费用解冻\n" % (self.mobile,value//100,key))


    def getTransferText(self,f2):
        for key,value in self.dict.items():
            f2.write("%s,platform,%d,【%s】还款费用划拨\n" % (self.mobile,value//100,key))




def getCommFee():
    dict={}
    sum=0
    with (open(os.path.abspath(os.curdir) + '/unfreeze.20161216.fee', 'a+')) as f1:
        with(open(os.path.abspath(os.curdir) + '/transfer.20161216.fee', 'a+')) as f2:
            for suffix in range(0,100):
                sql= str.format("select * from (select asset_id,asset_name,trans_id,remark,create_time,count(*) as count ,min(create_time) as minDate,max(create_time) as maxDate from product.t_assets_fee_%02d where remark = \"扣费节点\" and fee_node = 51 group by trans_id ) a where a.count > 2;" % (suffix))
                new_cursor.execute(sql)
                lists = new_cursor.fetchall()
                for list in lists:
                        tableName=str.format("product.t_assets_fee_%02d" % (suffix))
                        assetId=list["asset_id"]
                        assetName=list["asset_name"]
                        transId=list["trans_id"]
                        count=list["count"]
                        minDate=list["minDate"]
                        maxDate=list["maxDate"]
                        print(minDate)
                        print(maxDate)
                        if minDate.month != maxDate.month :
                            sql=str.format("select a.fee_suid,a.fee_duid,a.fee_amount,min(a.create_time) as req_time,b.dict_value as fee_name from %s a,asset.t_asset_dict  b where a.fee_type = b.dict_key and b.dict_category='fee_type' and a.trans_id = %d and a.create_time >= \"%s-%02d-%02d 00:00:00\" and a.create_time <= \"%s-%02d-%02d 23:59:59\" and  a.fee_node = 51 and a.operation = %d " % (tableName,transId,maxDate.year,maxDate.month,maxDate.day,maxDate.year,maxDate.month,maxDate.day,1))
                            new_cursor.execute(sql)
                            results=new_cursor.fetchall()
                            for result in results:
                                srcUser=result["fee_suid"]
                                dstUser=result["fee_duid"]
                                amount=result["fee_amount"]
                                reqTime=result["req_time"]
                                feeName=result["fee_name"]
                                if feeName == "(旧)融资服务费" :
                                    feeName="融资服务费"
                                if feeName == "(旧)贷后管理费" :
                                    feeName="贷后管理费"
                                if feeName == "(旧)进件服务费" :
                                    feeName="进件服务费"
                                if feeName == "(旧)咨询费（进件方）" :
                                    feeName = "咨询费(进件方)"
                                if feeName == "(旧)GPS使用费" :
                                    feeName = "GPS使用费"
                                if feeName == "(旧)咨询费（进件方）":
                                    feeName = "咨询费（进件方）"
                                sql=str.format("select mobile from user.t_user where id= %d" % srcUser)
                                new_cursor.execute(sql)
                                mobiles = new_cursor.fetchall()
                                for mobile in mobiles:
                                    phone=mobile["mobile"]
                                #print("tableName is "+tableName+",asset id is "+str(assetId)+",trans id is "+str(transId)+", count is "+str(count)+",minDate is "+str(minDate)+",maxDate is "+str(maxDate)+",amount is "+str(amount))
                                print("asset id is "+str(assetId)+",asset name is "+str(assetName)+",trans id is "+str(transId)+",reqTime is "+str(reqTime)+",srcUid is "+str(srcUser)+",电话:"+str(phone)+",dstUid is "+str(dstUser)+",金额 is "+str(amount//100)+",费用名称:"+str(feeName))

                                if phone in dict:
                                    fee=dict[phone]
                                    fee.setAmount(assetName, amount)
                                else:
                                    fee=Fee(phone)
                                    fee.setAmount(assetName, amount)
                                    dict[phone]=fee
            for phone,fee in dict.items():
                fee.getUnfreeText(f1)
                fee.getTransferText(f2)

            sum=0
            for phone,fee in dict.items():
                for key,value in fee.dict.items():
                    sum+=value
            print("sum="+str(sum))





        #sql=str.format("select frozen from account.t_user_account_%s where uid=%d and type =2 " % (str(srcUser)[-2:],srcUser))
        #new_cursor.execute(sql)
        #accountLists = new_cursor.fetchall()
        #for account in accountLists:
        #freeze=account["frozen"]
        #if freeze < amount:
        #        print("freeze < amount,uid = "+str(srcUser)+",feeze is "+str(freeze)+",amount is "+str(amount))

if __name__ == "__main__" :
    getCommFee()