#我们将pyplot导入为plt
#这是使用pylot的 python 程序的传统惯例。
import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]
x2 = [1,2,3]
y2 = [10,14,12]

#给直线定名字
plt.plot(x, y, label='First Line')
plt.plot(x2, y2, label='Second Line')

#给x轴和y轴命名
plt.xlabel('Plot Number')
plt.ylabel('Important var')
#给title
plt.title('Interesting Graph\nCheck it out')
#使用plt.legend()生成默认图例
plt.legend()
plt.show()
