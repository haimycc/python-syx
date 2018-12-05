from sqlMoudle.sqlTemplate import *


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
        # getHoldAsset(one['financial_plan_id'], one['investor_uid'], one['investment_id'], one['financial_plan_account'])


# 获取持有资产个数
def getHoldAsset(financialPlanId, investorUid, financialPlanInvestmentId, money):
    sql = \
        """
        SELECT
        *
        FROM invest.t_investments WHERE
	    financial_plan_id = %s
        AND investor_uid = %s
        AND financial_plan_investment_id = %s
        AND asset_type = 0 AND asset_pool IN (2, 4)
        AND ((asset_state = 5 AND state = 2) OR (asset_state IN (8, 9) AND state = 4))
        AND investment_id NOT IN (
	    SELECT investment_id FROM
		    (SELECT investment_id,
				SUM(CASE WHEN state = 0 THEN 1 ELSE 0 END) AS holdnum
			FROM invest.t_investment_payoffs WHERE
				financial_plan_id = %s
			AND investor_uid = %s
			AND financial_plan_investment_id = %s
			AND asset_type = 0
			AND asset_pool IN (2, 4)
			GROUP BY investment_id
			HAVING holdnum = 0) t)
        """ % (financialPlanId, investorUid, financialPlanInvestmentId, financialPlanId, investorUid,
               financialPlanInvestmentId)
    # print(sql)
    if (money < 5000):
        return
    investInfo_list = getAll(sql)
    if (len(investInfo_list) > 0):
        print(financialPlanId)
        print(investorUid)
        print(financialPlanInvestmentId)
        print(investInfo_list)
        # if (int(investInfo_list['financial_plan_account']) > 50000):
        #     print(investInfo_list)

        # print(investInfo_list)


if __name__ == '__main__':
    getMatchData(18110101)
