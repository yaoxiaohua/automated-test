# -*- coding: utf-8 -*-

from Base.BaseRunner import ParametrizedTestCase
import os
import sys
from PageObject.BasicPro.BasicPro import BasicPro

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class BasicProTest(ParametrizedTestCase):
    def testAspNet(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../Yamls/BasicPro/BasicPro.yaml"),
               "caseName": sys._getframe().f_code.co_name}

        page = BasicPro(app)
        page.operate()
        page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(BasicProTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(BasicProTest, cls).tearDownClass()
