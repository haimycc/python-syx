# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import json

obj="""
    {
        "assetId":20161230000069265,
        "categoryType":3,
        "businessType":201611040000006,
        "businessName":"企业贷",
        "assetName":"企融宝-161230TA7036",
        "assetType":"0",
        "assetPool":"1",
        "assetProperty":0,
        "publishPlatForm":0,
        "contractNo":"ZYXR-03-002645",
        "state":"5",
        "credit":"AAA",
        "assetDesc":"借款企业从事建设工程行业，企业经营状况良好，据银行征信系统显示，借款企业信用记录良好。\n本次借款50万元，用于补充流动资金，还款来源为企业经营收入。",
        "borrowerUid":201609010088999165,
        "borrowerName":"白洪飞",
        "borrowerBorrowway":"3",
        "borrowerTime":"1",
        "borrowerLocation":"",
        "totalAmount":50000000,
        "raisedAmount":38133200,
        "moneyRange":"2",
        "annualRate":800,
        "addRate":0,
        "phaseTotal":1,
        "phaseMode":"2",
        "repayMode":"2",
        "repayPhase":0,
        "depositPhase":0,
        "minTender":10000,
        "increaseTender":100,
        "maxTender":50000000,
        "investorCount":12,
        "operationDoc":"",
        "lockDay":30,
        "publishTime":"2017-02-05 17:32:32",
        "investTime":"2017-02-05 17:32:38",
        "bidTime":"2017-02-25 17:32:38",
        "updateTime":"2017-02-05 21:22:15",
        "createTime":"2017-02-05 17:32:53",
        "qixiTime":"满标放款后第2天开始计算收益"
    }
"""

result=json.loads(obj)
print(result)
