# -*- coding: utf-8 -*-

from Base.BaseRunner import ParametrizedTestCase
import os
import sys
from PageObject.InfoBase.InfoBase import InfoBase
from PageObject.Login.LoginPage import LoginPage
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class InfoBaseTest2(ParametrizedTestCase):
    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../Yamls/Login/Login.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginPage(app)
        page.operate()

    def testBasicJDAdd(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../Yamls/InfoBase/InfoBase2.yaml"),
               "caseName": sys._getframe().f_code.co_name}

        page = InfoBase(app)
        page.operate()
        page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(InfoBaseTest2, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(InfoBaseTest2, cls).tearDownClass()
