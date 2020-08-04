import datetime
import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体格式为黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
data = pd.read_excel('data.xlsx')

# 将日期由字符串转为timestamp时间戳，方便刻度显示
d = []
for i in range(len(data)):
    d.append(datetime.datetime.strptime(data['date'][i], "%Y-%m-%d"))
data['date'] = d

# 数据可视化并设置坐标轴
plt.plot(data['date'], data['score'], linestyle='--', label='评分')
plt.xticks(rotation=45)  # 设置x轴刻度显示角度
plt.legend(loc='upper left')  # 设置评分的图例显示在左上角
plt.twinx()  # 设置双坐标轴
plt.plot(data['date'], data['price'], color='r', label='股价')
plt.xticks(rotation=45)
plt.legend(loc='upper right')
plt.show()
