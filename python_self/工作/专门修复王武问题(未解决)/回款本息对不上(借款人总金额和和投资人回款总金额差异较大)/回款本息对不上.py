import os

import mysql.connector

new_conn = mysql.connector.connect(host='192.168.50.151', user='search', password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)


def payffNotRight():
    assetId = 999967416621810837
    sum = 0
    for phase in range(5, 13):
        # 该期还款
        sql = str.format(
            "select * from product.t_repayment_%s where asset_id=%d and expect_date>='2016-12-28 00:00:00' and phase=%d" % (
            str(assetId)[-2:], assetId, phase))
        new_cursor.execute(sql)
        repays = new_cursor.fetchall()
        for repay in repays:
            expectPrincipal = repay["expect_principal"]
            expectInterest = repay["expect_interest"]
            # 找到该期的投资回款
            payoffPrincipals=0
            payoffInterests=0
            for suffix in range(0, 100):
                payoffSql = str.format(
                    "select * from invest.t_investment_payoff_%02d where asset_id=%d and expect_date>='2016-12-28 00:00:00' and phase = %d " % (suffix, assetId,phase))
                new_cursor.execute(payoffSql)
                payoffs = new_cursor.fetchall()
                for payoff in payoffs:
                    payoffPrincipal = payoff["expect_principal"]
                    payoffInterest = payoff["expect_interest"]
                    payoffPrincipals+=payoffPrincipal
                    payoffInterests+=payoffInterest
        print("phase in end,repayexpectPrincipal is %d,repayexpectInterest is %d,payoffPrincipals is %d,payoffInterests is %d " % (expectPrincipal,expectInterest,payoffPrincipals,payoffInterests))




if __name__ == "__main__":
    payffNotRight()
