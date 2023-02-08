import  requests
import random
from flask import Flask, request, jsonify
import threading
import cx_Oracle
import os
import json

from flask_cors import *

app = Flask(__name__)
app.debug = True
r = str()
def insert(self):
    for i in range (1,2):
        b = "冲啊"+str(random.randint(1,150000000))

        data = {"type":1,"uploadFileSize":0,"answers":[{"queId":42372425,"queType":2,"values":[{"value":"张三"+b}],"tableValues":[]},{"queId":42372426,"queType":2,"values":[{"value":"吹牛"}],"tableValues":[]},{"queId":42372427,"queType":2,"values":[{"value":"好看"}],"tableValues":[]},{"queId":42372428,"queType":5,"values":[{"id":25754,"value":"铖cc"},{"id":9472,"value":"老王2"}],"tableValues":[]},{"queId":42372429,"queType":10,"values":[{"id":15060359,"otherInfo":"","value":"小米"}],"tableValues":[]},{"queId":42372430,"queType":2,"values":[{"value":"叶梅梅"}],"tableValues":[]},{"queId":42372431,"queType":8,"values":[{"value":"444"}],"tableValues":[]},{"queId":42372432,"queType":8,"values":[{"value":"222"}],"tableValues":[]},{"queId":42372433,"queType":8,"values":[{"value":"222"}],"tableValues":[]},{"queId":42372434,"queType":9,"values":[{"value":"https://develop-test.oalite.com/index/10271/app/58134e51/list/3"}],"tableValues":[]},{"queId":42372435,"queType":12,"values":[{"id":15060363,"otherInfo":"","value":"399"},{"id":15060364,"otherInfo":"","value":"899"}],"tableValues":[]},{"queId":42372436,"queType":21,"values":[{"value":"北京市","otherInfo":"110000","id":1},{"value":"北京市","otherInfo":"119000","id":2},{"value":"东城区","otherInfo":"110101","id":3},{"value":"","id":4}],"tableValues":[]},{"queId":42372437,"queType":14,"values":[{"value":"2022-06-17~2022-07-15"}],"tableValues":[]},{"queId":42372438,"queType":16,"values":[{"value":"<p>https://develop-test.oalite.com/index/10271/app/58134e51/list/3https://develop-test.oalite.com/index/10271/app/58134e51/list/3https://develop-test.oalite.com/index/10271/app/58134e51/list/3https://develop-test.oalite.com/index/10271/app/58134e51/list/3https://develop-test.oalite.com/index/10271/app/58134e51/list/3https://develop-test.oalite.com/index/10271/app/58134e51/list/3https://develop-test.oalite.com/index/10271/app/58134e51/list/3</p>"}],"tableValues":[]},{"queId":42372439,"queType":6,"values":[{"value":"15555896001@163.com"}],"tableValues":[]},{"queId":42372440,"queType":7,"values":[{"value":"15232323222"}],"tableValues":[]},{"queId":42372441,"queType":4,"values":[{"value":"2022-06-22"}],"tableValues":[]}]}
        headers = {"Content-Type": "application/json", "token": "f83ca3d2-3d4c-40b5-9bc1-1d096c5a00ce", "wsId": "4117"}
        reponse = requests.post(url="https://develop-test.oalite.com/api/app/58134e51/apply", json=data, headers=headers)
        print(reponse.text)
class myThread(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id = id
        pass
    def run(self):
        insert(id)
        #print ("开始操作%s"%i)
threads =[]
tlock=threading.Lock()
for  i in range(50):
    thread = myThread(i)
    threads.append(thread)

for i in range(len(threads)):
    threads[i].start()


#
# os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
#
# app = Flask(__name__)
# @app.route("/",methods=['post'])
#
# def  indextest():
#       amount = request.json.get("amount")
#       r = amount
#       return  insert()
#
# if __name__ =="__main__":
#     app.run(host="0.0.0.0",port=8000)