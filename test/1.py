# import json
# d = {'id': 'api_002', 'title': '查询添加数据结果', 'condition': '', 'step': 2.0, 'keyword': 'GET', 'page': 'openApi应用数据接口', 'element': '查询操作结果#<requestId>', 'data': 'headers={"Content-Type": "application/json","accessToken":"a68db3ea-ac45-4e8d-9bb8-8b1ce6101558"},,', 'expected': 'status_code=200,,', 'output': '', 'priority': '', 'designer': '', 'flag': '', 'score': '', 'result': '', 'remark': ''}
# d1 = d["data"].split("headers=")[1]
# print(d1)
# d2 = d1.split(",,")[0]
# d6 = d1.split(",,")[1]
# print(d2)
# print(d6)
# d3 = json.loads(d2)
# d3["accessToken"] = "22"
# d4 = json.dumps(d3)
# d5 = "headers=" + d4 + ",,"+d6
# d["data"] = d5
# print(d)
# a = [{'work_wechat_user_id': 'qingflow'}, {'work_wechat_user_id': 'privateqflow'}, {'work_wechat_user_id': 'wdl'}, {'work_wechat_user_id': 'test'}]
# c =[]
# for i in a:
#   print(i)
#   b = i["work_wechat_user_id"]
#   c.append(b)
# print(c)
# from flask import  Flask,request
# import  json
# app = Flask(__name__)
# app.debug = True
# a = ["赵黎峰","吴文可","周嘉辉","李蒙"]
# b  = -1
# @app.route("/",methods=["post"])
# def cs():
#     for i in a:
#        b = b+1
#        return a[b]
#
# if __name__ == "__main__":
#     # app.run()
#     app.run(host="0.0.0.0",port=8803,debug=True)






