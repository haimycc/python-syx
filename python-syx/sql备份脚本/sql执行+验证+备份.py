import pymysql

# sql连接模板
# new_conn = pymysql.connect(“localhost”,“root”,你的密码",“TESTDB” )
new_conn = pymysql.connect('192.168.9.252', 'admin', 'admin', 'test')
new_cursor = new_conn.cursor(pymysql.cursors.DictCursor)


def getOne(sql, *args):
    new_cursor.execute(sql)
    return new_cursor.fetchone()


def getAll(sql, *args):
    new_cursor.execute(sql)
    return new_cursor.fetchall()


def DBclose():
    new_conn.close()


# sql连接模板

fileGenIndex = open("D:\加索引.sql", "w")
fileDropIndex = open("D:\删索引.sql", "w")
fileUpdateSql = open("D:\\update.sql", "w")
fileDeleteSql = open("D:\\delete.sql", "w")
fileBackUpSql = open("D:\\backUp.sql", "w")
fileValidateSql = open("D:\\validate.sql", "w")


# 生成加索引sql
def genIndexSql(tableName, indexName, columnList, indexType='index'):
    sql = "ALTER TABLE {table_name} ADD {index_type} {index_name}({column_list});"
    sql_format = sql.format(table_name=tableName, index_type=indexType, index_name=indexName, column_list=columnList)
    print(sql_format)
    fileGenIndex.write(sql_format + "\n")


# 去掉索引
def genDropSqlIndex(tableName, indexName, indexType='index'):
    sql = "ALTER TABLE {table_name} drop {index_type} {index_name};"
    sql_format = sql.format(table_name=tableName, index_type=indexType, index_name=indexName)
    print(sql_format)
    fileDropIndex.write(sql_format + "\n")


# update语句
def genUpdateSql(tableName, values, conditions):
    sql = "update {table_name} set {values},update=now() where {conditions};"
    sql_format = sql.format(table_name=tableName)
    print(sql_format)
    fileUpdateSql.write(sql_format + "\n")


def genDeleteSql(tableName, conditions):
    sql = "DELETE FROM {table_name} where {conditions};"
    sql_format = sql.format(table_name=tableName)
    print(sql_format)
    # fileDeleteSql.write(sql_format + "\n")


if __name__ == '__main__':
    # for i in range(0, 100):
    #     genIndexSql('trustee.t_trustee_request_flow_%03d' % (i), 'idx_order_id', 'order_id')
    # fileGenIndex.close()
    x = getOne("select * from test.admin")
    print(x['id'])
    # genDropSqlIndex('cms.t_fdd_assets', 'index_oprate_type')


#
# SELECT '修改字段times值' AS title,CASE times WHEN 0 THEN '成功' ELSE '失败' END AS result
# FROM test.t_user_login_error_ext_t WHERE id=617
# UNION ALL
# SELECT '建表t_user_login_error_ext_t'  AS title,CASE COUNT(1) WHEN 1 THEN '成功' ELSE '失败' END AS result
# FROM information_schema.`TABLES` a
# WHERE a.table_schema='test' AND a.table_name='t_user_login_error_ext_t'
# UNION ALL
# SELECT 'times字段类型长度'  AS title,CASE a.column_type WHEN 'int(11)' THEN '成功' ELSE '失败' END AS result
# FROM information_schema.columns a
# WHERE a.table_schema='test' AND a.table_name='t_user_login_error_ext_t'
# AND a.column_name='times';