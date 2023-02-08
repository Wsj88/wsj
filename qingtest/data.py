import xlrd
from qingtest.utility import Excel, data2dict
from qingtest.config import header
from qingtest.globals import g
import json


def testsuite_format(data):
    '''
    将元素为 dict 的 list，处理为 testcase 的 list
    testcase 的格式：
    {
        'id': 'Login_001',  #用例编号
        'title': 'Login OK',  #用例标题
        'condition': '',  #前置条件
        'designer': 'Leo',  #设计者
        'flag': '',  #自动化标记
        'result': '',  #用例结果
        'remark': '',  #备注
        'steps':
            [
                {
                'no': 1,  #测试步骤
                'keyword': '输入',
                'page': '产品管系统登录页',
                'element': '用户名',
                'data': 'user1',  #测试数据
                'output': '',  #输出数据
                'score': '',  #测试结果
                'remark': ''  #备注
                },
                {……}
                ……
            ]
    }
    '''
    testsuite = []
    testcase = {'testsuite': '', 'no': 0}
    data = data2dict(data)

    for d in data:
        # 如果用例编号不为空，则为新的用例
        email = g.email
        password = g.password
        accessToken =g.accessToken
        if d["element"] == "登录":
            b0 = d["data"].split("json=")[0]
            b =  d["data"].split("json=")[1]
            b1 = json.loads(b)
            b1["email"] = email
            b1["password"] = password
            # 以上为取出赋值操作
            # 以下逆向操作，重新写入a中
            b2 = json.dumps(b1)
            b3 = b0 + "json=" + b2
            d["data"] = b3
            print(d)
        if "openApi" in d["page"]:
            if d["keyword"] == "GET":
                d1 = d["data"].split("headers=")[1]
                d2 = d1.split(",,")[0]
                d6 = d1.split(",,")[1]
                d3 = json.loads(d2)
                d3["accessToken"] = accessToken
                d4 = json.dumps(d3)
                d5 = "headers=" + d4 + ",,"+d6
                d["data"] = d5
            else:
                c2 = d["data"].split("json=")[0]
                c0 = d["data"].split("json=")[1]
                c3 = c2.split("headers=")[1]
                c4 = c3.split(",,")[0]
                c5 = json.loads(c4)
                c5["accessToken"] = accessToken
                c7 = json.dumps(c5)
                c8 = "headers=" + c7 + ",," + "json=" + c0
                d["data"] = c8
        if d['id'].strip():
            # 如果 testcase[id] 非空，则添加到 testsuite 里，并重新初始化 testcase
            if testcase.get('id'):
                testsuite.append(testcase)
                testcase = {'testsuite': '', 'no': 0}
            for key in ('id', 'title', 'condition', 'designer', 'flag', 'result', 'remark'):
                testcase[key] = d[key]
            if '#' in d['id']:
                testcase['set'] = d['id'].split('#')[0]
                testcase['flag'] = 'N'
            testcase['priority'] = d['priority'] if d['priority'] else 'M'
            testcase['steps'] = []
        # 如果测试步骤不为空，则为有效步骤，否则用例解析结束
        no = str(d['step']).strip()
        if no:
            step = {}
            step['control'] = ''
            if no[0] in ('^', '>', '<', '#'):
                step['control'] = no[0]
                step['no'] = no
            else:
                step['no'] = str(int(d['step']))
            for key in ('keyword', 'page', 'element', 'data', 'expected', 'output', 'score', 'remark'):
                step[key] = d.get(key, '')

            # 仅作为测试结果输出时，保持原样
            step['_keyword'] = d['keyword']
            step['_element'] = d['element']
            step['_data'] = d['data']
            step['vdata'] = d.get('data', '')
            step['_expected'] = d.get('expected', '')
            step['_output'] = d.get('output', '')
            testcase['steps'].append(step)
    if testcase:
        testsuite.append(testcase)
    return testsuite


def testsuite_from_excel(file_name, sheet_name):
    d = Excel(file_name)
    return testsuite_format(data2dict(d.read(sheet_name)))


def testsuite2data(data):
    # result = [list(header.values())]
    result = [[g.header_custom[key.lower()] for key in header.values()]]
    for d in data:
        s = d['steps'][0]  # 第一步和用例标题同一行
        testcase = [d['id'], d['title'], d['condition'], s['no'], s['_keyword'], s['page'], s['_element'],
                    s['vdata'], s['_output'], d['priority'], d['designer'], d['flag'], s['score'], d['result'], s['remark']]
        if g.header_custom['expected']:
            testcase.insert(8, s['_expected'])
        result.append(testcase)
        for s in d['steps'][1:]:
            step = ['', '', '', s['no'], s['_keyword'], s['page'], s['_element'],
                    s['vdata'], s['_output'], '', '', '', s['score'], '', s['remark']]
            if g.header_custom['expected']:
                step.insert(8, s['_expected'])
            result.append(step)
    return result


def testsuite2report(data):
    report = []
    for case in data:
        if case['condition'] in ('BASE', 'SETUP') or case['flag'] != 'N':
            for step in case['steps']:
                step['keyword'] = step.pop('_keyword')
                step['element'] = step.pop('_element')
                step['data'] = str(step.pop('vdata'))
                step['expected'] = step.pop('_expected')
                step['output'] = step.pop('_output')
            report.append(case)
    return report
