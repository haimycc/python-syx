# -*- coding:utf-8 -*-
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
#俘获是否有问题：
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
#没有错误就执行else语句
else:
    print('no error!')
#最后肯定会执行finally语句
finally:
    print('finally...')
print('END')
