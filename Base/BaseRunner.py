# -*- coding: utf-8 -*-

from Base.BaseLog import myLog
import unittest
from selenium import webdriver
import os
from Base.BaseYaml import getYam

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def get_driver():
    chromedriver = PATH("../exe/chromedriver.exe")
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.maximize_window()  # 将浏览器最大化
    openurl = getYam(PATH("../Yamls/config.yaml"))[1]["url"]
    driver.get(openurl)
    driver.implicitly_wait(10)
    return driver


class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should  
        inherit from this class.  
    """

    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.param = param

    @classmethod
    def setUpClass(cls):
        pass
        cls.driver = get_driver()
        cls.logTest = myLog().getLog("chrome")  # 每个设备实例化一个日志记录器

    def setUp(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        pass

    def tearDown(self):
        pass

    @staticmethod
    def parametrize(testcase_klass, defName=None, param=None):  #参数化方法
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'
        """
        testLoader = unittest.TestLoader()
        testNames = testLoader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        if defName != None:
            for name in testNames:
                if name == defName:
                    suite.addTest(testcase_klass(name, param=param))
        else:
            for name in testNames:
                suite.addTest(testcase_klass(name, param=param))
        return suite