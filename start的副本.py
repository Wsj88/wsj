# import tkinter
#!/接口测试
#-*- coding:utf-8 -*-
from qingtest import Autotest
from gevent import pywsgi
import sys
# import MySQLdb
import time
# from sweetest.HTMLTestRunner import HTMLTestRunner
import os
import qingtest.send
import json
from logzero import logger
import time
from flask import Flask
from flask_restful import Api
from flask import jsonify
from flask import make_response
from concurrent.futures import ThreadPoolExecutor
from flask import Flask
import pandas as pd
# from sweetest.picture import Wsj
from multiprocessing import Process, Pool
from qingtest.globals import g
from flask import Flask, request, jsonify
import  threading
import  uuid
from qingtest import database2

# b =""
# o=""
# c =""
# baseurl=""
# password=""
# email =""
# l =""
executor = ThreadPoolExecutor()
app = Flask(__name__)
api = Api(app)
# g.uid = "测试"
# db = database2.Sqldriver()
# db.update(res="23", taskid="d3eb1715-080c-11ed-826d-ef7ed0323842")
v = {"result": ["接口测试正在运行中"]}
q = '{"result": ["接口测试没有报错啦~"]}'
result ={"result": ["请输入正确的taskid"]}
def run(baseurl,password,email,enviro,accessToken,*args):
    """
    # 异步任务
    """
    # 对参数进行操zuo
    print("yibukaishi")
    plan_name = str(g.enviro)
    # 单 sheet 页面模式
    # a = 'personnel,应用相关,应用包信息,应用设置发布,流程日志数据日志留言,插件中心,进程中心,应用数据,单条数据,表单,流程,dashboard,数据报表,工作区信息,个人动态,个人设置偏好'
    # b ='tongxunlu,apply'

    sheet_name = g.sheetname.split(',')
    #
    # sheet_name =[yongli]
    # ,'masterplate'
    # sheet_name = ['personnel','应用相关','应用包信息','应用设置发布','流程日志数据日志留言','插件中心','进程中心','应用数据','单条数据','表单','流程','dashboard','数据报表','工作区信息','个人动态','个人设置偏好']
    # sheet_name = a.split(',')
    # python -m ensurepip
    # 环境配置信息
    # Chrome
    desired_caps = {'platformName': 'Desktop', 'browserName': 'Chrome', 'headless': True}
    server_url = ''
    # 初始化自动化实例
    sweet = Autotest(plan_name, sheet_name, desired_caps, server_url)
    sweet.plan()
    # 开启新线程
    # thread1.start()
    if (sweet.code) ==0:
         g.res="cs"
         db = database2.Sqldriver()
         db.update(res= q, taskid=g.uid)
         return
    else:
      k = []
      print(sweet.report_data)
      for i in sweet.report_data:
        print(sweet.report_data[i])
        o = sweet.report_data[i]
        print(o)
        for l in  o:
            if l["result"] == "failure":
              k.append(l["title"])
              print(k)
        res = dict() # 构造字典
        res["result"] = k
        print(res)
        print("g.uid",g.uid)
        db =database2.Sqldriver()
        db.update(res= str(res),taskid=g.uid)
        # g.res =res
    return res

    # time.sleep(3)
    # logger.info("name: %s, age: %s." % (name, age))
    # logger.info("耗时任务执行结束")
@app.route('/run',methods=['post'])
def check():
    uid = uuid.uuid1()
    g.uid = uid
    get_Data = request.get_data()
    # 传入的参数为bytes类型，需要转化成json
    get_Data = json.loads(get_Data)
    baseurl = get_Data.get('baseurl')
    password = get_Data.get('password')
    email = get_Data.get("email")
    enviro = get_Data.get("enviro")
    accessToken = get_Data.get("accessToken")
    print(baseurl)
    print(password)
    print(email)
    print(enviro)
    if enviro  == "openApi":
        sheetname = '子管理员,轻流应用接口,应用数据接口,通讯录,任务委托,子管理员,应用包,门户'
        # sheetname = "任务委托"
    # elif enviro  == "qingBi":
    #     sheetname = "filefunction,report,dataset,qbiReport"
    else:
        # sheetname = 'personnel,应用相关,应用包信息,应用设置发布,流程日志数据日志留言,插件中心,进程中心,应用数据,单条数据,表单,流程,dashboard,数据报表,工作区信息,个人动态,个人设置偏好,轻商城'
        sheetname = "流程"
    print(sheetname)
    g.baseurl = baseurl
    g.email = email
    g.password = password
    g.enviro =enviro
    g.sheetname = sheetname
    g.accessToken = accessToken
    print(type(g.sheetname))
    db = database2.Sqldriver()
    db.insert(res=None,taskid=uid)
    executor.submit(lambda p: run(*p), get_Data)
    result = {
        "code": "200",
        "message": "接口测试已启动",
         "taskid": uid
    }
    return  make_response(jsonify(result))
    # return  sweet.testsuite_data
@app.route('/result',methods=['get'])
def kkk():
    params = request.args
    taskid = params.get("taskid")
    db = database2.Sqldriver()
    a1= db.findAll()
    print(type(taskid))
    a2 = db.find(taskid)
    b1 = a2[0]
    c1 = list(b1)
    d = c1[0]
    print(d)
    if (taskid,) in a1:
    # if taskid == str(g.uid):
    #     if g.res == "" :
        if db.find(taskid) == ((None,),):
            return v
        elif db.find(taskid) ==(('{"result": ["接口测试没有报错啦~"]}',),):
            return q
        else:
          return  d
    else:
          return result
# 功能函数
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8802)
# #

# -*- coding=utf-8 -*-
#



# 如果是集成到 CI/CD，则给出退出码；也可以根据上面的测试结果自己生成退出码
# sys.exit(sweet.code)