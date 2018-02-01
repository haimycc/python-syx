file = open("D:\加索引sql.txt", "w")
def addIndex():
    sql1 = "ALTER TABLE financial_plan.t_new_financial_plan_payoff_%02d ADD INDEX index_update_time (update_time);"
    sql2 = "ALTER TABLE invest.t_investment_payoff_%02d ADD INDEX index_update_time (update_time);"

    for i in range(100):
        s1 = sql1 % (i);
        file.write(s1 + "\n")
    for j in range(100):
        s2 = sql2 % (j);
        file.write(s2 + "\n")
    file.close()

addIndex()
