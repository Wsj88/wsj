import json
import requests
from flask import  Flask,request
from concurrent.futures import ThreadPoolExecutor
executor = ThreadPoolExecutor()
app = Flask(__name__)
w = -1
"""
04a533ed  复工防疫
ea83deb4 设备巡检2.0
cbd896fb 工程项目管理
1ef2c3f5    互联网产品研发
e2941c1c  智能售后
bd73db01  集成式智能生产
597de24a   客户管理
14b2d8e4   招聘管理
"""
# slutionkey = ["f5da6a07", "ea83deb4","a2cb12af","bd73db01","e2941c1c","ce6efa87","990a4eb0","14b2d8e4"]
slutionkey =["14b2d8e4"]
# name = ["复工防疫","设备巡检","工程项目管理","集成式智能生产","智能售后","客户管理","互联网产品研发","招聘管理"]
name =["招聘管理"]
"""
统计时长
"""
globalk = []
globalv = {'result': []}

def slutiontime():
    global globalk
    global globalv
    globalk =[]
    globalv = {'result': []}
    print("yibukaishi")
    url_toekn = "https://qingflow.com/api/user/login"
    header_token = {"Content-Type": "application/json"}
    data_token = {"password":"einOK9tyfoiqWLkCbHQH51eBa8uOjtPfUSSsWPU8/qzqg7HrybyY72mbeyWZiFP7XGLHLWqZuxuwYqAAxoF7ep3o5bgEE/ssgBNExkwHMoB6tKlwxyfo38IMhrU8JWd2Bzjs9c8ipbmYiNgd31wQPYrh0ysvo6/ruWccVCX3r2M=","mobile":"","email":"qftest1206@126.com","areaCode":"86","loginType":"email"}
    r_token = requests.post(url=url_toekn, headers=header_token, json=data_token)
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


