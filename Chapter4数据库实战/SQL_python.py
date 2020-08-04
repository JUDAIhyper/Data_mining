import pymysql
# 预定义变量
# company = '阿里巴巴'
# title = '测试标题'
# href = '测试链接'
# date = '测试日期'
# source = '测试来源'

db = pymysql.connect(host='localhost', port=3306, user='root',
                     password='root', database='pachong', charset='utf8')
company = '阿里巴巴'
# 引入会话指针,调用sql语句
cur = db.cursor()
#sql = 'INSERT INTO test(company,title,href,date,source) VALUES(%s,%s,%s,%s,%s)'
# 查询语句
sql = 'SELECT * FROM test WHERE company=%s'
# cur.execute(sql, (company, title, href, date, source))  # 执行sql语句
cur.execute(sql, company)
data = cur.fetchall()  # 提取所有数据，并赋值给变量data
print(data)
db.commit()  # 更新数据表
cur.close()  # 关闭会话指针
db.close()  # 关闭数据库连接
