import sqlite3

import os

# # 数据库
dbName = os.path.abspath(os.path.dirname(__file__)) + "/defects.db"
print(dbName)
conn = sqlite3.connect(dbName)
cursor = conn.cursor()

# 后续封装成方法 只调用一次 其他crud另外写

# 创建表 用户
# try:
#     create_tb = ''' create table if not exists user_tb(
#     userId INTEGER PRIMARY KEY AUTOINCREMENT,
#     user_name varchar(64),
#     user_pass varchar(64));'''
#     cursor.execute(create_tb)
#     print("ok")
# except:
#     print("create fail")

# # 创建表 放数据
# try:
#     create_tb = ''' create table if not exists data_tb(
#     dataId INTEGER PRIMARY KEY AUTOINCREMENT,
#     data_name varchar(64),
#     attribute_01 varchar(64),
#     attribute_02 varchar(64),
#     attribute_03 varchar(64)
#     );'''
#     cursor.execute(create_tb)
#     print("ok")
# except:
#     print("table err")

# 插入初始数据
# insert_tb_user = ''' insert into user_tb(user_name,user_pass) values("admin","admin")'''
# cursor.execute(insert_tb_user)
# conn.commit()

#
# insert_tb_data = ''' insert into data_tb(data_name,attribute_01,attribute_02,attribute_03)
# values("xxx监测数据2","属性一的数据：88","属性2的数据：66","属性3的数据：11")'''
# cursor.execute(insert_tb_data)
# conn.commit()
# conn.close()

'''查询数据'''

def queryData(self, sql):
    dbName = os.path.abspath(os.path.dirname(__file__)) + "/defects.db"
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results


'''更新数据'''

def updateData(self, sql):
    dbName = os.path.abspath(os.path.dirname(__file__)) + "/defects.db"
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()



# 打印一下 是否写入
# query_tb_user = '''select * from user_tb'''
# # res=queryData("",query_tb_user)

# query_tb_data = '''select * from data_tb'''
# res = queryData("", query_tb_data)
#
# for i in res:
#     print(i)
