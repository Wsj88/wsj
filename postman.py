import requests
import json

# url = "http://localhost:8800/run"
# data = {"baseurl":"https://qingflow.com/api","email":"qftest1206@126.com","enviro":"private","password":"123456"}
# data = json.dumps(data)
# headers ={"Content-Type":"application/json"}
# response = requests.post(url=url,data = data,)
# print(response.text.encode("utf-8"))
# #
def  a(self):
        url = " http://localhost:8800/result"
        taskid = ""
        params = {"taskid": taskid}
        response = requests.get(url, data=params)
        print(str(response.text))
def b():
    url = " http://localhost:8800/result"
    data = {"baseurl":"","password":"","email":"","enviro":""}
    data = json.loads(data)
    response = requests.post(url,data=data)

