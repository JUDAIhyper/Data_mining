import tushare as ts
import pandas as pd
pd.set_option('display.max_columns', None)


# 调取特定时间段数据
def data_part():
    df = ts.get_hist_data('000002', start='2020-01-01', end='2020-07-29')


# 调取分钟级别的数据
def data_mint():
    df = ts.get_hist_data('000002', ktype='5')
# 调取实时数据


def data_present():
    df = ts.get_realtime_quotes('000002', '000980', '000981')
    # 选取需要的列
    df = df[['code', 'name', 'price', 'bid', 'ask', 'volume', 'amount', 'time']]

# 调取分笔数据


def data_trick():
    df = ts.get_tick_data('000002', date='2019-12-12', src='tt')
    print(df)

data_trick()
