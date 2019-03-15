file = open("D:\索引.txt", "w")


#生成加索引sql
def genSqlIndex(tableName, indexName, columnList, indexType='index'):
    sql = "ALTER TABLE {table_name} ADD {index_type} {index_name}({column_list});"
    sql_format = sql.format(table_name=tableName, index_type=indexType, index_name=indexName, column_list=columnList)
    print(sql_format)
    file.write(sql_format + "\n")

#去掉索引
def genDropSqlIndex(tableName, indexName, indexType='index'):
    sql = "ALTER TABLE {table_name} drop {index_type} {index_name};"
    sql_format = sql.format(table_name=tableName, index_type=indexType, index_name=indexName)
    print(sql_format)


if __name__ == '__main__':
    for i in range(0, 100):
        genSqlIndex('trustee.t_trustee_request_flow_%03d' % (i), 'idx_order_id', 'order_id')
    file.close()
    # genDropSqlIndex('cms.t_fdd_assets', 'index_oprate_type')
