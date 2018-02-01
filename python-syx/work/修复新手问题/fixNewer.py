# 修改新手状态

def updateSql(userId, assetId):
    f = open("updateNewerSql.txt", "w")
    investorIdSuffix = str(userId)[-3:]
    sql = "update user.t_user_attr_%s set value=0 where userid=%d and name='isnew';" % (investorIdSuffix, userId)
    print(sql)
    investorIdSuffix = str(userId)[-2:]
    sql2 = "update invest.t_investment_%s set state=3 where investor_uid=%d and asset_id=%d;" % (investorIdSuffix, userId, assetId)
    print(sql2)
    sql3 = "update invest.t_investments set state=3 where investor_uid=%d and asset_id=%d;" % (userId, assetId)
    print(sql3)
    f.write(sql + "\n" + sql2 + "\n" + sql3)


updateSql(201609230000004000, 20170105000014329)

def test(assetId):
    sql = "select * from asset.t_asset where assetId= %02s " % (str(0))
    print(sql)

test(0)