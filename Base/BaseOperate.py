# -*- coding: utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import selenium.common.exceptions
from Base.BaseElementEnmu import Element as be
from Base.BaseStatistics import write_append
from Base.BaseStatistics import read_append
from selenium.webdriver.common.action_chains import *
import time
import datetime
import re
import random
import string

'''
# 此脚本主要用于查找元素是否存在，操作页面元素
'''


class OperateElement:
    def __init__(self, driver=""):
        self.driver = driver

    def findElement(self, operate):
        '''
        查找元素.operate,dict|list
        operate_type：对应的操作
        element_info：元素详情
        find_type: find类型
        '''
        try:
            t = operate["check_time"] if operate.get("check_time",
                                                     "0") != "0" else be.WAIT_TIME  # 如果自定义检测时间为空，就用默认的检测等待时间
            if type(operate) == list:  # 多检查点
                for item in operate:
                    t = item["check_time"] if item.get("check_time", "0") != "0" else be.WAIT_TIME
                    WebDriverWait(self.driver, t).until(lambda x: self.elements_by(item))
                return {"result": True}
            if type(operate) == dict:  # 单检查点
                if operate.get("element_info", "0") == "0":  # 如果没有页面元素，就不检测是页面元素，可能是滑动等操作
                    return {"result": True}
                WebDriverWait(self.driver, t).until(lambda x: self.elements_by(operate))  # 操作元素是否存在
                return {"result": True}
        except selenium.common.exceptions.TimeoutException:
            # print("==查找元素超时==")
            return {"result": False, "type": be.TIME_OUT}
        except selenium.common.exceptions.NoSuchElementException:
            # print("==查找元素不存在==")
            return {"result": False, "type": be.NO_SUCH}
        except selenium.common.exceptions.WebDriverException:
            # print("WebDriver出现问题了")
            return {"result": False, "type": be.WEB_DROVER_EXCEPTION}

    '''
    查找元素.mOperate是字典:operate_type,element_info,find_type:
    testInfo: 用例介绍
    logTest: 记录日志
    '''

    def operate(self, operate, testInfo, logTest):
        res = self.findElement(operate)
        if res["result"]:
            return self.operate_by(operate, testInfo, logTest)
        else:
            return res

    def operate_by(self, operate, testInfo, logTest):
        try:
            info = "%s_%s_%s_%s" % (
                operate.get("element_info", " "), operate.get("find_type"), operate.get("operate_type", " "),
                operate.get("msg", " "))
            print("==操作步骤：%s==" % info)
            logTest.buildStartLine(testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + info)  # 记录日志

            if operate.get("operate_type", "0") == "0":  # 如果没有此字段，说明没有相应操作，一般是检查点，直接判定为成功
                return {"result": True}
            elements = {
                be.CLICK: lambda: self.click(operate),
                be.GET_VALUE: lambda: self.get_value(operate),
                be.GET_TEXT: lambda: self.get_text(operate),
                be.SEND_KEYS: lambda: self.send_keys(operate),
                be.MOVE_TO_ELEMENT: lambda: self.move_to_element(operate),
                be.SWITCH_FRAME: lambda: self.switch_frame(operate),
                be.SWITCH_TO_ELE: lambda: self.switch_to_ele(operate),
                be.SEND_KEYS_AND_RANDOM: lambda: self.send_keys_and_random(operate),
                be.RANDOM_PHONE: lambda: self.random_Phone(operate),
                be.WRITE_DATA: lambda: self.write_data(operate)
            }
            return elements[operate.get("operate_type")]()
        except IndexError:
            logTest.buildStartLine(
                testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + operate["element_info"] + "索引错误")  # 记录日志
            # print(operate["element_info"] + "索引错误")
            return {"result": False, "type": be.INDEX_ERROR}

        except selenium.common.exceptions.NoSuchElementException:
            logTest.buildStartLine(
                testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + operate[
                    "element_info"] + "页面元素不存在或没加载完成")  # 记录日志
            # print(operate["element_info"] + "页面元素不存在或没有加载完成")
            return {"result": False, "type": be.NO_SUCH}
        except selenium.common.exceptions.StaleElementReferenceException:
            logTest.buildStartLine(
                testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + operate[
                    "element_info"] + "页面元素已经变化")  # 记录日志
            # print(operate["element_info"] + "页面元素已经变化")
            return {"result": False, "type": be.STALE_ELEMENT_REFERENCE_EXCEPTION}
        except KeyError:
            # 如果key不存在，一般都是在自定义的page页面去处理了，这里直接返回为真
            return {"result": True}

    # 点击事件
    def click(self, operate):
        # print(self.driver.page_source)
        if operate["find_type"] == be.find_element_by_id or operate["find_type"] == be.find_element_by_xpath \
                or be.find_element_by_css_selector or operate["find_type"] == be.find_element_by_class_name or \
                        operate["find_type"] == be.find_element_by_link_text:
            self.elements_by(operate).click()
        elif operate.get("find_type") == be.find_elements_by_id:
            self.elements_by(operate)[operate["index"]].click()
        return {"result": True}

    def send_keys(self, operate):
        """
        :param operate:
        :return:
        """
        time.sleep(0.5)
        self.elements_by(operate).send_keys(operate["msg"])
        return {"result": True}

    def send_keys_and_random(self, operate):
        """
        :param operate:
        :return:
        """
        time.sleep(0.5)
        # 生成随机数
        # 组合数字与字母的序列
        # s = string.digits + string.ascii_letters
        s = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        # 随机取出6个字母和数字的组合并合并成字符串
        # zfill函数:在字符前补零，比如你想把某个字符a=‘1’设置成4位，那么你就可以使用a.zfill(4),那么结果就会是’0001’
        random_data = ''.join(s)
        # random_data = ''.join(random.sample(s, 6))
        self.elements_by(operate).send_keys(operate["msg"] + random_data)
        return {"result": True}

    def random_Phone(self, operate):
        time.sleep(0.5)
        headList = ["30", "31", "32", "33", "34", "35", "36", "37", "38", "39",
                    "47", "50", "51", "52", "53", "55", "56", "57", "58", "59",
                    "86", "87", "88", "89"]
        num = random.choice(headList) + "".join(random.choice("0123456789") for i in range(8))
        print(num)
        self.elements_by(operate).send_keys(str(operate["msg"]) + num)
        # str[-3:])
        return {"result": True}

    def get_text(self, operate):
        '''
        :param operate:
        :return: {}
        '''

        if operate.get("find_type") == be.find_elements_by_id:
            element_info = self.elements_by(operate)[operate["index"]]

            result = element_info.get_attribute("text")
            re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)  # 只匹配中文，大小写，字母
            return {"result": True, "text": "".join(re_reulst)}

        element_info = self.elements_by(operate)
        result = element_info.get_attribute("text")

        re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)
        return {"result": True, "text": "".join(re_reulst)}

    def get_value(self, operate):
        if operate.get("find_type") == be.find_elements_by_id:
            element_info = self.elements_by(operate)[operate["index"]]

            result = element_info.get_attribute("value")
            re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)  # 只匹配中文，大小写，字母
            return {"result": True, "text": "".join(re_reulst)}

        element_info = self.elements_by(operate)
        result = element_info.get_attribute("value")

        re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)
        return {"result": True, "text": "".join(re_reulst)}
    '''
    鼠标悬停
    '''
    def move_to_element(self, operate):
        ActionChains(self.driver).move_to_element(self.elements_by(operate)).perform()
        return {"result": True}

    def switch_frame(self, operate):
        if operate["find_type"] == be.find_element_by_id or operate["find_type"] == be.find_element_by_xpath \
                or be.find_element_by_css_selector or operate["find_type"] == be.find_element_by_class_name or \
                        operate["find_type"] == be.find_element_by_link_text:
            iframe = self.elements_by(operate)
            self.driver.switch_to.frame(iframe)
        elif operate.get("find_type") == be.find_elements_by_id:
            iframe1 = self.elements_by(operate)
            self.driver.switch_to.frame(iframe1)
        return {"result": True}
        print("--切换iframe---")

    def switch_to_ele(self, operate):
        if operate["find_type"] == be.find_element_by_id or operate["find_type"] == be.find_element_by_xpath \
                or be.find_element_by_css_selector or operate["find_type"] == be.find_element_by_class_name or \
                        operate["find_type"] == be.find_element_by_link_text:
            ele = self.elements_by(operate)
            get_js = "arguments[0].scrollIntoView()"   # js脚本
            self.driver.execute_script(get_js, ele)
        elif operate.get("find_type") == be.find_elements_by_id:
            ele1 = self.elements_by(operate)
            get_js = "arguments[0].scrollIntoView()"   # js脚本
            self.driver.execute_script(get_js, ele1)
        return {"result": True}
        print("--切换iframe2---")


    def write_data(self, operate):
        if operate["find_type"] == be.find_element_by_id or operate["find_type"] == be.find_element_by_xpath \
                or be.find_element_by_css_selector or operate["find_type"] == be.find_element_by_class_name or \
                        operate["find_type"] == be.find_element_by_link_text:
            ele = self.elements_by(operate)
            # data = ele.get_attribute("textContent")
            data = ele.get_attribute('value')
            write_append(data)
        elif operate.get("find_type") == be.find_elements_by_id:
            ele = self.elements_by(operate)
            # data = ele.get_attribute("textContent")
            data = ele.get_attribute('value')
            write_append(data)
        return {"result": True}
        print("--写入excel最后一行---")


    # 封装常用的标签
    def elements_by(self, operate):
        elements = {
            be.find_element_by_id: lambda: self.driver.find_element_by_id(operate["element_info"]),
            be.find_element_by_xpath: lambda: self.driver.find_element_by_xpath(operate["element_info"]),
            be.find_element_by_class_name: lambda: self.driver.find_element_by_class_name(operate['element_info']),
            be.find_elements_by_id: lambda: self.driver.find_elements_by_id(operate['element_info']),
            be.find_element_by_css_selector: lambda: self.driver.find_element_by_css_selector(operate['element_info']),
            be.find_element_by_link_text: lambda: self.driver.find_element_by_link_text(operate['element_info'])

        }
        return elements[operate["find_type"]]()
