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
from flask import Flask
import pandas as pd
# from sweetest.picture import Wsj
from multiprocessing import Process, Pool
from qingtest.globals import g
from flask import Flask, request, jsonify
import tkinter as tk
import  threading
# from enum import Enum
# class Yongli(Enum):
#     # 为序列值指定value值
#     message = 1

import requests
app = Flask(__name__)
app.debug = True
b =""
o=""
c =""
baseurl=""
password=""
email =""
# taskid = ""

# messageKey ="42b1749e-83d2-4f01-aba9-c996c61b1b64"
# import threading
# import time
# exitFlag = 0
#
# class myThread (threading.Thread):
#    def __init__(self, threadID, name, counter):
#          threading.Thread.__init__(self)
#          self.threadID = threadID
#          self.name = name
#          self.counter = counter
#
#          def run(self):
#            print ("开始线程：" + self.name)
#            print_time(self.name, self.counter, 1, self.app_id)
#            print ("退出线程：" + self.name)
#
# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1

@app.route("/jiekou", methods=["POST"])

def check():
    # 获取传入的参数

    get_Data = request.get_data()
    # 传入的参数为bytes类型，需要转化成json
    get_Data = json.loads(get_Data)
    baseurl = get_Data.get('baseurl')
    password = get_Data.get('password')
    email =get_Data.get("email")
    # app_id =request.values.get("app_id")
    # yongli =get_Data.get("yongli")
    # 对参数进行操作
    g.baseurl = baseurl
    g.email = email
    g.password = password
    plan_name = 'qingflowopenapi'
    # 单 sheet 页面模式
    # a = 'login,qrobot,data,report,datalst,process-editing,charts,qrobot-email'
    # sheet_name = a.split(',')
    #
    sheet_name =['tongxunlu',"apply"]
    # ,'masterplate'
    # sheet_name = ["数据报表","应用相关"]
    # sheet_name = ['message','personnel','应用相关','应用包信息','应用设置发布','流程日志数据日志留言','插件中心','进程中心','应用数据','单条数据','表单','流程','dashboard','数据报表','工作区信息','个人动态','个人设置偏好']
    # sheet_name = a.split(',')
    # python -m ensurepip
    # 环境配置信息
    # Chrome
    desired_caps = {'platformName': 'Desktop', 'browserName': 'Chrome', 'headless': True}
    server_url = ''
    # 初始化自动化实例
    sweet = Autotest(plan_name, sheet_name, desired_caps, server_url)
    # 创建新线程
    # thread1 = myThread(1, "Thread-1", 1)
    # # 开启新线程
    # thread1.start()
    w = Wsj()
    w.get_picture()
    tk.mainloop()
    sweet.plan()
    # 开启新线程
    # thread1.start()
    if (sweet.code) ==0:
       return  "接口测试通过"
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
        res["failure"] = k
    return res
      # return  sweet.testsuite_data
# 功能函数
if __name__ == "__main__":
    # pool = Pool(processes=4)

    app.run(debug=False, host='0.0.0.0', port=8800)


# #

# -*- coding=utf-8 -*-
#



# 如果是集成到 CI/CD，则给出退出码；也可以根据上面的测试结果自己生成退出码
# sys.exit(sweet.code)