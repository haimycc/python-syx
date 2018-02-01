#我们将pyplot导入为plt
#这是使用pylot的 python 程序的传统惯例。
import matplotlib.pyplot as plt

#我们调用plot的.plot方法绘制一些坐标。
#这个.plot需要许多参数，但前两个是'x'和'y'坐标，我们放入列表。
plt.plot([1,2,3],[5,7,4])

plt.show()