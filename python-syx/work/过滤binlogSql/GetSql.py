file = open("D:\sql3.txt", "r")
f = open('D:\sql4.txt', "w")
saveList = ("insert", "INSERT", "update", "UPDATE")

nolist = ("update t_coupon_interest_task_", "insert into t_operation_log", "insert into financial_plan.t_new_financial_plan_payoff_", "update_time datetime", "INSERT INTO invest.t_investments", "insert into t_login_history", "update invest.t_investment_sums a", "update account.t_id_config", "update `lock`.`t_grouplock'", "update t_login_history", "update `lock`.`t_grouplock`")
notList = ("insert into trustee.t_trustee_request_flow_", "update financial_plan.t_investment_", "update invest.t_investments a, invest.t_investment_", "insert into invest.t_investment_", "update invest.t_investment_sum_", "insert into product.t_repayment_flow_", "insert into financial.t_financial_earning_record_")
addList = ("insert into trustee.t_trustee_request_flow_025", "update financial_plan.t_investment_07", "update invest.t_investments a, invest.t_investment_25", "insert into invest.t_investment_25", "update invest.t_investment_sum_25", "insert into product.t_repayment_flow_25", "insert into financial.t_financial_earning_record_25")
while 1:
    # 用缓存效率提高3倍
    lines = file.readline(100000)
    if lines.startswith(saveList):
        if lines.startswith(nolist):
            continue
        else:
            if not lines.startswith(notList) | lines.startswith(addList):
                f.write(lines + "\n")
    elif not lines:
        break
    else:
        continue
file.close()
f.close()
