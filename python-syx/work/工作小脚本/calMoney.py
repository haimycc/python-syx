import os
from enum import Enum

import math


class RateTable(Enum):
    rate1 = 36000
    rate2 = 144000
    rate3 = 300000
    rate4 = 420000
    rate5 = 660000
    rate6 = 960000
    rate7 = 100000000
    rate1_hold = 3
    rate2_hold = 10
    rate3_hold = 20
    rate4_hold = 25
    rate5_hold = 30
    rate6_hold = 35
    rate7_hold = 45
    rate1_speed_cal = 0
    rate2_speed_cal = 2520
    rate3_speed_cal = 16920
    rate4_speed_cal = 31920
    rate5_speed_cal = 52920
    rate6_speed_cal = 85920
    rate7_speed_cal = 181920


MarkPoint = 5000
RateTableList = (
    RateTable.rate1, RateTable.rate2, RateTable.rate3,
    RateTable.rate4, RateTable.rate5, RateTable.rate6, RateTable.rate7)
TOTAL_MONEY = 0


def calWage(wage, insurance, surtax):
    global TOTAL_MONEY
    MonthRate = [0] * 13
    for i in range(1, 13):
        surtax_per = (wage * 100 - insurance * 100 - MarkPoint * 100 - surtax * 100) / 100
        if (surtax_per < 0):
            print("工资不用扣税")
            TOTAL_MONEY = surtax_per * 12
            return
        surtax_i = surtax_per * i
        for rateTable in RateTableList:
            if (surtax_i <= rateTable.value):
                i_tax = (surtax_i * RateTable[rateTable.name + "_hold"].value * 100 - MonthRate[i - 1] * 10000 -
                         RateTable[
                             rateTable.name + "_speed_cal"].value * 10000) / 10000
                i_tax = getFloatValue(i_tax)
                MonthRate[i] = i_tax + MonthRate[i - 1]
                print(str(i) + "月扣税" + str(getFloatValue(i_tax)) + ",实际到手" + str(
                    getFloatValue((wage - i_tax - insurance))) + "税级距" + str(RateTable[rateTable.name + "_hold"].value))
                TOTAL_MONEY = TOTAL_MONEY + getFloatValue((wage - i_tax - insurance)) * 100
                break
    return str(getFloatValue(MonthRate[12]))


def getFloatValue(num):
    return math.floor(num * 100) / 100


if __name__ == '__main__':
    print('单位都是元')
    wage = eval(input('输入税前工资：'))
    insurance = eval(input('五险一金扣除：'))
    surtax = eval(input('专项附加扣除值：'))
    wage = calWage(getFloatValue(wage), getFloatValue(insurance), getFloatValue(surtax))
    # wage = calWage(9000.52, 100, 100)
    print("累计扣税" + wage)
    print("累计到手工资" + str(getFloatValue(TOTAL_MONEY) / 100))
    # wage = calWage(22500, 3706.78, 1500)
    # print("累计扣税" + wage)
    os.system('pause')
