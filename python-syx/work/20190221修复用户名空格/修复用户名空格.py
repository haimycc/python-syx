from sqlMoudle.sqlTemplate import *

file = open("D:\修复用户名空格.txt", "w")


def genUpdateSql(tableName, userId):
    sql = "update {table_name} set real_name=REPLACE(real_name, ' ', ''),user_unique_code = REPLACE(user_unique_code, ' ', '') where userid={user_id};"
    sql_format = sql.format(table_name=tableName, user_id=userId)
    print(sql_format)
    file.write(sql_format + "\n")


if __name__ == '__main__':
    userData = getAll("SELECT * FROM `user`.t_user_detail_ext WHERE real_name LIKE '% %';")
    for i in userData:
        # realName = i['real_name']
        # userUniqueCode = i['user_unique_code']
        userId = i['userid']
        genUpdateSql('`user`.t_user_detail_ext', userId)
    file.close()
