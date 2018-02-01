import os
import datetime,time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
from enum import Enum, unique
import math
import numpy as np
import pandas as pd
import pandas.io.sql as sql


new_conn = mysql.connector.connect(host='192.168.2.104',user='root',password="123456", database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def genSql():
    with open("updateSql", "a+") as f:
        for suffix in range(0,100):
            sql="insert into invest.t_investment_sums select * from invest.t_investment_sum_%02d ;\n" % (suffix)
            f.write(sql)

genSql()
