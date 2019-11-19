"""
使用数据库完成登录注册功能，数据表自己拟定

*注册方法：收集用户信息，将用户信息存储到数据库，用户名不能重复
*登录方法：获取用户名密码，与数据库信息比对，判定是否允许登录
"""
import pymysql


class Database:
    def __init__(self):
        self.db = pymysql.connect(host="127.0.0.1",
                             port=3306,
                             user="root",
                             password="123456",
                             database="账号信息管理",
                             charset="utf8")
     # 生成游标对象(用于操作数据库数据，获取sql执行结果的对象)
        self.cur = self.db.cursor()

    def register(self, name, passwd):
        sql = "select 账号 from 账号信息 where 账号='%s';"%name
        self.cur.execute(sql)
        result = self.cur.fetchone()
        if result:
            return "账号已存在"
        try:
            sql = "insert into 账号信息 values (%s,%s);"
            self.cur.execute(sql,[name,passwd])
            self.db.commit()
            return "注册成功"
        except:
            self.db.rollback()
            return "注册失败"



    def login(self, name, passwd):
        sql = "select 账号,密码 from 账号信息 where 账号=%s and 密码=%s;"
        self.cur.execute(sql, [name, passwd])
        result = self.cur.fetchone()
        if result:
            return "登录成功"
        return "登录失败"


if __name__ == '__main__':
    db = Database()
    # print(db.register('a123','b123'))
    print(db.login('a123','b123'))


    #关闭游标和数据库连接
    db.cur.close()
    db.db.close()






