import math

import pymysql
import psycopg2

mysql_host = ''
mysql_port =
mysql_user = ''
mysql_password = ''
mysql_database = ''

greenplum_host = ''
greenplum_port =""
greenplum_user = ''
greenplum_password = ''
greenplum_database = ''

default_num = "100"
default_capacity = "2097152"

def dataset():
    print("--------------------------开始执行数据集数据初始化--------------------------------")
    wsIdList = []  # wsid初始数据数组
    tableNameList = []  # 数据源表名

    # 创建mysql Connection连接
    mysqldb = pymysql.connect(
        host=mysql_host,
        port=mysql_port, user=mysql_user,
        password=mysql_password,
        database=mysql_database, charset='utf8')
    mysqldb.autocommit(1)
    # 获得Cursor对象
    mysqlConn = mysqldb.cursor()
    # 执行select语句 按工作区id升序查询出工作区下的所有数据源表
    mysqlCount = mysqlConn.execute('select ws_id, dataset_id from bi_dataset_config where ws_id = 110146 order by ws_id')

    # 打印受影响的行数
    print("查询到%d条数据" % mysqlCount)
    # 将查询结果放入对应数组中
    mysqlResult = mysqlConn.fetchall()
    # 获取查询的结果
    for row in mysqlResult:
        wsIdList.append(row[0])
        tableNameList.append(row[1])

    # 创建PostgresSQL Connection连接
    postgresqldb = psycopg2.connect(
        database=greenplum_database, user=greenplum_user,
        password=greenplum_password,
        host=greenplum_host, port=greenplum_port)
    postgresqldb.autocommit = True
    # 获得Cursor对象
    postgresqlConn = postgresqldb.cursor()

    wsSize = 0
    wsNum = 1
    flag = 0
    s = "(%d,%d,%d,%d,'%s')"
    replaceSql = 'replace into bi_data_capacity_and_num (`ws_id`,`num`,`capacity`,`virtual_capacity`,`data_type`) values '
    for i in range(0, len(wsIdList)):
        tableName = "'large_table_" + tableNameList[i] + "'"  # 对应表名
        tableSize = 0
        try:
            # 执行select语句
            postgresqlConn.execute('select pg_relation_size(' + tableName + ')')
            result = postgresqlConn.fetchone()
            tableSize = result[0]
        except BaseException as e:
            print(e.args)
        # 是最后一个
        if len(wsIdList) == i+1:
            # 是最后一个并且和前一个ws不同 需要先将上一个工作区处理完
            if wsIdList[i] != wsIdList[i - 1]:
                size = math.ceil(wsSize/1024)
                sql = s % (wsIdList[i - 1], wsNum - 1, size, size, "dataset")
                if flag != 0:
                    replaceSql = replaceSql + ','
                replaceSql = replaceSql + sql
                flag = 1
                wsSize = 0
                wsNum = 1
            # 将当前数据写入sql
            wsSize = wsSize + tableSize
            size = math.ceil(wsSize / 1024)
            sql = s % (wsIdList[i], wsNum, size, size, "dataset")
            if flag != 0:
                replaceSql = replaceSql + ','
            replaceSql = replaceSql + sql
        # 不为第一个且和前面ws不同
        elif i != 0 and wsIdList[i] != wsIdList[i - 1]:
            size = math.ceil(wsSize/1024)
            sql = s % (wsIdList[i - 1], wsNum - 1, size, size, "dataset")
            if flag != 0:
                replaceSql = replaceSql + ','
            replaceSql = replaceSql + sql
            flag = 1
            wsSize = 0
            wsNum = 1
        wsSize = wsSize + tableSize
        wsNum = wsNum + 1
    # 打印查询的结果
    mysqlConn.execute(replaceSql)
    # 关闭Cursor对象
    mysqlConn.close()
    postgresqldb.close()

