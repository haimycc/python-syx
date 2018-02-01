#!/bin/bash
# 生产环境
mysql_exec="mysql -h192.168.50.150 -u search -psearch@zyxr.com"
# 测试环境
#mysql_exec="mysql -h192.168.30.130 -u mysqluser -pmysqluser@zyxr.com"

exec_sql=""
outfile="投资记录总表异常数据.txt"
execsql_file=""

echo "##########################invest####################################"
db=invest
echo "获取invest.t_investment_xx与invest.t_investments不一致的数据..."
sleep 1
m=0
n=0

echo "查看更改前不一致的投资记录数据,并输出到$outfile"
rm $outfile

for i in {0..99}
do	
	m=$(($i/10))
	n=$(($i%10))
    exec_sql="select s.investment_id,
if(s.asset_id                         <>        t.asset_id,  CONCAT(s.asset_id,'<>',t.asset_id),'ok')                      					as asset_id,
if(s.asset_type                       <>        t.asset_type,CONCAT(s.asset_type,'<>',t.asset_type),'ok')                  					as asset_type,
if(s.asset_pool			              <>        t.asset_pool,CONCAT(s.asset_pool,'<>',t.asset_pool),'ok')                  					as asset_pool,							  
if(s.asset_state		              <>        t.asset_state,CONCAT(s.asset_state,'<>',t.asset_state),'ok')               					as asset_state,							
if(s.asset_property		              <>        t.asset_property,CONCAT(s.asset_property,'<>',t.asset_property),'ok')      					as asset_property,						
if(s.asset_name			              <>        t.asset_name,CONCAT(s.asset_name,'<>',t.asset_name),'ok')                  					as asset_name,							
if(s.annual_rate					  <>        t.annual_rate,CONCAT(s.annual_rate,'<>',t.annual_rate),'ok')               					as annual_rate,										
if(s.add_rate						  <>        t.add_rate,CONCAT(s.add_rate,'<>',t.add_rate),'ok')                        					as add_rate,												
if(s.phase_total					  <>        t.phase_total,CONCAT(s.phase_total,'<>',t.phase_total),'ok')               					as phase_total,										
if(s.phase_mode			              <>        t.phase_mode,CONCAT(s.phase_mode,'<>',t.phase_mode),'ok')                  					as phase_mode,			    							
if(s.repay_mode			              <>        t.repay_mode,CONCAT(s.repay_mode,'<>',t.repay_mode),'ok')                  					as repay_mode,			    							
if(s.contract_no	         		  <>        t.contract_no,CONCAT(s.contract_no,'<>',t.contract_no),'ok')               					as contract_no,	        							
if(s.debt_id		          		  <>        t.debt_id,CONCAT(s.debt_id,'<>',t.debt_id),'ok')                           					as debt_id,		        								
if(s.debt_name		        		  <>        t.debt_name,CONCAT(s.debt_name,'<>',t.debt_name),'ok')                     					as debt_name,		        								
if(s.investor_uid		        	  <>        t.investor_uid,CONCAT(s.investor_uid,'<>',t.investor_uid),'ok')            					as investor_uid,		    							
if(s.borrower_uid		        	  <>        t.borrower_uid,CONCAT(s.borrower_uid,'<>',t.borrower_uid),'ok')            					as borrower_uid,		    							
if(s.amount				              <>        t.amount,CONCAT(s.amount,'<>',t.amount),'ok')                              					as amount,				    								
if(s.valid_amount		              <>        t.valid_amount,CONCAT(s.valid_amount,'<>',t.valid_amount),'ok')            					as valid_amount,		    							
if(s.percentage				          <>        t.percentage,CONCAT(s.percentage,'<>',t.percentage),'ok')                  					as percentage,											
if(s.init_percentage		          <>        t.init_percentage,CONCAT(s.init_percentage,'<>',t.init_percentage),'ok')   					as init_percentage,								
if(s.conpon_id				          <>        t.conpon_id,CONCAT(s.conpon_id,'<>',t.conpon_id),'ok')                     					as conpon_id,												
if(s.conpon_type			          <>        t.conpon_type,CONCAT(s.conpon_type,'<>',t.conpon_type),'ok')               					as conpon_type,										
if(s.state					          <>        t.state,CONCAT(s.state,'<>',t.state),'ok')                                 					as state,														
if(s.debt_property			          <>        t.debt_property,CONCAT(s.debt_property,'<>',t.debt_property),'ok')         					as debt_property,										
if(s.from_device			          <>        t.from_device,CONCAT(s.from_device,'<>',t.from_device),'ok')               					as from_device,										
if(s.rest_phase				          <>        t.rest_phase,CONCAT(s.rest_phase,'<>',t.rest_phase),'ok')                  					as rest_phase,											
if(s.expect_principal		          <>        t.expect_principal,CONCAT(s.expect_principal,'<>',t.expect_principal),'ok')					as expect_principal,								
if(s.expect_interest		          <>        t.expect_interest,CONCAT(s.expect_interest,'<>',t.expect_interest),'ok')                	as expect_interest,								
if(s.expect_add_interest	          <>        t.expect_add_interest,CONCAT(s.expect_add_interest,'<>',t.expect_add_interest),'ok')    	as expect_add_interest,						
if(s.expect_pay_platform	          <>        t.expect_pay_platform,CONCAT(s.expect_pay_platform,'<>',t.expect_pay_platform),'ok')    	as expect_pay_platform,						
if(s.received_principal		          <>        t.received_principal,CONCAT(s.received_principal,'<>',t.received_principal),'ok')       	as received_principal,							
if(s.received_interest	        	  <>        t.received_interest,CONCAT(s.received_interest,'<>',t.received_interest),'ok')          	as received_interest,	    						
if(s.received_add_interest      	  <>        t.received_add_interest,CONCAT(s.received_add_interest,'<>',t.received_add_interest),'ok')  as received_add_interest,  				
if(s.actual_pay_platform        	  <>        t.actual_pay_platform,CONCAT(s.actual_pay_platform,'<>',t.actual_pay_platform),'ok')        as actual_pay_platform,    					
if(s.received_money		        	  <>        t.received_money,CONCAT(s.received_money,'<>',t.received_money),'ok')                       as received_money,		    						
if(s.next_payoff_day	        	  <>        t.next_payoff_day,CONCAT(s.next_payoff_day,'<>',t.next_payoff_day),'ok')                    as next_payoff_day,	    						
if(s.lock_day		            	  <>        t.lock_day,CONCAT(s.lock_day,'<>',t.lock_day),'ok')                                         as lock_day,		        								
if(s.finish_time	            	  <>        t.finish_time,CONCAT(s.finish_time,'<>',t.finish_time),'ok')                                as finish_time,	        							
if(s.full_time		            	  <>        t.full_time,CONCAT(s.full_time,'<>',t.full_time),'ok')                                      as full_time		        			

from t_investment_${m}${n} t, t_investments s where t.investment_id=s.investment_id
and (		
s.asset_state			<>          t.asset_state			
or s.state					<>          t.state							
or s.expect_principal		<>          t.expect_principal		
or s.expect_interest		<>          t.expect_interest		
or s.expect_add_interest	<>          t.expect_add_interest	
or s.expect_pay_platform	<>          t.expect_pay_platform	
or s.received_principal	    <>          t.received_principal	
or s.received_interest		<>          t.received_interest		
or s.received_add_interest	<>          t.received_add_interest
or s.actual_pay_platform	<>          t.actual_pay_platform	
or s.received_money		    <>          t.received_money);
"
$mysql_exec $db -N -e "$exec_sql" >> $outfile
done

cat $outfile | while read line
do
echo $line
done


echo "==================END======================"