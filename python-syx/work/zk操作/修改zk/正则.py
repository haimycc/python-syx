import re


def ceshi():
    patten = '.*'
    #[\s\S]匹配换行
    match = re.findall(patten, "ddd" "<root</root>dfd")
    print(match)



ceshi()
