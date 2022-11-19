使用说明：

介绍
* unittest参数化
* PageObject分层管理
* 用例编写基于yaml配置
* 支持失败重连
* 自动生成excel、html测试报告

结构：
-  Base：  管理常用方法
-  PageObject：  处理页面逻辑
-  TestCase：  测试用例调用，调用Page层，传入yaml用例
-  yamls： 测试用例编写层，基于关键字驱动，主要包含
    - testinfo：用例介绍
    - testcase：用例操作步骤，用例操作步骤
    - check.：检查点
-  Runner 执行入口
-  Log： 日志，含截图
-  Report： 测试报告


## yaml用例编写说明
用例分为三部分

- ```testinfo``` 表示用例介绍
    - ```id``` 用例id
    - ```title``` 用例标题
    - ```info``` 前置条件

- ```testcase``` 用例的执行步骤
    - ```element_info: com.huawei.works.contact:id/title``` 元素
    -  ```find_type: id```  元素类型
        - ```id```
        - ```xpath```
        - ```css```
        - ```ids``` 需要增加```index```
        - ```index``` 和```ids```配合
    - ```operate_type: click``` 操作
        - ```click```
        - ```swipe_down```
        - ```swipe_up```
        - ```get_value```
        - ```set_value```
        - ```msg``` 传给```set_value```关键字
        - ```adb_tap``` 使用adb中的tap命令点击元素,元素必须可识别，应用于悬浮层场景
        -  ```get_content_desc``` 无法切换到webview时，用此关键字
        - ```其他关键字``` 用于定制一些特殊业务
    - ```is_time: 3``` 自定义暂停3秒

- ```check``` 检查点,支持多检查点
  - ```element_info:
  - ```find_type: ids```
  - ```index: 0```

举例：
testinfo:
    - id: test007
      title: 基础产品信息库管理
      info: 应用验证信息管理-元器件

testcase:
    - element_info: //*[@id="side-menu"]/li[4]/a/span[1]
      find_type: xpath
      operate_type: click
      info: 点击基础产品信息库管理
      is_time: 1
    - element_info: //*[@id="side-menu"]/li[4]/ul/li[1]/a
      find_type: xpath
      operate_type: click
      info: 点击元器件
      is_time: 1
    - element_info: //iframe[contains(@src,'/component/product')]
      find_type: xpath
      operate_type: switch_frame
      info: 切换frame
      is_time: 1
    - element_info: //*[@class="btn btn-outline btn-default"][1]
      find_type: xpath
      operate_type: click
      info: 点击新增
      is_time: 1
    - element_info: "0"
      find_type:
      operate_type: switch_default_frame
      info: 切换默认frame
      is_time: 1
    - element_info: //iframe[contains(@src,'/component/product/add')]
      find_type: xpath
      operate_type: switch_frame
      info: 切换frame
      is_time: 1
    - element_info: proNo
      find_type: id
      operate_type: send_keys_and_random
      msg:  元器件物资编码
      info: 填写物资编码
    - element_info: proNo
      find_type: id
      operate_type: write_data
      info: 获取信息
      is_time: 2
check:
    - element_info: //button[contains(text(),'保存')]
      find_type: xpath
      check: default_check
      info: 验证存在保存按钮
    - element_info: //button[contains(text(),'提交')]
      find_type: xpath
      check: contrary
      info: 验证不存在提交按钮

## 比较麻烦case处理
- 当遇到有些用例比较麻烦，需要单独写page层
- 自定义page层


