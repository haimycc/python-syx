import matplotlib.pyplot as plt

#画条形图,第一个list是x轴，第二个list是y轴
plt.bar([1,3,5,7,9],[5,2,7,8,2], label="Example one")
#画条形图,并且制定颜色
plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Example two", color='g')
#默认图例
plt.legend()
#x轴的名字和y轴名字
plt.xlabel('bar number')
plt.ylabel('bar height')
#图名
plt.title('Epic Graph\nAnother Line! Whoa')

plt.show()
