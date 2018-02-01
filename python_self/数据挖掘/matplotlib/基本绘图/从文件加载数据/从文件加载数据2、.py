import matplotlib.pyplot as plt
import numpy as np

#加载文件
x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)
#画直线
plt.plot(x,y, label='Loaded from file!')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
