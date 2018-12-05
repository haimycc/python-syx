from sqlMoudle.sqlTemplate import *


def getFailedData():
    getSql = "SELECT * FROM trustee.t_trustee_request_order_038 WHERE user_id=253722046203009138 AND state=1 AND remark ='双节钜惠返现奖励'  AND DATE(create_time)='2018-10-26' ORDER BY  create_time;"
    res = getAll(getSql)
    a = 0
    for s in res:
        if '可用余额不足' in s['response']:
            a = a + 1

    print(a)
# state:0初始化 1成功 2失败
getFailedData()
