import os
import mysql.connector

new_conn = mysql.connector.connect(host='192.168.50.151', user='search', password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)


if __name__ == "__main__" :
    with open("./insertSqls2","a+") as f:
        #找到分表有，总表没有的
        for suffix in range(0,100):
            sql=str.format("select a.payoff_id as a_id,b.payoff_id as b_id from invest.t_investment_payoff_%02d a left join invest.t_investment_payoffs b on a.payoff_id=b.payoff_id" % (suffix))
            new_cursor.execute(sql)
            investIds = new_cursor.fetchall()
            for investId in investIds:
                aId=investId["a_id"]
                bId=investId["b_id"]
                if aId != bId :
                    #aId就是investment id
                    sql=str.format("insert into invest.t_investment_payoffs ( "
                                   "payoff_id,"
                                   "financial_plan_id,"
                                   "investment_id,"
                                   "financial_plan_investment_id,"
                                   "asset_id,"
                                   "asset_name,"
                                   "asset_type,"
                                   "asset_pool,"
                                   "investor_uid,"
                                   "borrower_uid,"
                                   "amount,"
                                   "annual_rate,"
                                   "add_rate,"
                                   "repayment_id,"
                                   "phase,"
                                   "expect_principal,"
                                   "expect_interest,"
                                   "expect_add_interest,"
                                   "expect_pay_platform,"
                                   "expect_date,"
                                   "actual_principal,"
                                   "actual_interest,"
                                   "actual_add_interest,"
                                   "actual_pay_platform,"
                                   "actual_date,"
                                   "state,"
                                   "property,"
                                   "update_time,"
                                   "create_time"
                                   ")"
                                   "select "
                                   "payoff_id,"
                                   "financial_plan_id,"
                                   "investment_id,"
                                   "financial_plan_investment_id,"
                                   "asset_id,"
                                   "asset_name,"
                                   "asset_type,"
                                   "asset_pool,"
                                   "investor_uid,"
                                   "borrower_uid,"
                                   "amount,"
                                   "annual_rate,"
                                   "add_rate,"
                                   "repayment_id,"
                                   "phase,"
                                   "expect_principal,"
                                   "expect_interest,"
                                   "expect_add_interest,"
                                   "expect_pay_platform,"
                                   "expect_date,"
                                   "actual_principal,"
                                   "actual_interest,"
                                   "actual_add_interest,"
                                   "actual_pay_platform,"
                                   "actual_date,"
                                   "state,"
                                   "property,"
                                   "update_time,"
                                   "create_time "
                                   "from invest.t_investment_payoff_%s where payoff_id=%d ;\n" % (str(aId)[-2:],aId))
                    f.write(sql)



