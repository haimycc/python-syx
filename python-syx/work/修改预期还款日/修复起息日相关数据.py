import mysql.connector

new_conn = mysql.connector.connect(host='172.27.48.181', user='search', password='search@zyfax.com', database='product')
new_cursor = new_conn.cursor(dictionary=True)
backup = open('D:\\backupsql.txt', "w")
f = open('D:\\fixRepayData.txt', "w")


def updateSql(assetId, repayRows, payOffRows, investRows, updateTime):
    f.write("#还款表修复\n")
    for repayRow in repayRows:
        repaymentId = repayRow["repayment_id"]
        expectDate = repayRow["expect_date"]
        f.write(
            "UPDATE product.t_repayments  set expect_date = DATE_SUB(expect_date, INTERVAL 1 DAY) ,update_time='%s' where asset_id=%d and repayment_id=%d and expect_date='%s';\n" % (
                updateTime, assetId, repaymentId, expectDate))
        f.write(
            "UPDATE product.t_repayment_%s  set expect_date = DATE_SUB(expect_date, INTERVAL 1 DAY),update_time='%s' where asset_id =%d and repayment_id=%d and expect_date='%s';\n" % (
                str(repaymentId)[-2:], updateTime, assetId, repaymentId, expectDate))

    f.write("#回款表修复\n")
    for payOffRow in payOffRows:
        investmentId = payOffRow["investment_id"]
        expectDate = payOffRow["expect_date"]
        f.write(
            "UPDATE invest.t_investment_payoffs  set expect_date = DATE_SUB(expect_date, INTERVAL 1 DAY),update_time='%s' where asset_id = %d AND investment_id = %s and expect_date='%s' ;\n" % (
                updateTime, assetId, investmentId, expectDate))
        f.write(
            "UPDATE invest.t_investment_payoff_%s  set expect_date = DATE_SUB(expect_date, INTERVAL 1 DAY),update_time='%s' WHERE asset_id = %d AND investment_id = %s and expect_date='%s';\n" % (
                str(investmentId)[-2:], updateTime,assetId, investmentId, expectDate))

    f.write("#投资表修复\n")
    for investRow in investRows:
        investmentId = investRow["investment_id"]
        nextPayoffDay = investRow["next_payoff_day"]
        f.write(
            "UPDATE invest.t_investments set next_payoff_day = DATE_SUB(next_payoff_day, INTERVAL 1 DAY),update_time='%s' "
            "where asset_id = %s AND investment_id = %s and next_payoff_day='%s';\n" % (
                updateTime, assetId, investmentId, nextPayoffDay))
        f.write(
            "UPDATE invest.t_investment_%s set next_payoff_day = DATE_SUB(next_payoff_day, INTERVAL 1 DAY),update_time='%s' "
            "where asset_id = %s AND investment_id = %s and next_payoff_day='%s';\n" % (
                str(investmentId)[-2:], updateTime, assetId, investmentId, nextPayoffDay))
        f.write(
            "update product.t_investment_%s set next_payoff_day=DATE_SUB(next_payoff_day, INTERVAL 1 DAY),update_time='%s' where asset_id=%d and investment_id=%d and next_payoff_day='%s';\n" % (
                str(assetId)[-2:], updateTime, assetId, investmentId, nextPayoffDay))


def backUpSql(assetId, repayRows, payOffRows, investRows):
    backup.write("#还款表备份\n")
    for repayRow in repayRows:
        repaymentId = repayRow["repayment_id"]
        expectDate = repayRow["expect_date"]
        backup.write(
            "SELECT * FROM product.t_repayments where asset_id=%d and repayment_id=%d and expect_date='%s';\n" % (
            assetId, repaymentId, expectDate))
        backup.write(
            "SELECT * FROM product.t_repayment_%s where asset_id=%d and repayment_id=%d and expect_date='%s';\n" % (
            str(repaymentId)[-2:], assetId, repaymentId, expectDate))

    backup.write("#回款表备份\n")
    for payOffRow in payOffRows:
        investmentId = payOffRow["investment_id"]
        expectDate = payOffRow["expect_date"]
        backup.write(
            "SELECT * FROM invest.t_investment_payoffs WHERE asset_id=%d and investment_id=%d and expect_date='%s';\n" % (
            assetId, investmentId, expectDate))
        backup.write(
            "SELECT * FROM invest.t_investment_payoff_%s WHERE asset_id = %d AND investment_id = %d and expect_date='%s';\n" % (
                str(investmentId)[-2:], assetId, investmentId, expectDate))

    backup.write("#投资表备份\n")
    for investRow in investRows:
        investmentId = investRow["investment_id"]
        nextPayoffDay = investRow["next_payoff_day"]
        backup.write(
            "select * from invest.t_investments where asset_id=%d and investment_id=%d and next_payoff_day='%s';\n" % (
            assetId, investmentId, nextPayoffDay))
        backup.write(
            "SELECT * FROM invest.t_investment_%s WHERE asset_id = %d AND investment_id = %s and next_payoff_day='%s';\n" % (
                str(investmentId)[-2:], assetId, investmentId, nextPayoffDay))
        backup.write(
            "SELECT * from product.t_investment_%s where asset_id=%d and investment_id=%d and next_payoff_day='%s';\n" % (
                str(assetId)[-2:], assetId, investmentId, nextPayoffDay))


def fun():
    assetId = 26355055020202382

    repaySql = "SELECT * FROM product.t_repayments where asset_id=%d;" % (assetId);
    new_cursor.execute(repaySql)
    repayRows = new_cursor.fetchall()

    payOffSql = "SELECT * FROM invest.t_investment_payoffs WHERE asset_id=%d;\n" % (assetId)
    new_cursor.execute(payOffSql)
    payOffRows = new_cursor.fetchall()

    investSql = "SELECT * FROM invest.t_investments WHERE asset_id=%d;\n" % (assetId)
    new_cursor.execute(investSql)
    investRows = new_cursor.fetchall()

    backUpSql(assetId, repayRows, payOffRows, investRows)
    updateSql(assetId, repayRows, payOffRows, investRows, '2018-05-14 20:45:00')

    backup.close()
    f.close()


fun()