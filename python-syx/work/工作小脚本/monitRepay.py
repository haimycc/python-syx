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
        sql1 = "SELECT CONCAT(asset_name,'|',phase) as asset_name,borrower_uid,asset_id,phase,guarantee_id FROM product.t_repayments WHERE state=1;"
        sql2 = "SELECT count(DISTINCT trans_id) as num FROM account.t_user_account_flow_%02d WHERE uid=%d AND remark='%s';"
        sql3 = "SELECT count(1) as num FROM invest.t_investment_payoffs WHERE asset_id=%d AND state =0 and phase=%d;"

        waitRepays = getAll(sql1)
        if waitRepays is None:
            return
        try:
            for repayInfo in waitRepays:
                asset_name = repayInfo['asset_name']
                borrower_uid = repayInfo['borrower_uid']
                asset_id = repayInfo['asset_id']
                phase = repayInfo['phase']
                guarantee_id = repayInfo['guarantee_id']
                uid = borrower_uid
                if (guarantee_id > 0):
                    uid = guarantee_id
                completeNum = getOne(sql2 % (uid % 100, uid, asset_name))
                allNum = getOne(sql3 % (asset_id, phase))
                if allNum:
                    print("标的名称 = " + str(asset_name))
                    print("已处理条数 = " + str(completeNum['num']))
                    print("总条数 = " + str(allNum['num']) + "\n")
                else:
                    print("标的名称 = " + str(asset_name) + "已还款完成" + "\n")
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
