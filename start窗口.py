#!/接口测试
#-*- coding:utf-8 -*-
from qingtest import Autotest
# from sweetest.HTMLTestRunner import HTMLTestRunner
# from sweetest.picture import Wsj
from qingtest.globals import g
from flask import Flask
from qingtest.picture import wsj
import tkinter as tk

# from enum import Enum
# class Yongli(Enum):
#     # 为序列值指定value值
#     message = 1
app = Flask(__name__)
app.debug = True
baseurl=""
password=""
email =""
# taskid = ""
g.baseurl = baseurl
g.email = email
g.password = password
plan_name = 'private'
# 单 sheet 页面模式
# a = 'login,qrobot,data,report,datalst,process-editing,charts,qrobot-email'
# sheet_name = a.split(',')
#
# ,'masterplate'
# sheet_name = ["数据报表","应用相关"]
sheet_name = ['personnel','应用相关','应用包信息','应用设置发布','流程日志数据日志留言','插件中心','进程中心','应用数据','单条数据','表单','流程','dashboard','数据报表','工作区信息','个人动态','个人设置偏好']
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
w = wsj()
w.get_picture()
tk.mainloop()
sweet.plan()

