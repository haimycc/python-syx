import os
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.51.145',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)
columns = "financial_plan_id,investment_id,financial_plan_investment_id,asset_id,asset_type,asset_pool,asset_state,asset_property,asset_name,annual_rate,add_rate,phase_total,phase_mode,repay_mode,contract_no,debt_id,debt_name,investor_uid,borrower_uid,amount,valid_amount,percentage,init_percentage,conpon_id,conpon_type,state,debt_property,from_device,rest_phase,expect_principal,expect_interest,expect_add_interest,expect_pay_platform,received_principal,received_interest,received_add_interest,actual_pay_platform,received_money,next_payoff_day,lock_day,update_time,create_time,finish_time,full_time"


#读取新老数据库投资记录ID
def readFile():
    infos=[]
    with open('./oldInvestmentToNewInvestment', 'r') as f:
        for line in f.readlines():
            info=line.split(",")
            infos.append(info)
    return infos

def selectOldInvestment(lists):
    for line in lists:
        borrowerName=line[0]
        borrowerUid=
        oldInvestor=line[0]
        oldInvestmentId=line[1]
        newIvnestor=line[2]
        newInvestmentId=line[3]
        #旧投资记录ID
        oldSuffix=oldInvestor[-2:]
        #旧投资记录
        selectSql="select * from invest.t_investment_%s where investment_id=%s and investor_uid=%s;" % (oldSuffix,oldInvestmentId,oldInvestor)
        new_cursor.execute(selectSql)
        results = new_cursor.fetchall()
        for result in results:
            financial_plan_id=result['financial_plan_id']
            investment_id=result['investment_id']
            financial_plan_investment_id=result['financial_plan_investment_id']
            asset_id=result['asset_id']
            asset_type=result['asset_type']
            asset_pool=result['asset_pool']
            asset_state=result['asset_state']
            asset_state = result['asset_state']
            asset_property = result['asset_property']
            asset_name = result['asset_name']
            annual_rate = result['annual_rate']
            add_rate = result['add_rate']
            phase_total = result['phase_total']
            phase_mode = result['phase_mode']
            repay_mode = result['repay_mode']
            contract_no = result['contract_no']
            debt_id = result['debt_id']
            debt_name = result['debt_name']
            investor_uid = result['investor_uid']
            borrower_uid = result['borrower_uid']
            amount = result['amount']
            valid_amount = result['valid_amount']
            percentage = result['percentage']
            init_percentage = result['init_percentage']
            conpon_id = result['conpon_id']
            conpon_type = result['conpon_type']
            state = result['state']
            debt_property = result['debt_property']
            from_device = result['from_device']
            rest_phase = result['rest_phase']
            expect_principal = result['expect_principal']
            expect_interest = result['expect_interest']
            expect_add_interest = result['expect_add_interest']
            expect_pay_platform = result['expect_pay_platform']
            received_principal = result['received_principal']
            received_interest = result['received_interest']
            received_add_interest = result['received_add_interest']
            actual_pay_platform = result['actual_pay_platform']
            received_money = result['received_money']
            next_payoff_day = result['next_payoff_day']
            if next_payoff_day == None :
                next_payoff_day = "0000-00-00 00:00:00"
            lock_day = result['lock_day']
            update_time = result['update_time']
            if update_time == None :
                update_time = "0000-00-00 00:00:00"
            create_time = result['create_time']
            if create_time == None :
                create_time = "0000-00-00 00:00:00"
            finish_time = result['finish_time']
            if finish_time == None :
                finish_time = "0000-00-00 00:00:00"
            full_time = result['full_time']
            if full_time == None :
                full_time = "0000-00-00 00:00:00"

            investIdSuffix=int(newInvestmentId)%100
            assetIdSuffix=asset_id%100
            financialPlanIdSuffix=financial_plan_id%100
            insertSql1="insert into invest.t_investment_%02d (%s) values (" \
                       "%d,%d,%d,%d,%d,%d,%d,%d,'%s',%d,%d,%d,%d,%d,'%s',%d,'%s',%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,'%s',%d,'%s','%s','%s','%s') " % \
                       (investIdSuffix,columns,
                        financial_plan_id,
                        int(newInvestmentId),
                        financial_plan_investment_id,
                        asset_id,
                        asset_type,
                        asset_pool,
                        asset_state,
                        asset_property,
                        asset_name,
                        annual_rate,
                        add_rate,
                        phase_total,
                        phase_mode,
                        repay_mode,
                        contract_no,
                        debt_id,
                        debt_name,
                        int(newIvnestor),
                        borrower_uid,
                        amount,
                        valid_amount,
                        percentage,
                        init_percentage,
                        conpon_id,
                        conpon_type,
                        state,
                        debt_property,
                        from_device,
                        rest_phase,
                        expect_principal,
                        expect_interest,
                        expect_add_interest,
                        expect_pay_platform,
                        received_principal,
                        received_interest,
                        received_add_interest,
                        actual_pay_platform,
                        received_money,
                        next_payoff_day,
                        lock_day,
                        update_time,
                        create_time,
                        finish_time,
                        full_time)
            insertSql2="insert into invest.t_investments (%s) values (" \
                       "%d,%d,%d,%d,%d,%d,%d,%d,'%s',%d,%d,%d,%d,%d,'%s',%d,'%s',%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,'%s',%d,'%s','%s','%s','%s') " % \
                       (columns,
                        financial_plan_id,
                        int(newInvestmentId),
                        financial_plan_investment_id,
                        asset_id,
                        asset_type,
                        asset_pool,
                        asset_state,
                        asset_property,
                        asset_name,
                        annual_rate,
                        add_rate,
                        phase_total,
                        phase_mode,
                        repay_mode,
                        contract_no,
                        debt_id,
                        debt_name,
                        int(newIvnestor),
                        borrower_uid,
                        amount,
                        valid_amount,
                        percentage,
                        init_percentage,
                        conpon_id,
                        conpon_type,
                        state,
                        debt_property,
                        from_device,
                        rest_phase,
                        expect_principal,
                        expect_interest,
                        expect_add_interest,
                        expect_pay_platform,
                        received_principal,
                        received_interest,
                        received_add_interest,
                        actual_pay_platform,
                        received_money,
                        next_payoff_day,
                        lock_day,
                        update_time,
                        create_time,
                        finish_time,
                        full_time)
            insertSql3="insert into product.t_investment_%02d (%s) values (" \
                       "%d,%d,%d,%d,%d,%d,%d,%d,'%s',%d,%d,%d,%d,%d,'%s',%d,'%s',%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,'%s',%d,'%s','%s','%s','%s') " % \
                       (assetIdSuffix,columns,
                        financial_plan_id,
                        int(newInvestmentId),
                        financial_plan_investment_id,
                        asset_id,
                        asset_type,
                        asset_pool,
                        asset_state,
                        asset_property,
                        asset_name,
                        annual_rate,
                        add_rate,
                        phase_total,
                        phase_mode,
                        repay_mode,
                        contract_no,
                        debt_id,
                        debt_name,
                        int(newIvnestor),
                        borrower_uid,
                        amount,
                        valid_amount,
                        percentage,
                        init_percentage,
                        conpon_id,
                        conpon_type,
                        state,
                        debt_property,
                        from_device,
                        rest_phase,
                        expect_principal,
                        expect_interest,
                        expect_add_interest,
                        expect_pay_platform,
                        received_principal,
                        received_interest,
                        received_add_interest,
                        actual_pay_platform,
                        received_money,
                        next_payoff_day,
                        lock_day,
                        update_time,
                        create_time,
                        finish_time,
                        full_time)
            insertSql4="insert into financial_plan.t_investment_%02d (%s) values (" \
                       "%d,%d,%d,%d,%d,%d,%d,%d,'%s',%d,%d,%d,%d,%d,'%s',%d,'%s',%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,'%s',%d,'%s','%s','%s','%s') " % \
                       (financialPlanIdSuffix,columns,
                        financial_plan_id,
                        int(newInvestmentId),
                        financial_plan_investment_id,
                        asset_id,
                        asset_type,
                        asset_pool,
                        asset_state,
                        asset_property,
                        asset_name,
                        annual_rate,
                        add_rate,
                        phase_total,
                        phase_mode,
                        repay_mode,
                        contract_no,
                        debt_id,
                        debt_name,
                        int(newIvnestor),
                        borrower_uid,
                        amount,
                        valid_amount,
                        percentage,
                        init_percentage,
                        conpon_id,
                        conpon_type,
                        state,
                        debt_property,
                        from_device,
                        rest_phase,
                        expect_principal,
                        expect_interest,
                        expect_add_interest,
                        expect_pay_platform,
                        received_principal,
                        received_interest,
                        received_add_interest,
                        actual_pay_platform,
                        received_money,
                        next_payoff_day,
                        lock_day,
                        update_time,
                        create_time,
                        finish_time,
                        full_time)
            print(insertSql1)
            print(insertSql2)
            print(insertSql3)
            print(insertSql4)

            #设置老的投资记录的状态的下单失败
            updateSql1="update invest.t_investment_%s set state=3 where investment_id=%s and asset_id=%d ;" % (oldSuffix,oldInvestmentId,asset_id)
            updateSql2="update invest.t_investments set state=3 where investment_id=%s and asset_id=%d ;" % (oldInvestmentId,asset_id)
            updateSql3="update product.t_investment_%02d set state=3 where investment_id=%s and asset_id=%d ;" % (assetIdSuffix,oldInvestmentId,asset_id)
            updateSql4="update financial_plan.t_investment_%02d set state=3 where investment_id=%s and asset_id=%d ;" % (financialPlanIdSuffix,oldInvestmentId,asset_id)

            print(updateSql1)
            print(updateSql2)
            print(updateSql3)
            print(updateSql4)


if '__main__' == __name__:
    selectOldInvestment(readFile())



