# -*- coding:utf-8 -*-
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        #要是找到了
        if pattern in li:
            #返回生成器的例子，注意返回了该行，还有之前的命中的行
            yield li, previous_lines
        #加入到deque中
        previous_lines.append(li)


# Example use on a file
if __name__ == '__main__':
    with open(r'../../cookbook/somefile.txt') as f:
        #通过遍历不断返回生成器，返回该行还有命中的行
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)