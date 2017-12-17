#coding=utf-8
#导入pymysql的包
import pymysql
import datetime

# 连接数据库
conn=pymysql.connect(
    host='192.168.223.10',
    port=3306,
    user='root',
    passwd='TomLee4!',
    db='big_data',
    charset='utf8'
)

# 获取游标
cursor = conn.cursor()

# 插入数据
sql = "INSERT INTO phone_detail  VALUES (NULL , '18124201612', '广东广州', '2017-12-17 00:00:00')"
cursor.execute(sql)
conn.commit()
print('成功插入', cursor.rowcount, '条数据')

# # 修改数据
# sql = "UPDATE trade SET saving = %.2f WHERE account = '%s' "
# data = (8888, '13512345678')
# cursor.execute(sql % data)
# connect.commit()
# print('成功修改', cursor.rowcount, '条数据')
#
# # 查询数据
# sql = "SELECT name,saving FROM trade WHERE account = '%s' "
# data = ('13512345678',)
# cursor.execute(sql % data)
# for row in cursor.fetchall():
#     print("Name:%s\tSaving:%.2f" % row)
# print('共查找出', cursor.rowcount, '条数据')
#
# # 删除数据
# sql = "DELETE FROM trade WHERE account = '%s' LIMIT %d"
# data = ('13512345678', 1)
# cursor.execute(sql % data)
# connect.commit()
# print('成功删除', cursor.rowcount, '条数据')
#
# # 事务处理
# sql_1 = "UPDATE trade SET saving = saving + 1000 WHERE account = '18012345678' "
# sql_2 = "UPDATE trade SET expend = expend + 1000 WHERE account = '18012345678' "
# sql_3 = "UPDATE trade SET income = income + 2000 WHERE account = '18012345678' "
#
# try:
#     cursor.execute(sql_1)  # 储蓄增加1000
#     cursor.execute(sql_2)  # 支出增加1000
#     cursor.execute(sql_3)  # 收入增加2000
# except Exception as e:
#     connect.rollback()  # 事务回滚
#     print('事务处理失败', e)
# else:
#     connect.commit()  # 事务提交
#     print('事务处理成功', cursor.rowcount)

# 关闭连接
cursor.close()
conn.close()
