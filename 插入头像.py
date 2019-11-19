



import pymysql


# 连接数据库
db = pymysql.connect(host="127.0.0.1",
                     port=3306,
                     user="root",
                     password="123456",
                     database="stu",
                     charset="utf8")
# 生成游标对象(用于操作数据库数据，获取sql执行结果的对象)
cur = db.cursor()

# with open("lyf.jpg","rb") as f:
#     date = f.read()

# try:
#     sql = "update class1 set img=%s where id=1;"
#     cur.execute(sql,[date])
#     db.commit()
# except:
#     db.rollback()


sql = "select img from class1 where name='Abby'"
cur.execute(sql)
data =cur.fetchone()

with open("lyf.jpg","wb")as f:
    f.write(data[0])



    # 关闭游标和数据库连接
cur.close()
db.close()