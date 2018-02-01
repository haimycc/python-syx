import mysql.connector

new_conn = mysql.connector.connect(host='192.168.31.222', user='root', password='123456', database='product')
new_cursor = new_conn.cursor(dictionary=True)
file = open("D:\回款数据备份.txt", "w")
f = open("D:\回款数据备份简单版.txt", "w")

# " a.asset_id,a.expect_date,a.phase, b.expect_date,a.create_time"
a = dict()
def handler():
    sql3 = "SELECT "\
    " b.* "\
    " FROM"\
    " product.t_repayments a,"\
    " invest.t_investment_payoffs b"\
    " WHERE"\
    " a.asset_id = b.asset_id"\
    " AND a.phase = b.phase"\
    " AND DATE(a.expect_date) != date(b.expect_date)"\
    " AND a.state in (0,4)"\
    " AND b.state = 0"\
    " AND a.create_time > '2017-03-01 00:00:00'"\
    " AND b.actual_date = '0000-00-00 00:00:00'"\
    " AND a.actual_date = '0000-00-00 00:00:00'"\
    " ORDER BY a.create_time"

    new_cursor.execute(sql3)
    results = new_cursor.fetchall()
    for res in results:
        file.write(str(res) + "\n")
        a['asset_id'] = res['asset_id']
        a['asset_name'] = res['asset_name']
        a['expect_date'] = str(res['expect_date'])
        a['phase'] = res['phase']
        a['investment_id'] = res['investment_id']
        a['investor_uid'] = res['investor_uid']
        a['borrower_uid'] = res['borrower_uid']
        f.write(str(a) + "\n")

    f.close()
    file.close()
handler()
