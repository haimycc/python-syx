import os
import mysql.connector

new_conn = mysql.connector.connect(host='192.168.50.151', user='search', password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

if __name__ == "__main__" :
    lists=[(20170104000072703,20170104000013504),
          (20170104000073903,20170104000021011),
          (20170104000073903,20170104000015838),
          (20170104000060003,20170104000000139),
          (20170104000072703,20170104000022240),
          (20170104000072703,20170104000014853),
          (20170104000073903,20170104000022661),
          (20170104000072703,20170104000049164),
          (20170104000033807,20170104000014469),
          (20170104000060003,20170104000012173),
          (20170104000073903,20170104000021376),
          (20170104000072703,20170104000015578)
          ]
    for tuple in lists:
        assetId=tuple[0]
        investId=tuple[1]
        sql="update product.t_investment_%s set state = 3 where asset_id = %d and investment_id = %d and state = 0 ; " % (str(assetId)[-2:],assetId,investId)
        print(sql)
