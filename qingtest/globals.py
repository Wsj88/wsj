import time

from qingtest.config import element_wait_timeout, page_flash_timeout


def now():
    t = time.time()
    return time.strftime("@%Y%m%d_%H%M%S", time.localtime(t))


def timestamp():
    # js 格式的时间戳
    return int(time.time() * 1000)


class Global:
    def __init__(self):
        self.start_time = now()
        self.start_timestamp = timestamp()
        self.plan_name = ''
        self.sheet_name = ''
        self.plan_data = {}
        self.testsuite_data = {}
        self.no = 1
        self.driver = ''
        self.snippet = {}
        self.caseset = {}
        self.baseurl = ""
        self.email = ""
        self.password = ""
        self.encr_password = ""
        self.res=""
        self.uid=""
        self.enviro =""
        self.accessToken =""
        self.sheetname=""

        # self.pubkey = ""

    def init(self, desired_caps, server_url):
        self.desired_caps = desired_caps
        self.server_url = server_url
        self.platform = desired_caps.get('platformName', '')
        self.browserName = desired_caps.get('browserName', '')
        self.headless = desired_caps.pop('headless', False)
        self.snapshot = desired_caps.pop('snapshot', False)
        self.executable_path = desired_caps.pop('executable_path', False)

    def set_driver(self):
        self.test_data = {'_last_': False}
        self.var = {}
        self.caseset = {}
        self.casesets = []  # 用例组合执行容器
        self.current_page = '通用'
        self.db = {}
        self.http = {}
        self.windows = {}
        # self.baseurl = {}
        self.action = {}
        self.wait_times = 0



    def plan_end(self):
        self.plan_data['plan'] = self.plan_name
        # self.plan_data['task'] = self.start_timestamp
        self.plan_data['start_timestamp'] = self.start_timestamp
        self.plan_data['end_timestamp'] = int(time.time() * 1000)

        return self.plan_data


g = Global()
