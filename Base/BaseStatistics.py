# -*- coding: utf-8 -*-

import xlsxwriter
from Base.BaseElementEnmu import Element
from Base.BaseExcel import OperateReport
from Base.BaseInit import destroy
from Base.BasePickle import *
from datetime import datetime
import time
import xlrd
import xlwt
from xlutils.copy import copy
import pandas

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

'''
统计数据相关
'''

'''
result bool
logTest 记录日志类 class
driver
testinfo

'''


def countInfo(**kwargs):
    _info = {}
    step = ""  # 操作步骤信息
    check_step = ""  # 检查点步骤信息

    for case in kwargs["testCase"]:
        step = step + case["info"] + "\n"

    if type(kwargs["testCheck"]) == list:  # 检查点为列表
        for check in kwargs["testCheck"]:
            check_step = check_step + check["info"] + "\n"
    elif type(kwargs["testCheck"]) == dict:
        check_step = kwargs["testCheck"]["info"]
    else:
        print("获取检查点步骤数据错误，请检查")
        print(kwargs["testCheck"])

    _info["step"] = step  # 用例操作步骤
    _info["checkStep"] = check_step  # 用例检查点

    if kwargs["result"]:
        _info["result"] = "通过"
        kwargs["logTest"].checkPointOK(driver=kwargs["driver"], caseName=kwargs["testInfo"][0]["title"],
                                       checkPoint=kwargs["caseName"] + "_" + kwargs["testInfo"][0].get(
                                           "msg", " "))
    else:
        _info["result"] = "失败"  # 用例接开关
        _info["img"] = kwargs["logTest"].checkPointNG(driver=kwargs["driver"], caseName=kwargs["testInfo"][0]["title"],
                                                      checkPoint=kwargs["caseName"] + "_" + kwargs["testInfo"][0].get(
                                                          "msg", " "))
    _info["id"] = kwargs["testInfo"][0]["id"]  # 用例id
    _info["title"] = kwargs["testInfo"][0]["title"]  # 用例名称
    _info["caseName"] = kwargs["caseName"]  # 测试函数
    _info["name"] = kwargs["name"]  # 设备名
    _info["msg"] = kwargs["testInfo"][0].get("msg", " ")  # 备注
    _info["info"] = kwargs["testInfo"][0]["info"]  # 前置条件

    writeInfo(data=_info, path=PATH("../Log/" + Element.INFO_FILE))
    # print(read(PATH("../Log/info.pickle")))


# 统计所有用例数
def countSum(result):
    # print("----countSum----")
    data = {"sum": 0, "pass": 0, "fail": 0}
    _read = read(PATH("../Log/sum.pickle"))
    if _read:
        data = _read
    data["sum"] = data["sum"] + 1
    if result:
        data["pass"] = data["pass"] + 1
    else:
        data["fail"] = data["fail"] + 1
    write(data=data, path=PATH("../Log/" + Element.SUM_FILE))
    # print(read(PATH("../Log/sum.pickle")))


def countDate(testDate, testSumDate):
    data = read(PATH("../Log/" + Element.SUM_FILE))
    if data:
        data["testDate"] = testDate
        data["testSumDate"] = testSumDate
        write(data=data, path=PATH("../Log/" + Element.SUM_FILE))
    else:
        print("统计数据失败")
    data = read(PATH("../Log/" + Element.SUM_FILE))
    print("==统计数据：%s==" % data)


'''
测试报告
'''


def writeExcel():
    currentTime = time.strftime('%Y-%m-%d')
    workbook = xlsxwriter.Workbook(PATH('../Report/' + currentTime + '_' + Element.REPORT_FILE))     # 创建一个Excel文档
    worksheet = workbook.add_worksheet("测试总况")   # 添加工作表
    worksheet2 = workbook.add_worksheet("测试详情")
    operateReport = OperateReport(workbook)
    operateReport.init(worksheet, read(PATH("../Log/" + Element.SUM_FILE)))
    operateReport.detail(worksheet2, readInfo(PATH("../Log/" + Element.INFO_FILE)))
    operateReport.close()
    # destroy()  # 删除文件


def write_append(data):
    workbook = PATH('../Log/' + Element.ORDER_FILE)
    excel = pandas.read_excel(workbook)
    rb = xlrd.open_workbook(workbook, formatting_info=True)  # 打开excel，保留文件格式
    wb = copy(rb)  # 利用xlutils.copy下的copy函数复制之前表里存在的数据
    ws = wb.get_sheet(0)  # 获取表单0
    ID = len(excel) + 1
    # data = 'abc'
    # data1 = 'abcd'
    list = [ID, data]  # 要写入的数据，这里以列表的形式
    line = len(excel) + 1
    for index, value in enumerate(list):  # 写入
        ws.write(line, index, value)
    wb.save(workbook)  # 保存的有旧数据和新数据

def read_append(args):
    workbook = PATH('../Log/' + Element.ORDER_FILE)
    excel = pandas.read_excel(workbook)
    data = pandas.DataFrame(excel) # 读取数据,设置None可以生成一个字典，字典中的key值即为sheet名字，此时不用使用DataFram，会报错
    ID = len(excel)
    # print(ID)
    # print(data.index)  # 获取行的索引名称
    # print(data.columns)  # 获取列的索引名称
    # print(data['姓名'])  # 获取列名为姓名这一列的内容
    record = data[args].loc[ID-1]  # 获取最后一行列名为Record的内容
    print("==读取的数据为：%s==" % record)
    return record


# def writeOrderData():
#     currentTime = time.strftime('%Y-%m-%d')
#     workbook = xlsxwriter.Workbook(PATH('../Report/' + Element.ORDER_FILE))
#     worksheet = workbook.add_worksheet("读取列表01")
#     worksheet2 = workbook.add_worksheet("读取列表02")
#
#
#     file_test = xlrd.open_workbook(r"F:\文档\测试文档\读写文件\test01.xlsx")#读取test1.xlsx文件
#     count=len(file_test.sheets())#获取该文件中的工作簿数
#     print("工作簿总数为：",count)
#     table1=file_test.sheet_by_name("Sheet1")#根据工作簿名字获取该工作簿的数据
#     nrows=table1.nrows #获取工作簿行数
#     ncols=table1.ncols #获取工作簿列数
#     print("Sheet1的行数为：",nrows,"列数为：",ncols)
#     #从第二行开始，遍历Sheet1中的数据（第一行为表头）
#     for i in range(1,nrows):
#         rowvalues=table1.row_values(i) #按行读取数据
#         key=rowvalues[1] #第一列为序号，我们取第二列的搜索词
#         print("搜索词：",key)
#         driver.find_element_by_id("kw").clear()#清空搜索框中的内容
#         driver.find_element_by_id("kw").send_keys(key) #根据搜索词填入百度搜索框
#         WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.ID,"su")))#显性等待
#         driver.find_element_by_id("su").click()#点击百度一下按钮
#         time.sleep(2)
#
#     operateReport = OperateReport(workbook)
#     operateReport.close()


if __name__ == '__main__':
    # writeInfo(data, PATH("../Log/info.pickle"))
    # writeInfo(data, PATH("../Log/info.pickle"))
    # _read = readInfo(PATH("../Log/info.pickle"))
    writeExcel()
