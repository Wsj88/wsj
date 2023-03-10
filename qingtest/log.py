import logging
import datetime
from pathlib import Path
import sys
from qingtest.utility import mkdir


def today():
    now = datetime.datetime.now()
    return now.strftime('%Y%m%d')



def set_log(logger, log_path):
    mkdir('log')

    # 文件日志
    log_file = Path('log') / f'{today()}.log'
    file_handler = logging.FileHandler(filename=log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式

    # 单次文件日志
    sweet_log = log_path / 'sweet.log'   
    try:
        sweet_log.unlink()
    except:
        pass
    sweet_handler = logging.FileHandler(filename=sweet_log, encoding="utf-8")
    sweet_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式

    # 控制台日志
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.formatter = formatter  # 也可以直接给formatter赋值

    # 为logger添加的日志处理器
    logger.addHandler(file_handler)
    logger.addHandler(sweet_handler)    
    logger.addHandler(console_handler)

    # 指定日志的最低输出级别，默认为WARN级别
    # DEBUG，INFO，WARNING，ERROR，CRITICAL
    logger.setLevel(logging.INFO)

    return str(sweet_log)

# 获取logger实例，如果参数为空则返回root logger
logger = logging.getLogger("qingtest-01")
# 指定logger输出格式
formatter = logging.Formatter('%(asctime)s [%(levelname)s]: #  %(message)s')