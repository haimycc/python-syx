import os
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)


MySQL [(none)]> select distinct investor_uid,count(1) from invest.t_investment_payoffs where investment_id not in (select distinct investment_id from invest.t_investments) group by investor_uid ;
+--------------------+----------+
| investor_uid       | count(1) |
+--------------------+----------+
| 201609010000000098 |       72 |
| 201609010000001110 |        3 |
| 201609010000003071 |       36 |
+--------------------+----------+


