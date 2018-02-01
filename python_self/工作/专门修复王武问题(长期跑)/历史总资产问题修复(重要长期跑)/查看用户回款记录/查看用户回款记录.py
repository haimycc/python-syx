import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def getUserPayoff():
    loanPrincipal=0
    loanInterest=0
    loanAddInterest=0
    planPrincipal=0
    planInterest=0
    planAddInterest=0
    with open("userinfo.csv", "a+") as f:
        f.write("标的ID,标的名称,是否定期理财,是否理财计划,投资记录ID,投资总金额,投资时间,第几期回款,预计本金,预计利息,预计加息,预计时间,是否已经回款\n")
        userSql="select id from user.t_user where mobile=13278763202"
        new_cursor.execute(userSql)
        userLists = new_cursor.fetchall()
        for userList in userLists:
            userId=userList["id"]
            print("用户uid等于%d"%(userId))
            # 定期理财回款:
            loanSql="select asset_id,asset_name,investment_id,amount,create_time from invest.t_investment_%s where investor_uid = %d and state in (4) and asset_type = 0 and asset_pool = 1 " % (str(userId)[-2:],userId)
            new_cursor.execute(loanSql)
            invests = new_cursor.fetchall()
            for invest in invests:
               assetId=invest["asset_id"]
               assetName=invest["asset_name"]
               investId=invest["investment_id"]
               amount=invest["amount"]
               investTime=invest["create_time"]
               payoffSql="select * from invest.t_investment_payoffs where investment_id= %d and asset_type = 0 and asset_pool = 1 and state not in (1,3)" % (investId)
               new_cursor.execute(payoffSql)
               payoffs = new_cursor.fetchall()
               for payoff in payoffs:
                   phase=payoff["phase"]
                   expectPrincipal=payoff["expect_principal"]
                   expectInterest=payoff["expect_interest"]
                   expectAddInterest=payoff["expect_add_interest"]
                   expectTime=payoff["expect_date"]
                   state=payoff["state"]
                   if int(state) == 1 or int(state) == 3:
                       state="已回款"
                       break
                   else :
                       state="未回款"
                   isLoan="是"
                   isFinancial="否"
                   f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" %
                           (str(assetId),str(assetName),isLoan,isFinancial,str(investId),str(amount),str(investTime),
                            str(phase),str(expectPrincipal),str(expectInterest),str(expectAddInterest),str(expectTime),str(state)))
                   loanPrincipal += expectPrincipal
                   loanInterest += expectInterest
                   loanAddInterest += expectAddInterest

            # 未满标生产回款的定期理财
            loansql2="select asset_id,asset_name,investment_id,amount,create_time from invest.t_investment_%s where investor_uid = %d and state in (2) and asset_type = 0 and asset_pool = 1 " % (str(userId)[-2:],userId)
            new_cursor.execute(loansql2)
            invests = new_cursor.fetchall()
            for invest in invests:
                assetId=invest["asset_id"]
                assetName=invest["asset_name"]
                investId=invest["investment_id"]
                amount=invest["amount"]
                investTime=invest["create_time"]
                state="未回款"
                isLoan = "是"
                isFinancial = "否"
                f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" %
                    (str(assetId), str(assetName), isLoan, isFinancial, str(investId), str(amount), str(investTime),
                     str(0), str(amount), str(0), str(0), str("未满标"),
                     str(state)))
                loanPrincipal += amount

            #理财计划
            FinanSql="select asset_id,asset_name,investment_id,amount,create_time from invest.t_investment_%s where investor_uid = %d and state in (4) and asset_type = 1 and asset_property &  65536 != 65536 " % (str(userId)[-2:],userId)
            new_cursor.execute(FinanSql)
            invests = new_cursor.fetchall()
            for invest in invests:
                assetId = invest["asset_id"]
                assetName = invest["asset_name"]
                investId = invest["investment_id"]
                amount = invest["amount"]
                investTime = invest["create_time"]
                payoffSql = "select * from specialDB.t_new_financial_plan_payoff where investment_id=%d" % (investId)
                new_cursor.execute(payoffSql)
                payoffs = new_cursor.fetchall()
                for payoff in payoffs:
                    phase = 1
                    expectPrincipal = payoff["expect_principal"]
                    expectInterest = payoff["expect_interest"]
                    expectAddInterest = payoff["expect_add_interest"]
                    expectTime = payoff["expect_date"]
                    state = payoff["state"]
                    if int(state) == 1 or int(state) == 3:
                        state = "已回款"
                        break
                    else:
                        state = "未回款"
                    isLoan = "否"
                    isFinancial = "是"
                    f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" %
                        (str(assetId), str(assetName), isLoan, isFinancial, str(investId), str(amount), str(investTime),
                        str(phase), str(expectPrincipal), str(expectInterest), str(expectAddInterest), str(expectTime), str(state)))
                    planPrincipal += expectPrincipal
                    planInterest +=expectInterest
                    planAddInterest +=expectAddInterest

            #未满标生产回款的理财计划
            FinanSql2="select asset_id,asset_name,investment_id,amount,create_time from invest.t_investment_%s where investor_uid = %d and state in (2) and asset_type = 1 and asset_property &  65536 != 65536 " % (str(userId)[-2:],userId)
            new_cursor.execute(FinanSql2)
            invests = new_cursor.fetchall()
            for invest in invests:
                assetId = invest["asset_id"]
                assetName = invest["asset_name"]
                investId = invest["investment_id"]
                amount = invest["amount"]
                investTime = invest["create_time"]
                state = "未回款"
                isLoan = "否"
                isFinancial = "是"
                f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" %
                        (str(assetId), str(assetName), isLoan, isFinancial, str(investId), str(amount), str(investTime),
                         str(0), str(amount), str(0), str(0), str("未满标"),
                         str(state)))
                planPrincipal += expectPrincipal
                planInterest += 0
                planAddInterest += 0
    print("定期理财待收本金:%d,待收利息:%d,待收加息:%d" % (loanPrincipal,loanInterest,loanAddInterest))
    print("理财计划待收本金:%d,待收利息:%d,待收加息:%d" % (planPrincipal,planInterest,planAddInterest))
    sum=(loanPrincipal+loanInterest+loanAddInterest+planPrincipal+planInterest+planAddInterest)
    print("用户待收本息:%d"%(sum))




if __name__ == "__main__" :
    getUserPayoff()