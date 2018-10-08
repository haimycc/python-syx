from sqlMoudle.sqlTemplate import *

# backup = open('D:\\backupsql.txt', "w")
# f = open('D:\\fixRepayData.txt', "w")

def fun():
    # 获取理财顾问advisorId
    advisorMobile = 18288772663
    advisorSql = "SELECT id FROM market.`t_financial_advisor` t WHERE t.`mobile`='%s' AND t.`status`=0;" % (
        advisorMobile)
    advisorRows = getOne(advisorSql)
    newAdvisorId = advisorRows['id']

    # 获取直接客户现在的理财顾问id
    mobile = 15288315669
    typeSql = "SELECT  t.`advisor`,t.`referee_id`,t.`user_type` FROM user.`t_user` t WHERE t.`mobile`='%s';" % (mobile)
    feeRows = getOne(typeSql)
    if (feeRows['user_type'] == 0):
        newSql = "SELECT advisor_id FROM market.`t_financial_user` t WHERE t.`mobile`='%s';" % (mobile)
        row = getOne(newSql)
        if (str(row['advisor_id']) == str(newAdvisorId)):
            print(str(mobile) + '用户不用修改market库')


if __name__ == '__main__':
    fun()
