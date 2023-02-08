# import tkinter
#!/接口测试
#-*- coding:utf-8 -*-
from qingtest import Autotest
from gevent import pywsgi
import sys
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
b =""
o=""
c =""
baseurl=""
password=""
email =""
l =""
# taskid = 1
executor = ThreadPoolExecutor()
app = Flask(__name__)
api = Api(app)
g.uid = "测试"
def run(baseurl,password,email,enviro):
    """
    # 异步任务
    """
    # 对参数进行操zuo
    plan_name = str(g.enviro)
    # 单 sheet 页面模式
    a = 'tongxunlu'
    sheet_name = a.split(',')
    #
    # sheet_name =['message']
    # ,'masterplate'
    sheet_name = ['personnel','应用相关','应用包信息','应用设置发布','流程日志数据日志留言','插件中心','进程中心','应用数据','单条数据','表单','流程','dashboard','数据报表','工作区信息','个人动态','个人设置偏好']
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
        g.res =res
    return res
    # time.sleep(3)
    # logger.info("name: %s, age: %s." % (name, age))
    # logger.info("耗时任务执行结束")
@app.route('/run',methods=['post'])
def check():
    g.res = ""
    get_Data = request.get_data()
    # 传入的参数为bytes类型，需要转化成json
    get_Data = json.loads(get_Data)
    baseurl = get_Data.get('baseurl')
    password = get_Data.get('password')
    email = get_Data.get("email")
    enviro = get_Data.get("enviro")
    # environment = get_Data.get("environment")
    g.baseurl = baseurl
    g.email = email
    g.password = password
    g.enviro =enviro
    executor.submit(lambda p: run(*p), get_Data)
    uid = uuid.uuid1()
    g.uid =uid
    result = {
        "code": "200",
        "message": "接口测试已启动",
         "taskid": uid
    }
    return  make_response(jsonify(result))
    # return  sweet.testsuite_data
@app.route('/result',methods=['get'])
def kkk():
    v = {"result": ["接口测试正在运行中"]}
    q ={"result":["接口测试没有报错啦~"]}
    result={"result":["请输入正确的taskid"]}
    params = request.args
    taskid = params.get("taskid")
    print(type(g.uid ))
    if taskid == str(g.uid):
        if g.res == "" :
            return v
        elif g.res =="cs":
            return q
        else:
          return g.res
    else:
          return result
# 功能函数
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8800)
# #

# -*- coding=utf-8 -*-
#



# 如果是集成到 CI/CD，则给出退出码；也可以根据上面的测试结果自己生成退出码
# sys.exit(sweet.code)