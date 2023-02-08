#!/接口测试
#-*- coding:utf-8 -*-
from qingtest import Autotest
from qingtest.globals import g
from flask import Flask
from qingtest.picture import wsj
import tkinter as tk
test = wsj()
test.get_picture()
tk.mainloop()
# plan_name = str(g.enviro)
plan_name = "openApi"
# 单 sheet 页面模式
# a = 'personnel,应用相关,应用包信息,应用设置发布,流程日志数据日志留言,插件中心,进程中心,应用数据,单条数据,表单,流程,dashboard,数据报表,工作区信息,个人动态,个人设置偏好,轻商城'
a = '子管理员,轻流应用接口,应用数据接口,通讯录,任务委托,子管理员,应用包,门户'
sheet_name = a.split(',')
# sheet_name =['tongxunlu',"apply"]
# ,'masterplate'
# sheet_name = ["工作区信息"]
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
if (sweet.code) ==0:
    print("接口没有报错啦")
else:
    k=[]
    for i in sweet.report_data:
        o = sweet.report_data[i]
        for l in o:
            if l["result"] == "failure":
                k.append(l["title"])
        res = dict()  # 构造字典
        res["result"] = k
    print(res)
input('Press Enter to exit…')




