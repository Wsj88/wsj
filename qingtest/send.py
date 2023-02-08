from requests_toolbelt import MultipartEncoder
import sys
import json
import requests

# result = ""


def sendMessage(key, status, name, sheet_name):
    headers = {'content-type': "application/json"}
    url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=42b1749e-83d2-4f01-aba9-c996c61b1b64"
    if status == 1:
           result = "测试通过"
    else:
           result = "测试失败"

    content = {
        "msgtype": "text",
        "text": {
            "content": "自动化测试用例：" + name + "\n" + "功能：" + ("'" + "','".join(sheet_name) + "'") + "\n测试结果：" + result,
            "mentioned_mobile_list": ["18900565298"]
        }
    }
    r = requests.post(url=url, data=json.dumps(content), headers=headers)
    print(r.text+"test")


def sendFile(key, file_id):
    url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}"
    headers = {'content-type': "application/json"}
    content = {
        "msgtype": "file",
        "file": {
            "media_id": file_id
        }
    }
    s = requests.post(url=url, data=json.dumps(content), headers=headers)
    print(s.text+"test2")


def uploadFile(filepath, filename, access_token):
    post_file_url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key={access_token}&type=file"

    # m = MultipartEncoder(fields:{filename: ('file', open(filepath + Autotest., 'rb'), 'text/plain')})
    m = MultipartEncoder(fields = {filename: (filename, open(filepath, 'rb'))},)

    print(m)
    r = requests.post(url=post_file_url, data=m, headers={
        'Content-Type': "multipart/form-data"})
    print(r.text)
    return r.json()['media_id']


# def sendRequest(serverUrl, result, uuId):
#     headers = {'Content-Type': "application/json"}
#     content = {
#         "uuId": uuId,
#         "result": result
#     }
#     print("更新平台状态成功")
#     print(requests.post(serverUrl, json.dumps(content), headers=headers).text)



'''@allure.feature("轻流自动化测试模块")
class Test_Qtest():
    @allure.severity("normal")
    @allure.story("xxx测试用例")
    @allure.description("自动化测试")
    @pytest.mark.parametrize('sheet_name',getInfo())
    def test_runTest(self,testcase, sheet_name, messageKey, uuId, mobile,autotest_data):
        with allure.step("1.执行用例；2.断言结果"):
            program = Autotest(testcase, sheet_name,autotest_data,
                               {'platformName': 'Desktop', 'browserName': 'Chrome', 'snapshot': False, 'headless': True,
                                'mobile': mobile}, '')
            # program.fliter(id='LOGIN')
            program.plan()
            print(program.code)
        #加了下面代码就不会推送消息？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        #不会设生成测试报告再推送消息？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        with allure.step("自动化测试截图"):
            snapshot_plan = Path('snapshot') / g.plan_name
            snapshot_folder = snapshot_plan / g.start_time[1:]
            for filename in os.listdir(snapshot_folder):
                if filename.startswith(sheet_name):
                    with open(Path(snapshot_folder) / filename, mode='rb') as f:
                        file = f.read()
                    allure.attach(file, filename, allure.attachment_type.PNG)
                with open(Path(snapshot_folder) / 'sweet.log', mode='rb') as f:
                    word = f.read()
                    word_d = word.decode()
                    # error=re.search('ERROR',line)
                    str = 'ERROR'
                    assert str not in word_d

        if messageKey == "":
            if (program.code) == 0:
                send_test.sendRequest(serverUrl, "测试通过", uuId)
            else:
                send_test.sendRequest(serverUrl, "测试未通过", uuId)

        else:
            if (program.code) == 0:
                # media_id = send.uploadFile(program.report_excel, program.report_filename, messageKey)  # 获取临时文件的media_id
                send_test.sendMessage(messageKey, 1, testcase, sheet_name)  # 推送信息至企业微信
                # send.sendFile(messageKey, media_id)  # 推送文件至企业微信
                send_test.sendRequest(serverUrl, "测试通过", uuId)
            else:
                # media_id = send.uploadFile(program.report_excel, program.report_filename, messageKey)  # 获取临时文件的media_id
                send_test.sendMessage(messageKey, 0, testcase, sheet_name)  # 推送信息至企业微信
     pytest.main(['222test_index.py', '-s', '--alluredir', 'C:\\Autotest\\autotest\\Allure-reports\\temp'])
    os.system('allure generate C:\\Autotest\\autotest\Allure-reports\\temp -o  C:\Autotest\\autotest\Allure-reports\\report --clean')'''