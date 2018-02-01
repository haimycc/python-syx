import os
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.51.145',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)



def GetInfo():
    sql="select s1.asset_id,s1.IAMT,d1.SAMT from " \
        "(select s.asset_id,sum(s.expect_principal)/100 AS IAMT from " \
        "invest.t_investments s " \
        "where " \
        "s.asset_type=0 and s.asset_pool=1  and s.asset_state=8  and s.state in (2,4) " \
        "group by s.asset_id) s1 " \
        "left join " \
        "(select r.asset_id,sum(r.expect_principal)/100 as SAMT from " \
        "product.t_repayments r " \
        "left join product.t_assets d  on r.asset_id=d.asset_id where d.asset_type=0 and d.asset_pool=1 group by asset_id) " \
        "d1" \
        " on s1.asset_id=d1.asset_id " \
        "where " \
        "d1.SAMT-s1.IAMT>10 order by d1.SAMT-s1.IAMT desc;"


