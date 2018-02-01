def handler():
    with open('./handler', 'a+') as f:
        for idx in range(0,100):
            updateSql="update product.t_repayment_%02d set state = 3 where date(expect_date)<=date(now()) ;\n" % (idx)
            f.write(updateSql)
        updateSql="update product.t_repayments set state = 3 where date(expect_date)<=date(now()) ;\n"
        f.write(updateSql)


handler()
