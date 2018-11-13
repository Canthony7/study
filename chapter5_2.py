# --*-- coding:utf-8 --*--

import pymysql
import traceback
from redis import StrictRedis

db = pymysql.connect(host="localhost", user="root", password="123456", port=3306, db="spiders")
cursor = db.cursor()

# sql = "CREATE TABLE IF NOT EXISTS students (id VARCHAR (255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NULL, PRIMARY KEY (id))"
# cursor.execute(sql)

# id = "20100101"
# user = "Bob"
# age = 25
# sql = "INSERT INTO students(id, name, age) VALUE (%s, %s, %s)"
# try:
#     cursor.execute(sql, (id, user, age))
#     db.commit()
# except:
#     db.rollback()

# data = {
#     "id": "777",
#     "name": "anthony",
#     "age": 34
# }
# table = "students"
# keys = ",".join(data.keys())
# values = ",".join(["%s"]*len(data))
# sql = "INSERT INTO {table} ({keys}) VALUES ({values})".format(table=table, keys=keys, values=values)
#
# try:
#     cursor.execute(sql, tuple(data.values()))
#     db.commit()
#     print("successful")
# except:
#     db.rollback()
#     traceback.print_exc()

# sql = "UPDATE students SET age = %s WHERE name=%s"
# try:
#     cursor.execute(sql, (19, "anthony"))
#     db.commit()
# except:
#     traceback.print_exc()
#     db.rollback()





db.close()