def dataorigin():
    print("--------------------------开始执行数据源数据初始化--------------------------------")

    wsIdList = []  # wsid初始数据数组
    tableNameList = []  # 数据源表名

    # 创建mysql Connection连接
    mysqldb = pymysql.connect(
        host=mysql_host,
        port=mysql_port, user=mysql_user,
        password=mysql_password,
        database=mysql_database, charset='utf8')
    # 获得Cursor对象
    mysqldb.autocommit(1)
    mysqlConn = mysqldb.cursor()
    # 执行select语句 按工作区id升序查询出工作区下的所有数据源表
    mysqlCount = mysqlConn.execute(
        'select o.ws_id, c.table_name from bi_dataorigin o join bi_dataorigin_sheet s join bi_sheet_config c on '
        'o.dataorigin_id = s.dataorigin_id and s.sheet_id = c.sheet_id where o.ws_id = 110146 order by o.ws_id')

    # 打印受影响的行数
    print("查询到%d条数据" % mysqlCount)
    # 将查询结果放入对应数组中
    mysqlResult = mysqlConn.fetchall()
    # 获取查询的结果
    for row in mysqlResult:
        wsIdList.append(row[0])
        tableNameList.append(row[1])

    # 创建PostgresSQL Connection连接
    postgresqldb = psycopg2.connect(
        database=greenplum_database, user=greenplum_user,
        password=greenplum_password,
        host=greenplum_host, port=greenplum_port)
    postgresqldb.autocommit = True
    # 获得Cursor对象
    postgresqlConn = postgresqldb.cursor()

    wsSize = 0
    wsNum = 1
    flag = 0
    s = "(%d,%d,%d,%d,'%s')"
    replaceSql = 'replace into bi_data_capacity_and_num (`ws_id`,`num`,`capacity`,`virtual_capacity`,`data_type`) values '
    for i in range(0, len(wsIdList)):
        tableName = "'" + tableNameList[i] + "'"  # 对应表名
        tableSize = 0
        try:
            # 执行select语句
            postgresqlConn.execute('select pg_relation_size(' + tableName + ')')
            result = postgresqlConn.fetchone()
            tableSize = result[0]
        except BaseException as e:
            print(e.args)
        # 是最后一个
        if len(wsIdList) == i + 1:
            # 是最后一个并且和前一个ws不同 需要先将上一个工作区处理完
            if wsIdList[i] != wsIdList[i - 1]:
                size = math.ceil(wsSize / 1024)
                sql = s % (wsIdList[i - 1], wsNum - 1, size, size, "dataorigin")
                if flag != 0:
                    replaceSql = replaceSql + ','
                replaceSql = replaceSql + sql
                flag = 1
                wsSize = 0
                wsNum = 1
            # 将当前数据写入sql
            wsSize = wsSize + tableSize
            size = math.ceil(wsSize / 1024)
            sql = s % (wsIdList[i], wsNum, size, size, "dataorigin")
            if flag != 0:
                replaceSql = replaceSql + ','
            replaceSql = replaceSql + sql
        # 不为第一个且和前面ws不同
        elif i != 0 and wsIdList[i] != wsIdList[i - 1]:
            size = math.ceil(wsSize / 1024)
            sql = s % (wsIdList[i - 1], wsNum - 1, size, size, "dataorigin")
            if flag != 0:
                replaceSql = replaceSql + ','
            replaceSql = replaceSql + sql
            flag = 1
            wsSize = 0
            wsNum = 1
        wsSize = wsSize + tableSize
        wsNum = wsNum+1
    mysqlConn.execute(replaceSql)
    # 关闭Cursor对象
    mysqlConn.close()
    postgresqldb.close()


def data_limit():
    print("--------------------------开始执行用户限制数据初始化--------------------------------")

    size = 300
    default = "(%d," + default_num + ",0,'dataset'),(%d," + default_num + ",0,'dataorigin'),(%d,0," + default_capacity + ",'dataall')"
    tempSql = 'replace into bi_data_capacity_and_num_limit (`ws_id`,`num`,`capacity`,`data_type`) values '

    # 创建mysql Connection连接
    mysqldb = pymysql.connect(
        host=mysql_host,
        port=mysql_port, user=mysql_user,
        password=mysql_password,
        database=mysql_database, charset='utf8')
    # 获得Cursor对象
    mysqldb.autocommit(1)
    mysqlConn = mysqldb.cursor()
    replace = mysqldb.cursor()
    # 执行select语句 按工作区id升序查询出工作区下的所有数据源表
    mysqlCount = mysqlConn.execute(
        'select ws_id from bi_vip')

    # 打印受影响的行数
    print("查询到%d条数据" % mysqlCount)

    while True:
        mysqlResult = mysqlConn.fetchmany(size)
        if not mysqlResult:
            break
        i = 0
        replaceSql = tempSql
        for row in mysqlResult:
            if i >= 1:
                replaceSql = replaceSql + " , "
            replaceSql = replaceSql + default % (row[0], row[0], row[0])
            i = i+1
        replaceSql = replaceSql
        aa = mysqldb.cursor()
        aa.execute(replaceSql)
    replace.close()
    mysqlConn.close()

def dataall():
    print("--------------------------开始执行总容量sql--------------------------------")
    mysqldb = pymysql.connect(
        host=mysql_host,
        port=mysql_port, user=mysql_user,
        password=mysql_password,
        database=mysql_database, charset='utf8')
    mysqldb.autocommit(1)
    # 获得Cursor对象
    mysqlConn = mysqldb.cursor()
    mysqlConn.execute("replace into bi_data_capacity_and_num (`ws_id`,`capacity`,`virtual_capacity`,`data_type`) (select ws_id ,sum(capacity) as capacity ,sum(virtual_capacity) as virtual_capacity ,'dataall' from bi_data_capacity_and_num where ws_id = 110146 and `data_type` != 'dataall' group by ws_id )")

if __name__ == '__main__':
    dataset()
    dataorigin()
    dataall()
    # data_limit()
