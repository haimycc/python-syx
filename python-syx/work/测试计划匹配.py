#                       使用说明
#在getMatchData(xxx)填入计划名称中的数字部分
#例如智投DD-18051408 则填入getMatchData(18051408)
#查看数据中
# financial_plan_account>=设定值的部分
# 累加是否和页面中的当日未匹配资金价值相等

import mysql.connector

#173,74环境配置
new_conn = mysql.connector.connect(host='192.168.9.173', user='mysqluser', password='mysqluser@zyxr.com', database='product')
#101-103环境配置
# new_conn = mysql.connector.connect(host='10.3.100.103', user='mysqluser', password='mysqluser@zyxr.com', database='product')
new_cursor = new_conn.cursor(dictionary=True)


def getOne(sql, *args):
    new_cursor.execute(sql)
    return new_cursor.fetchone()


def getAll(sql, *args):
    new_cursor.execute(sql)
    return new_cursor.fetchall()

def getMatchData(planName):
    getPlanId = "SELECT asset_id FROM product.t_assets WHERE asset_name='%s'" % (planName)
    planId = getOne(getPlanId)['asset_id']
    assetInvestInfoSql = \
        """
        SELECT
        investment_id
        FROM
        product.t_investment_%s
        WHERE
        asset_type IN (1, 4)
        AND asset_id = %s
        AND state IN (2, 4)
        AND asset_state IN (8, 9)
        AND debt_property IN (0, 1)
        AND financial_plan_account > 0
        """ % (str(planId)[-2:], planId)
    # print(assetInvestInfoSql)
    assetInvestInfoList = getAll(assetInvestInfoSql)
    for list in assetInvestInfoList:
        getInvestInfoSql = \
            """
            SELECT
            financial_plan_id,investment_id,asset_id,debt_property,financial_plan_account,match_state,investor_uid
            FROM
            invest.t_investment_%s
            WHERE
            investment_id =%s
            """ % (str(list['investment_id'])[-2:], list['investment_id'])
        # print(getInvestInfoSql)
        one = getOne(getInvestInfoSql)
        print(one)

if __name__ == '__main__':
    #填入计划名称
    getMatchData(18051408)
