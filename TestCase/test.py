import pandas as pd
from xlutils.copy import copy
import xlrd
from Base.BaseElementEnmu import Element
import os
import pandas
import time
import random
import datetime
from Base.BaseStatistics import read_append



PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)



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

def send_keys(self, operate):
    """
    :param operate:
    :return:
    """
    time.sleep(0.5)
    self.elements_by(operate).clear()
    self.elements_by(operate).send_keys(operate["msg"])
    return {"result": True}



read_append('Record')

