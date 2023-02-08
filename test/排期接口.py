from flask import Flask, request
import json
import time
i = 0
app = Flask(__name__)
app.debug = True
@app.route("/", methods=['post'])
def check():
    global i
    get_Data = request.get_data()
    # 传入的参数为bytes类型，需要转化成json
    get_Data = json.loads(get_Data)
    a = get_Data.get('a')
    b = get_Data.get('b')
    c = get_Data.get("c")
    d = get_Data.get("d")
    list_name =[a,b,c,d]
    print(i)
    work_name = list_name[i]
    if i <=2:
      i = i+1
    else:
        i =0
    # 默认返回内容
    result ={"a":work_name,"b":i}
    return result

if __name__ == "__main__":
    # app.run()
    app.run(host="0.0.0.0",port=8807,debug=True)