import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

if __name__ == "__main__" :
    sum=0
    with open("./sum.txt","r") as f:
        for line in f.readlines():
            num=float(line)
            sum+=num
    print(sum)