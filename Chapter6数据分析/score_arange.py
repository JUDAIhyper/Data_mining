# 汇总舆情数据评分
import pandas as pd
import datetime
import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root',
                     password='root', database='pachong', charset='utf8')
# 设定参数
company = '万科集团'

date_list = list(pd.date_range('2020-01-01', '2020-07-29'))
for i in range(len(date_list)):
    date_list[i] = datetime.datetime.strftime(date_list[i], "%Y-%m-%d")
    # date_list[i]=date_list[i].strftime("%Y-%m-%d")

# 编写SQL语句
cur = db.cursor()
sql = 'SELECT * FROM article WHERE company=%s AND date=%s'
# 遍历date_list中的日期，获取每天的评分并存储到字典score_list中
score_list = {}  # 建立字典
for d in date_list:
    cur.execute(sql, (company, d))
    data = cur.fetchall()  # 提取所有数据并赋值给变量data
    # print(data)
    score = 100
    for i in range(len(data)):
        score += data[i][5]
    score_list[d] = score
db.commit()
cur.close()
db.close()
# # 导出舆情数据评分表格
# data = pd.DataFrame.from_dict(score_list, orient='index', columns=['score'])
# # 将行索引变成数字符号：
# # 1.通过重置索引的方式将行索引转换为列
# data.index.name = 'date'  # 将行索引列命名为date
# data.reset_index()  # 重置行索引

# 2.将字典转换成列表，然后创建dataframe
data = pd.DataFrame(list(score_list.items()), columns=['date', 'score'])
print(data)
data.to_excel('score.xlsx')

# 3.用data.index.name命名索引列后在写入excel时设置保留索引信息
# data = pd.DataFrame.from_dict(score_list, orient='index', columns=['score'])
# data.index.name = 'date'
# data.to_excel('score.xlsx')
