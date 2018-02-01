def updateSql():
    for id in range(100):
        sql = "update t_repayment_%02d set state = state + 10 where state in (0,1,4) " % (id)
        print(sql + ";")

updateSql()

def updateSql2():
    for id in range(100):
        sql = "update t_repayment_%02d set state = state - 10 where state in (10,11,14)" % (id)
        print(sql + ";")

updateSql2()
