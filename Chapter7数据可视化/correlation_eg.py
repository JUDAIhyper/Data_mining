# 相关度计算，皮尔逊相关系数
from scipy.stats import pearsonr

# corr=pearsonr(X,Y)
import random
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.2)
y1 = 3 * x + 5
# y2在y1的基础上进行-5~5之间的随机实数波动
y2 = []
for i in y1:
    y2.append(i + random.uniform(-5, 5))

plt.plot(x, y1, color='r', label='y1')
plt.plot(x, y2, color='g', label='y2')
plt.legend()
plt.show()

# 计算相关性
corr = pearsonr(y1, y2)
print("相关系数r值为" + str(corr[0]) + ',显著性水平p值为' + str(corr[1]))
