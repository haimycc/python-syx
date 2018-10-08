import mysql.connector

new_conn = mysql.connector.connect(host='172.27.48.181', user='search', password='search@zyfax.com', database='product')
new_cursor = new_conn.cursor(dictionary=True)


def getOne(sql, *args):
    new_cursor.execute(sql)
    return new_cursor.fetchone()


def getAll(sql, *args):
    new_cursor.execute(sql)
    return new_cursor.fetchall()



