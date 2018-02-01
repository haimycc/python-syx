# -*- coding:utf-8 -*-

import os
import datetime,time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import pandas as pd
import numpy as np
import json
import pandas.io.sql as sql


new_conn = mysql.connector.connect(host='192.168.50.151', user='search', password='search@zyxr.com', database='invest')
#把sql数据存放到frame中
frame=sql.read_sql("select * from product.t_repayments limit 0,10",new_conn)
print(frame.columns)
print()
print(frame.index)
print()
print(frame.values)
print()




