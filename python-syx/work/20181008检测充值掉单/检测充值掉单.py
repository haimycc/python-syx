from sqlMoudle.sqlTemplate import *


def getOrderState(moblie, orderId):
    getUidSql = "SELECT id FROM `user`.t_user where mobile='%s';" % (moblie)
    uid = getOne(getUidSql)['id']
    getRechageSql = "SELECT order_id, response,create_time,state,user_id FROM trustee.t_trustee_request_order_0%02d WHERE user_id=%d and order_id=%d  ORDER BY create_time DESC;"
    # getRechageSql = "SELECT * FROM trustee.t_trustee_request_order_0%02d WHERE user_id=%d and order_id=%d  ORDER BY create_time DESC;"
    sql = str(getRechageSql) % (uid % 100, uid, orderId)
    # print(sql)
    res = getOne(sql)
    print(res)


# 1 成功 2失败 3处理中
getOrderState(13698760118, 276965093307726057)
