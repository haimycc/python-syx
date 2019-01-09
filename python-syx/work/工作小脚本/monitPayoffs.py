import os
import mysql.connector

new_conn = mysql.connector.connect(host='172.27.48.181', user='search', password='search@zyfax.com', database='product')
new_cursor = new_conn.cursor(dictionary=True)


def getOne(sql, *args):
    new_cursor.execute(sql)
    return new_cursor.fetchone()


def getAll(sql, *args):
    new_cursor.execute(sql)
    return new_cursor.fetchall()

def DBclose():
    new_conn.close()


class MonitRepay(object):
    def get_asset_info(self):
        # 1.查询操作
        # 编写sql 查询语句  user 对应我的表名
        sql1 = "SELECT asset_id,phase,asset_name,borrower_uid FROM product.t_repayments WHERE state=0  AND DATE(expect_date) = DATE(NOW());"
        sql3 = "SELECT count(1) as num FROM invest.t_investment_payoffs WHERE asset_id=%d AND state =0 and phase=%d HAVING COUNT(1) > 1000;"
        getMobile = "SELECT mobile FROM `user`.t_user WHERE id=%d;"

        waitRepays = getAll(sql1)
        if waitRepays is None:
            return
        try:
            for repayInfo in waitRepays:
                asset_id = repayInfo['asset_id']
                asset_name = repayInfo['asset_name']
                phase = repayInfo['phase']
                borrower_uid = repayInfo['borrower_uid']
                allNum = getOne(sql3 % (asset_id, phase))
                if allNum is not None:
                    user = getOne(getMobile % (borrower_uid))
                    print("借款人手机号 = " + str(user['mobile']))
                    print("标的名称 = " + str(asset_name))
                    print("总条数 = " + str(allNum['num']) + "\n")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    print("稍等,正在查询......\n")
    repay = MonitRepay()
    try:
        repay.get_asset_info()
        DBclose()
        print("查询完毕")
    except Exception as e:
        print(e)
    # os.system('pause')
