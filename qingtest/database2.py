import pymysql
class Sqldriver(object):
    def __init__(self):
        self.host = '124.71.177.59'
        self.port = 5672
        self.user = 'root'
        self.password = 'qflow_955'
        self.database = 'autotest'

    # 连接数据库
    def Connect(self):
        self.db = pymysql.connect(

            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            charset='utf8',
            init_command="SET SESSION time_zone='+08:00'"
        )
    # 插入数据
    def insert(self,res,taskid):
        try:
            # 连接数据库
            self.Connect()
            # 创建游标
            global cursor
            cursor = self.db.cursor()
            # sql命令
            sql = "insert into jiekou (taskid,res)" \
                  " values(%s,%s)"
            # 执行sql语句
            cursor.execute(sql, (
                taskid,res))
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            self.db.commit()
            self.db.close()

    def update(self,res,taskid):
        try:
            # 连接数据库
            self.Connect()
            # 创建游标
            global cursor
            cursor = self.db.cursor()
            # sql命令
            sql = "update jiekou set res=%s where taskid =%s"
            print(sql)
            # 执行sql语句
            cursor.execute(sql, (
                res,taskid))
            # cursor.execute(sql)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            self.db.commit()
            self.db.close()

    def find(self, taskid):
        try:
            # 连接数据库
            self.Connect()
            # 创建游标
            global cursor
            cursor = self.db.cursor()
            # sql命令
            sql= "select res from jiekou where taskid =%s"
            # 执行sql语句
            cursor.execute(sql, (
                taskid))
            data = cursor.fetchall()
            return data
            # cursor.execute(sql)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            self.db.commit()
            self.db.close()

    def findAll(self):
        try:
            # 连接数据库
            self.Connect()
            # 创建游标
            global cursor
            cursor = self.db.cursor()
            # sql命令
            sql= "select taskid from jiekou"
            # 执行sql语句
            cursor.execute(sql)

            data2 = cursor.fetchall()
            a1 =list(data2)
            return  a1
            # cursor.execute(sql)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            self.db.commit()
            self.db.close()
    #查询数据
    # def find(self,taskid,res):
    #     try:
    #         # 连接数据库
    #         self.Connect()
    #         # 创建游标
    #         global cursor
    #         cursor = self.db.cursor()
    #         # sql命令
    #         sql = "select  test (taskid,res)" \
    #               " values(%s,%s)"
    #         # 执行sql语句
    #         cursor.execute(sql, (
    #             taskid,res))
    #     except Exception as e:
    #         print(e)
    #     finally:
    #         cursor.close()
    #         self.db.commit()
    #         self.db.close()
