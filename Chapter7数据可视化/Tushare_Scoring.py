# 合并分数与收益表格
import tushare as ts
# data = ts.get_hist_data('000002', start='2020-01-01', end='2020-07-29')
# data.to_excel('share.xlsx')
import pandas as pd
score = pd.read_excel('../Chapter6数据分析/score.xlsx')  # 读取评分数据
share = pd.read_excel('share.xlsx')  # 读取行情数据
share = share[['date', 'close']]  # 只需要行情数据里的日期和收益价
data = pd.merge(score, share, on='date', how='inner')  # 数据合并
data = data.rename(columns={'close': 'price'})  # close列重命名为price
# print(data)
data.to_excel('data.xlsx', index=False)
