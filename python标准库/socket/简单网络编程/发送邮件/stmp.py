#-*- coding: UTF-8 -*-

from smtplib import SMTP

SMTPSVR="smtp.qq.com"
origHdrs = ['From: xplovexjy@qq.com',
    'To: 80694172@qq.com',
    'Subject: test msg']
origBody = ['xxx', 'yyy', 'zzz']
origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs), '\r\n'.join(origBody)])
sendSvr = SMTP(SMTPSVR)
errs = sendSvr.sendmail('xplovexjy@qq.com',
    ('80694172@qq.com', ), origMsg)
sendSvr.quit()
