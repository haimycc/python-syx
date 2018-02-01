# -*- coding:utf-8 -*-
import keyword

#打印出python的所有关键字
print(keyword.kwlist)
#['False',
# 'None',
#  'True',
# 'and',
#  'as',
#  'assert',
# 'break',
# 'class',
# 'continue',
# 'def',
#  'del',
# 'elif',
# 'else',
# 'except',
#  'finally',
#  'for',
# 'from',
#  'global',
#  'if',
# 'import',
# 'in',
# 'is',
#  'lambda',
#  'nonlocal',
#  'not',
# 'or',
# 'pass',
#  'raise',
# 'return',
# 'try',
# 'while',
# 'with',
# 'yield']

print(keyword.iskeyword("def"))
print(keyword.iskeyword("class"))
print(keyword.iskeyword("if"))