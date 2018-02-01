import mysql.connector

new_conn = mysql.connector.connect(host='192.168.31.222', user='root', password='123456', database='invest')
new_cursor = new_conn.cursor(dictionary=True)
file = open("D:\回款总表.txt", "w")
f = open('D:\回款分表.txt', "w")


def handler():
    sql1 = "SELECT * from invest.t_investment_payoffs where asset_id=20170804000239841 AND phase=2;"
    updat_sql = "update invest.t_investment_payoff_%02d set actual_date='2017-10-17 17:00:00',update_time=now() where asset_id=20170804000239841 AND phase=2 AND investment_id=%s and payoff_id=%s;"
    updatAll = "update invest.t_investment_payoffs set actual_date='2017-10-17 17:00:00',update_time=now() where asset_id=20170804000239841 AND phase=2 AND investment_id=%s and payoff_id=%s;"


    new_cursor.execute(sql1)
    resAll = new_cursor.fetchall()

    for ra in resAll:
        id_ = updat_sql % (int(str(ra["investment_id"])[-2:]), str(ra["investment_id"]), str(ra["payoff_id"]))
        id_2 = updatAll % (str(ra["investment_id"]), str(ra["payoff_id"]))
        print(id_)
        f.writelines(id_ + "\n")
        file.writelines(id_2 + "\n")

    f.close()
    file.close()

handler()
