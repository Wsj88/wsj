import json
import requests
from flask import  Flask,request
from concurrent.futures import ThreadPoolExecutor
import uuid
executor = ThreadPoolExecutor()
app = Flask(__name__)
uuid =uuid.uuid1()
def slutiontime():
    print("yibukaishi")
    url_singnup1 = "https://develop-test.oalite.com/api/share/user/signup"
    header_token = {"Content-Type": "application/json"}
    data_token = {"email":"76767600009@qq.com","password":"AwXCVKmcTGKEDHRLmTyh4KNg6mWSygXaSq3oR6S9c/aQUJYQwOGTbkAROn2F4PKn/sdg8cwFjsCKmbuL34Q6ZVGEN+AHkysUG0yYdRdrzZmD0ZG9Cifh/YHNb1Ee/pSkPy+BoGYAHyRwbXhKBAcXAHBOb1hUd+7NAx2iGPzciPQ=","code":"999999","mobile":"76767600009","areaCode":"86","source":"home_home","uuid":"544ae1f2-2553-4caa-ad70-745f5dab353b","signUpSource":"home","beingInvited":False,"utmInfo":None,"bdVid":"","beingPrivacyPolicy":True,"registerSource":"normal"}
    r_token = requests.post(url=url_singnup1, headers=header_token, json=data_token)
    b = json.loads(r_token.text)["token"]
    w = -1
    print(b)
    v = {'result': []}
    k = []
    for i in slutionkey:
        w = w+1
        print(w)
        url = "https://qingflow.com/api/app"
        header = {"token": b, "wsId": "110146", "Content-Type": "application/json"}
        data = {"solutionKey":i,"beingCopyData":True,"solutionSource":"solutionDetail"}
        print(header)
        print(data)
        r = requests.post(url=url, json=data, headers=header)
        print(type(r.text))
        """
        删除安装的解决方案
        """
        dele = json.loads(r.text)["tagIds"]
        print(dele)
        url_delete ="https://api.qingflow.com/tag"
        data_delete = {"tagIds":dele,"clearAll":True}
        header_delete = {"accessToken":"a68db3ea-ac45-4e8d-9bb8-8b1ce6101558","Content-Type": "application/json"}
        r_delete =requests.delete(url=url_delete,headers=header_delete,json=data_delete)
        print(r_delete.text)
        h = r.elapsed.total_seconds()
        p = round(h,1)
        print(p)
        x = str(p)+"s"+name[w]+"，"
        k.append(x)
        print(v)
    v["result"] = k
    print(k)
    globalk = k
    globalv = v
    return v
"""
启动安装解决方案
"""
@app.route('/jiankong',methods=['post'])
def  run():
    u=""
    get_Data = request.get_data()
    # 传入的参数为bytes类型，需要转化成json
    get_Data = json.loads(get_Data)
    password = get_Data.get('password')
    if password == "wsj":
       executor.submit(lambda p: slutiontime(),u)
       return  {"result":"开始安装解决方案～"}
    else:
       return {"result":'请输入正确的密钥'}
"""
查询解决方案耗时
"""
@app.route('/',methods=["get"])
def  result():
   params = request.args
   password = params.get("password")
   set1 = set(globalk)
   print(globalk)
   print(set1)
   if password == "wsj":
       if len(set1) >= 8 :
         return globalv
       else:
         return {"reult":["正在安装解决方案,请稍等～"]}
   else:
       return {"result":["请输入正确的值"]}
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8805)

