import mysql.connector
import json

new_conn = mysql.connector.connect(host='192.168.31.222', user='root', password='123456', database='product')
new_cursor = new_conn.cursor(dictionary=True)

file = open("D:\dd.txt", "r", encoding="utf-8")
f = open("D:\www.txt", "a")


def handler(update_sql, select_sql):
    while 1:
        lines = file.readline()
        if lines == "":
            break
        loads = json.loads(lines)
        id_ = select_sql % (str(loads["investmentId"]))
        print(id_)
        new_cursor.execute(id_)
        fetchall = new_cursor.fetchone()
        invest_sql = update_sql % (
            str(loads["receivedInterest"]),
            str(loads["receivedAddInterest"]),
            str(loads["actualPayPlatform"]),
            str(loads["receivedMoney"]),
            str(loads["investmentId"]),
            str(fetchall["asset_state"]),
            str(fetchall["rest_phase"]),
            str(fetchall["received_interest"]),
            str(fetchall["received_add_interest"]),
            str(fetchall["actual_pay_platform"]),
            str(fetchall["received_money"])
        )
        f.writelines(invest_sql + "\n")


def handerPer(update_sql, select_sql):
    while 1:
        lines = file.readline()
        if lines == "":
            break
        loads = json.loads(lines)
        id_ = select_sql % (int(str(loads["investmentId"])[-2:]), str(loads["investmentId"]))
        print(id_)
        new_cursor.execute(id_)
        fetchall = new_cursor.fetchone()
        invest_sql = update_sql % (
            int(str(loads["investmentId"])[-2:]),
            str(loads["receivedInterest"]),
            str(loads["receivedAddInterest"]),
            str(loads["actualPayPlatform"]),
            str(loads["receivedMoney"]),
            str(loads["investmentId"]),
            str(fetchall["asset_state"]),
            str(fetchall["rest_phase"]),
            str(fetchall["received_interest"]),
            str(fetchall["received_add_interest"]),
            str(fetchall["actual_pay_platform"]),
            str(fetchall["received_money"])
        )
        f.writelines(invest_sql + "\n")


update_invest_sql = "UPDATE invest.t_investment_%02d" \
                    " SET asset_state=8, rest_phase=1," \
                    " received_interest=%s, received_add_interest=%s, actual_pay_platform=%s, received_money=%s," \
                    " update_time=now() WHERE investment_id=%s and asset_id=20170804000239841" \
                    " and asset_state=%s and rest_phase=%s and received_interest=%s and received_add_interest=%s and actual_pay_platform=%s and received_money=%s;"

select_sql = "select asset_state,rest_phase,received_interest,received_add_interest,actual_pay_platform,received_money " \
             "from invest.t_investment_%02d where investment_id=%s and asset_id=20170804000239841 "

update_investS_sql = "UPDATE invest.t_investments" \
                     " SET asset_state=8, rest_phase=1," \
                     " received_interest=%s, received_add_interest=%s, actual_pay_platform=%s, received_money=%s," \
                     " update_time=now() WHERE investment_id=%s and asset_id=20170804000239841" \
                     " and asset_state=%s and rest_phase=%s and received_interest=%s and received_add_interest=%s and actual_pay_platform=%s and received_money=%s;"

s2_sql = "select asset_state,rest_phase,received_interest,received_add_interest,actual_pay_platform,received_money " \
         "from invest.t_investments where investment_id=%s and asset_id=20170804000239841 "

update_financial_sql = "UPDATE financial_plan.t_investment_00" \
                       " SET asset_state=8, rest_phase=1," \
                       " received_interest=%s, received_add_interest=%s, actual_pay_platform=%s, received_money=%s," \
                       " update_time=now() WHERE investment_id=%s and asset_id=20170804000239841" \
                       " and asset_state=%s and rest_phase=%s and received_interest=%s and received_add_interest=%s and actual_pay_platform=%s and received_money=%s;"
s3_sql = "select asset_state,rest_phase,received_interest,received_add_interest,actual_pay_platform,received_money " \
         "from financial_plan.t_investment_00 where investment_id=%s and asset_id=20170804000239841 "

update_product_sql = "UPDATE product.t_investment_41" \
                     " SET asset_state=8, rest_phase=1," \
                     " received_interest=%s, received_add_interest=%s, actual_pay_platform=%s, received_money=%s," \
                     " update_time=now() WHERE investment_id=%s and asset_id=20170804000239841" \
                     " and asset_state=%s and rest_phase=%s and received_interest=%s and received_add_interest=%s and actual_pay_platform=%s and received_money=%s;"

s4_sql = "select asset_state,rest_phase,received_interest,received_add_interest,actual_pay_platform,received_money " \
         "from product.t_investment_41 where investment_id=%s and asset_id=20170804000239841 "

# handerPer(update_invest_sql, select_sql)
# handler(update_investS_sql, s2_sql)
# handler(update_financial_sql, s3_sql)
handler(update_product_sql, s4_sql)

file.close()
f.close()
