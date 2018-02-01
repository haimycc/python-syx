
#打开文件,读取文件
with open("test.txt") as file:
    for line in file:
        #print只支持ascii编码
        print(line)

with open('test.txt', 'rt', newline='') as f:
    for line in f:
        print(line)


with open('test.txt', 'rt', encoding='ascii', errors='ignore') as f:
    for line in f:
        print(line)