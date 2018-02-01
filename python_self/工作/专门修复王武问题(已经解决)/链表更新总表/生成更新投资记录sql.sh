#!/bin/bash
#                  生产环境
mysql_exec="mysql -h192.168.50.150 -u search -psearch@zyxr.com"
#                  测试环境
#mysql_exec="mysql  -h192.168.30.130 -u mysqluser -pmysqluser@zyxr.com"

exec_sql=""
outfile="投资记录总表异常数据.txt"

##############################################
#investment_id	asset_id	asset_type	asset_pool	asset_state	asset_property	asset_name	annual_rate	add_rate	phase_total	phase_mode	repay_mode	contract_no	debt_id	debt_name	investor_uid	borrower_uid	amount	valid_amount	percentage	init_percentage	conpon_id	conpon_type	state	debt_property	from_device	rest_phase	expect_principal	expect_interest	expect_add_interest	expect_pay_platform	received_principal	received_interest	received_add_interest	actual_pay_platform	received_money	next_payoff_day	lock_day	finish_time	full_time
#20161121000000000	ok	ok	ok	ok	ok	ok	ok	ok	ok	ok	ok	ok	ok	ok	ok	ok	ok	ok	ok	ok	ok	ok	ok	ok	ok	3<>1	ok	ok	ok	ok	0<>664172	0<>11893	ok	0<>625	0<>11893	2016-12-22 00:00:00<>2017-02-22 00:00:00	ok	ok	ok
############################

execsql_file=""

echo "##########################invest####################################"
db=invest

##更新投资记录总表sql
execsql_file="update_invest.t_investments.sql"
rm $execsql_file
exec_sql="use $db;"

echo $exec_sql >> $execsql_file
## 生成sql,对应投资记录investment_id
for investmentId in ` cat $outfile| awk '{print $1}'` 
{ 
	# 截取后2位
	suffix=${investmentId:0-2:2}
	 exec_sql="update invest.t_investments inner join invest.t_investment_${suffix} t on invest.t_investments.investment_id=t.investment_id 
set 
invest.t_investments.asset_state           = t.asset_state		  ,
invest.t_investments.state                 = t.state			      ,   	
invest.t_investments.expect_principal      = t.expect_principal	  ,
invest.t_investments.expect_interest       = t.expect_interest	  ,
invest.t_investments.expect_add_interest   = t.expect_add_interest  ,
invest.t_investments.expect_pay_platform   = t.expect_pay_platform  ,      
invest.t_investments.received_principal    = t.received_principal	  ,   
invest.t_investments.received_interest     = t.received_interest	  ,   
invest.t_investments.received_add_interest = t.received_add_interest,   
invest.t_investments.actual_pay_platform   = t.actual_pay_platform  ,       
invest.t_investments.received_money        = t.received_money           

where invest.t_investments.investment_id=$investmentId;"
	 echo $exec_sql >> $execsql_file
}  

echo "END###########################################################################"
sleep 1
echo "done!"