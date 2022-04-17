# -*- coding: utf-8 -*-

from TestCase.BasicPro import BasicProTest
import os
import time
from BeautifulReport import BeautifulReport
from Base.HTMLTestRunner_cn import HTMLTestRunner
from TestCase.InfoBase import InfoBaseTest
from TestCase.InfoBase1 import InfoBaseTest1
from TestCase.InfoBase2 import InfoBaseTest2
from TestCase.InfoBase3 import InfoBaseTest3
from TestCase.InfoBase4 import InfoBaseTest4
from TestCase.AddComponent import AddComponent
from TestCase.EditComponent import EditComponent
from TestCase.test1 import test1
from TestCase.Verify import Verify
from datetime import datetime
from Base.BaseStatistics import countDate, writeExcel
from Base.BaseInit import mk_file
import unittest
from TestCase.LoginTest import LoginTest
from Base.BaseRunner import ParametrizedTestCase
import sys
sys.path.append('..')

def PATH(p): return os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def runnerCaseApp():
    start_time = datetime.now()
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(LoginTest))
    # suite.addTest(ParametrizedTestCase.parametrize(InfoBaseTest))
    # suite.addTest(ParametrizedTestCase.parametrize(InfoBaseTest1))
    # suite.addTest(ParametrizedTestCase.parametrize(InfoBaseTest2))
    # suite.addTest(ParametrizedTestCase.parametrize(InfoBaseTest3))
    # suite.addTest(ParametrizedTestCase.parametrize(InfoBaseTest4))
    # suite.addTest(ParametrizedTestCase.parametrize(test1))
    # suite.addTest(ParametrizedTestCase.parametrize(Verify))
    # suite.addTest(ParametrizedTestCase.parametrize(BasicProTest))
    # suite.addTest(ParametrizedTestCase.parametrize(AddComponent))
    # suite.addTest(ParametrizedTestCase.parametrize(EditComponent))

    unittest.TextTestRunner(verbosity=2).run(suite)
    end_time = datetime.now()
    countDate(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
              str((end_time - start_time).seconds) + "秒")
    # now = time.strftime("%Y-%m-%d %H_%M_%S")
    # path = PATH("../Report/")
    # if not os.path.exists(path):
    #     os.makedirs(path)
    # else:
    #     pass
    # # 将运行结果保存到report，名字为定义的路径和文件名，运行脚本
    # report_path = path + '/' + now + "_report.html"
    # reportTitle = '测试报告'
    # desc = u'测试报告详情'
    # fp = open(report_path, 'wb')
    # runner = HTMLTestRunner(stream=fp, title=reportTitle, description=desc)
    # runner.run(suite)
    # fp.close()
    # currentTime = time.strftime('%Y-%m-%d %H_%M_%S')
    # desc = u'测试报告详情'
    # result = BeautifulReport(suite)
    # reportPath = PATH("../Report/")
    # result.report(filename=currentTime + "_report.html", report_dir = reportPath,
    #               description=desc)


if __name__ == '__main__':
    mk_file()
    runnerCaseApp()
    writeExcel()
