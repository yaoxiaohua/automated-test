# -*- coding: utf-8 -*-

class Element(object):

    # selenium关键字
    find_element_by_id = "id"
    find_elements_by_id = "ids"
    INDEX = "index"
    find_elements_by_xpath = "xpaths"
    find_element_by_xpath = "xpath"
    find_element_by_css_selector = "css"
    find_element_by_class_name = "class_name"
    find_element_by_link_text = "link_text"
    CLICK = "click"
    GET_TEXT = "get_text"
    SEND_KEYS = "send_keys"
    GET_VALUE = "get_value"
    WAIT_TIME = 20  # 查找元素等待时间
    MOVE_TO_ELEMENT = "move_to_element" # 鼠标悬停
    DEFAULT_OPERATE= "default_operate" # 默认值
    SWITCH_FRAME= "switch_frame" # 切换frame
    SWITCH_FRAME1= "switch_frame1" # 切换frame1
    SWITCH_FRAME2= "switch_frame2" # 切换frame1
    SWITCH_TO_ELE= "switch_to_ele" # 跳转到元素
    SWITCH_DEFAULT_FRAME= "switch_default_frame"  # 切换默认frame
    SWITCH_PARENT_FRAME= "switch_parent_frame"  # 切换默认frame
    SEND_KEYS_AND_RANDOM= "send_keys_and_random" # 输入带随机数
    RANDOM_PHONE= "random_Phone" # 输入随机手机号
    CLICK_EXCEL_ELE= "click_excel_ele" # 点击excel存储对应元素
    WRITE_DATA= "write_data" # 写excel最后一行
    UPLOAD_FILE = "upload_file" # 上传文件


    # 错误日志
    TIME_OUT = "timeout"
    NO_SUCH = "noSuch"
    WEB_DROVER_EXCEPTION = "WebDriverException"
    INDEX_ERROR = "index_error"
    STALE_ELEMENT_REFERENCE_EXCEPTION = "StaleElementReferenceException"
    DEFAULT_ERROR = "default_error"

    # 检查点
    CONTRARY = "contrary" # 相反检查点，表示如果检查元素存在就说明失败，如删除后，此元素依然存在
    CONTRARY_GETVAL = "contrary_getval" # 检查点关键字contrary_getval: 相反值检查点，如果对比成功，说明失败
    DEFAULT_CHECK = "default_check" # 默认检查点，就是查找页面元素
    COMPARE = "compare" # 历史数据和实际数据对比

    RE_CONNECT = 1  # 是否打开失败后再次运行一次用例

    # 文件名字
    INFO_FILE = "info.pickle"
    SUM_FILE = "sum.pickle"
    DEVICES_FILE = "devices.pickle"
    REPORT_FILE = "Report.xlsx"
    ORDER_FILE = "Order.xls"
