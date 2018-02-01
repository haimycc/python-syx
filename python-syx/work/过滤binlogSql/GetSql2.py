file = open("D:\sql4.txt", "r")
f = open('D:\sql5.txt', "w")
saveList = ("insert", "INSERT", "update", "UPDATE")
numList = ("20170710000000025", "20170710000000025", "20170509000000125", "20170504000014125", "201705030002396025", "20170503000070025", "20161104000033625", '201611040000002025', "20170504000041964", "20170509000001425")

while 1:
    # 用缓存效率提高3倍
    lines = file.readline(100000)
    if lines.startswith(saveList):
        for num in numList:
            if num in lines:
                f.write(lines + "\n")
                break
    elif not lines:
        break
    else:
        continue
file.close()
f.close()
