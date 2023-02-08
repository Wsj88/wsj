# b = a["data"].split("headers=")[1]
import  json
# a = {'id': 'api_001', 'title': '添加数据', 'condition': '', 'step': 1.0, 'keyword': 'POST', 'page': '应用数据', 'element': 'openapi-删除数据', 'data': 'headers={"Content-Type": "application/json","accessToken":"1"},,json={"answers": [{"queId": 24261452, "queType": 2, "values": [{"value": "测试吴上进"}], "tableValues": []}]},,', 'expected': "status_code=200,,json={'result.requestId':'<requestId>'}", 'output': '', 'priority': '', 'designer': '', 'flag': '', 'score': '', 'result': '', 'remark': ''}
# b2 = a["data"].split("json=")[0]
# b0 = a["data"].split("json=")[1]
# print(b0)
# print(b2)
# b3 = b2.split("headers=")[1]
# print(b3)
# b4 = b3.split(",,")[0]
# b5 = json.loads(b4)
# b5["accessToken"] =2
# b7 = json.dumps(b5)
# b8 = "headers="+b7+",,"+"json="+b0
# print(b8)
# a = {'id': 'api_001', 'title': '添加数据', 'condition': '', 'step': 1.0, 'keyword': 'POST', 'page': '应用数据', 'element': 'openapi-删除数据', 'data': 'headers={"Content-Type": "application/json","accessToken":"1"},,', 'expected': "status_code=200,,json={'result.requestId':'<requestId>'}", 'output': '', 'priority': '', 'designer': '', 'flag': '', 'score': '', 'result': '', 'remark': ''}
# d1 = a ["data"].split("headers=")[1]
# d2 = d1.split(",,")[0]
# print(d2)
# d3 = json.loads(d2)
# d3["accessToken"] =2
# d4 = json.dumps(d3)
# d5 = "headers=" + d4 +",,"
# print(d5)
# print(d4)
# print(type(b4))
# a = {'code': 0, 'data': {'17566104': {'auditNodeId': 17566104, 'autoJudges': [], 'beingBranchEnd': True, 'nextId': 17566102, 'nodeState': None, 'prevId': 17566102, 'type': 2}, '17566103': {'auditNodeId': 17566103, 'autoJudges': [], 'beingBranchEnd': True, 'nextId': 17566102, 'nodeState': None, 'prevId': 17566102, 'type': 2}, '17566102': {'auditNodeId': 17566102, 'beingBranchEnd': False, 'nextId': 17566099, 'nodeState': None, 'prevId': 7430797, 'type': 1}}, 'message': 'success'}
# b = a["data"]["17566104"]["auditNodeId"]
# print(b)
# j= {'code': 0, 'data': {'pubkey': 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDDH/tnqpmFtlslE2rxcC8wCmlNE4yqiMZx9/APnu7pKVvXE+vt+y+4vH0dUruN6MT8KpBkV4h9jc8PBOBvAJ47FutAhwpnQHt7YlLP+V7Kbv9PZNrFuFzRmoieVv8V8zv/Nok4CKkjj/oZke7/2sjBMivYVsMK68z19+cX9Fuy7wIDAQAB'}, 'message': 'success'}
# respose["json"]=j
# if "pubkey" in j["data"]:
#     print("1")
# else:
#     print("2")
#
# a = j["data"]["pubkey"]
# print(a)
a = {'code': 0, 'data': {'17566104': {'auditNodeId': 17566104, 'autoJudges': [], 'beingBranchEnd': True, 'nextId': 17566102, 'nodeState': None, 'prevId': 17566102, 'type': 2}, '17566103': {'auditNodeId': 17566103, 'autoJudges': [], 'beingBranchEnd': True, 'nextId': 17566102, 'nodeState': None, 'prevId': 17566102, 'type': 2}, '17566102': {'auditNodeId': 17566102, 'beingBranchEnd': False, 'nextId': 17566099, 'nodeState': None, 'prevId': 7430797, 'type': 1}}, 'message': 'success'}
b = a["data"]
for item in b.items():
   print(item[0])
c = item[0]
print(c)
d = {'code': 0, 'data': {'editVersionNo': 954}, 'message': 'success'}
print(d['data']['editVersionNo'])
