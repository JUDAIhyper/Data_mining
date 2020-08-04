import pymysql
import time
db = pymysql.connect(host='localhost', port=3306, user='root',
                     password='root', database='pachong', charset='utf8')
company = '阿里巴巴'
today = time.strftime("%Y-%m-%d")

# 编写sql语句提取当天目标公司的全部新闻数据
cur = db.cursor()
sql = 'SELECT * FROM article WHERE company=%s AND date=%s'
cur.execute(sql, (company, today))
data = cur.fetchall()
# 计算当天评分
score = 100
for i in range(len(data)):
    score += data[i][5]

db.commit()
cur.close()
db.close()

print(company + '的今日舆情评分为：' + str(score))
