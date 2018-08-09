def handler():
    sql = "alter table t_trustee_card_order_%03d modify column real_name varchar(64) NOT NULL DEFAULT '' COMMENT '真实姓名';"
    for i in range(100):
        res = str(sql) % (i)
        print(res)

handler()