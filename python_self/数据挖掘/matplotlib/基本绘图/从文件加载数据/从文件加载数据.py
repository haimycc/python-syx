import matplotlib.pyplot as plt
import csv

x = []
y = []

#解析csv模块
with open('example.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    #把每一行的第一个元素设置为x,第二个元素设置为y
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

#画直线
plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
