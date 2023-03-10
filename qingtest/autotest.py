import os.path
from pathlib import Path
import sys
import json
import requests
from qingtest.data import testsuite_format, testsuite2data, testsuite2report
from qingtest.parse import parse
from qingtest.elements import e
from qingtest.globals import g
from qingtest.windows import w
from qingtest.testsuite import TestSuite
from qingtest.utility import Excel, get_record, mkdir
from qingtest.log import logger, set_log
from qingtest.junit import JUnit
from qingtest.report import summary, markdown
from qingtest.config import _testcase, _elements, _report



class Autotest:

    def __init__(self, file_name, sheet_name, desired_caps={}, server_url=''):
        if desired_caps:
            self.desired_caps = desired_caps
        else:
            self.desired_caps = {
                'platformName': 'Desktop', 'browserName': 'Chrome'}
        self.server_url = server_url
        self.conditions = {}
        g.plan_name = file_name.split('-')[0]
        g.init(self.desired_caps, self.server_url)

        plan_path = Path('snapshot') / g.plan_name
        task_path = plan_path / g.start_time[1:]

        for p in ('JUnit', 'report', 'snapshot', plan_path, task_path, 'report/' + g.plan_name):
            mkdir(p)

        g.plan_data['log'] = set_log(logger, task_path)
        testcase_path = str(os.path.dirname( os.path.dirname(os.path.abspath(__file__))))+"/testcase/"
        self.testcase_file = testcase_path +str((file_name+'-'+_testcase+'.xlsx'))
        element_path = str(os.path.dirname( os.path.dirname(os.path.abspath(__file__))))+"/element/"
        self.elements_file = element_path +str((file_name+'-'+_elements+'.xlsx'))
        # self.testcase_file = str(
        #     Path('testcase') / (file_name + '-' + _testcase + '.xlsx'))
        # self.elements_file = str(
        #     Path('element') / (g.plan_name + '-' + _elements + '.xlsx'))
        self.report_xml = str(
            Path('JUnit') / (file_name + '-' + _report + g.start_time + '.xml'))
        self.testcase_workbook = Excel(self.testcase_file, 'r')
        self.sheet_names = self.testcase_workbook.get_sheet(sheet_name)
        self.report_excel = str(Path(
            'report') / g.plan_name / (file_name + '-' + _report + g.start_time + '.xlsx'))
        self.report_workbook = Excel(self.report_excel, 'w')
        self.report_filename = str(
            file_name + '-' + _report + g.start_time + '.xlsx')

        self.report_data = {}  # ????????????????????????

    def fliter(self, **kwargs):
        # ??????????????????????????????
        self.conditions = kwargs

    def plan(self):
        self.code = 0  # ?????????
        # 1.??????????????????
        try:
            e.get_elements(self.elements_file)
        except:
            logger.exception('*** Parse config file failure ***')
            self.code = -1
            sys.exit(self.code)

        self.junit = JUnit()
        self.junit_suite = {}

        # 2.????????????????????????
        for sheet_name in self.sheet_names:
            g.sheet_name = sheet_name
            # xml ?????????????????????
            self.junit_suite[sheet_name] = self.junit.create_suite(
                g.plan_name, sheet_name)
            self.junit_suite[sheet_name].start()

            self.run(sheet_name)

        self.plan_data = g.plan_end()
        self.testsuite_data = g.testsuite_data

        summary_data = summary(
            self.plan_data, self.testsuite_data, self.report_data, {})
        self.report_workbook.write(summary_data, '_Summary_')
        self.report_workbook.close()

        with open(self.report_xml, 'w', encoding='utf-8') as f:
            self.junit.write(f)

    def run(self, sheet_name):
        # 1.??? Excel ?????????????????????
        try:
            data = self.testcase_workbook.read(sheet_name)
            testsuite = testsuite_format(data)
            # logger.info('Testsuite imported from Excel:\n' +
            #             json.dumps(testsuite, ensure_ascii=False, indent=4))
            logger.info('From Excel import testsuite success')
        except:
            logger.exception('*** From Excel import testsuite failure ***')
            self.code = -1
            sys.exit(self.code)

        # 2.?????????????????????
        try:
            g.set_driver()
            # ????????????????????????????????????????????????????????????????????????????????????????????????
            data_file = Path('data') / (g.plan_name +
                                        '-' + sheet_name + '.csv')
            if data_file.is_file():
                g.test_data = get_record(str(data_file))
            w.init()
        except:
            logger.exception('*** Init global object failure ***')
            self.code = -1
            sys.exit(self.code)

        # 3.?????????????????????
        try:
            parse(testsuite)
            logger.debug('testsuite has been parsed:\n' + str(testsuite))
        except:
            logger.exception('*** Parse testsuite failure ***')
            self.code = -1
            sys.exit(self.code)

        # 4.??????????????????
        g.ts = TestSuite(testsuite, sheet_name,
                         self.junit_suite[sheet_name], self.conditions)
        g.ts.run()

        # 5.??????????????????
        if self.junit_suite[sheet_name].high_errors + self.junit_suite[sheet_name].medium_errors + \
                self.junit_suite[sheet_name].high_failures + self.junit_suite[sheet_name].medium_failures:
            self.code = -1

        # 6.??????????????????
        try:
            data = testsuite2data(testsuite)
            self.report_workbook.write(data, sheet_name)
            self.report_data[sheet_name] = testsuite2report(testsuite)
        except:
            logger.exception('*** Save the report is failure ***')

    def report(self, md_path):
        markdown(self.plan_data, self.testsuite_data,
                 self.report_data, md_path)

    def sendMessage(key, status, name):
        headers = {'content-type': "application/json"}
        url=f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}"
        if status == 1:
            result = "????????????"
        else:
            result = "????????????"

        content = {
            "msgtype": "text",
            "text": {
                "content": "????????????????????????\n" + "????????????"+name + "\n???????????????" + result,
                "mentioned_mobile_list": ["18939881330"]
            }
        }
        requests.post(url=url, data=json.dumps(content), headers=headers)

    def sendFile(key,file_id):
        url=f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}"
        headers = {'content-type': "application/json"}
        content = {
            "msgtype": "file",
            "file": {
                "media_id": file_id
                 }
            }
        s=requests.post(url=url, data=json.dumps(content), headers=headers)
        print(s.text)

