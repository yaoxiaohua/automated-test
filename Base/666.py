'''
你好，我叫吕振华,16年大专毕业，后来自己去考了本科，web和app测试都做过，上个项目做的是web端的，元器件综合管理系统，主要是用来
对一些飞机元器件的管理，和可以被国产化替代器件库建立，统计等。
我们项目组只有我一个测试，所以基本的测试工作都是我在负责，项目紧忙不过来的时候会调其他部门的测试来协助下，这个项目主要就是
一些常态化的功能/性能测试，功能就是一些手工测试加上ui自动化环境搭建和维护，还有接口自动化平台的搭建。

'''



# coding:utf-8
# import pymysql
#
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

def getRandomSet(bits):
    num_set = [chr(i) for i in range(48,58)]
    char_set = [chr(i) for i in range(97,123)]
    total_set = num_set + char_set

    value_set = "".join(random.sample(total_set, bits))

    return value_set

if __name__ == '__main__' :
    strings = getRandomSet(8)
    print(strings)



# # !/usr/bin/python3
#
# import pymysql
#
# # 打开数据库连接
#
# conn = pymysql.connect(host='10.3.2.13', user='biaozw1',password='biaozw1',database='ht301_avic',charset='utf8')
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = conn.cursor()
#
# # 使用 execute()  方法执行 SQL 查询
# a = 43949
# p =43949
# # s = []
# # for a in range(1):
# #     sql = "SELECT a.cat_name,b.cat_name,c.cat_name from pd_category a left join pd_category b on b.parent_id=a.type_id left join pd_category c on c.parent_id=b.type_id where a.type_id is not null and a.parent_id != 0 and b.cat_name is not null and c.cat_name is not null;"
# #     cursor.execute(sql)
# #     conn.commit()
# #     q = cursor.fetchall()
# #     s.append(q)
#
# while a <= 150000:
#     sql = r"INSERT INTO `ht301_avic`.`pd_product_avic`(`pro_id`, `unique_id`, `eq_id`, `equip_research_unit`, `cat_id`, `supplier_name`, `supplier_id`, `pro_no`, `pro_name`, `pro_model`, `quality_level`, `equip_count`, `pro_count`, `tech_index_desc`, `country_id`, `is_special_high`, `ext_dependence_level`, `solution_analysis_level`, `rep_quality_level`, `rep_supplier_name`, `rep_supplier_id`, `file_indentify`, `submit_unit`, `reported_status`, `package_type`, `standard_all`, `standard_detail_name`, `maturity`, `choose_level`, `is_product_manufacturer`, `is_encapsulate_domestic_pro`, `supplier_contact_way`, `remark`, `application_environment`, `version`, `pro_type`, `status`, `create_by`, `update_by`, `create_time`, `update_time`, `rep_model`, `rep_suggestion`, `substituted_manufacturer`, `rep_models2`, `rep_suggestion2`, `substituted_manufacturer2`, `rep_models3`, `rep_suggestion3`, `substituted_manufacturer3`, `if_selection`, `if_match`, `reliability_level`, `eq_pro_count`, `manufacturer_contact`, `file_name`, `rep_supplier_level`, `model_name`, `system_name`, `subsystem_name`, `device_name`, `device_model`, `substitute_specification`, `solution_channel`, `alternative_progress`, `reserve_progress`, `is_increment`) VALUES (%s, NULL, 112, '188所', 347, 'A厂', NULL, NULL, 'N 沟道场效应晶体管', 'RE1/6-4k99-W-C3', 'JY', 5.000, 2.000, '工作温度范围 最小值:-55.0℃,最大值:150.0℃,典型值:25.0℃;电源电流 最小值:20.0A,最大值:100.0A,典型值:55.0A;输出阻抗 最小值:5.0Ω,最大值:25.0Ω,典型值:20.0Ω;', 79, 0, 1, 1, 'I', '可替代产品厂家003', NULL, '120所-型机', '120所', 1, 'TO-18', 'GJB360', 'GJB125', 1, 0, 1, 0, '陈秀琴电话15395327207', '备注003', '应用环境003', '1', '2', 1, 'admin', 'admin', '2020-12-16 18:01:39', '2020-12-16 18:01:39', NULL, NULL, NULL, NULL, NULL, 'null', NULL, NULL, 'null', 1, NULL, 'A2', 1.000, NULL, '120所-型机', '3', 'X18T型机', '发动机系统', '左翼发动机', '高度控制器', 'XXXDDD1', '可替代产品规格003', '测试hello', '1', '1', NULL);"%p
#     sql2 = r"INSERT INTO `ht301_avic`.`pd_product_avic_wendor`(`pro_id`, `unique_id`, `eq_id`, `equip_research_unit`, `cat_id`, `supplier_name`, `supplier_id`, `pro_no`, `pro_name`, `pro_model`, `quality_level`, `equip_count`, `pro_count`, `tech_index_desc`, `country_id`, `is_special_high`, `ext_dependence_level`, `solution_analysis_level`, `rep_quality_level`, `rep_supplier_name`, `rep_supplier_id`, `file_indentify`, `submit_unit`, `reported_status`, `package_type`, `standard_all`, `standard_detail_name`, `maturity`, `choose_level`, `is_product_manufacturer`, `is_encapsulate_domestic_pro`, `supplier_contact_way`, `remark`, `application_environment`, `version`, `pro_type`, `status`, `create_by`, `update_by`, `create_time`, `update_time`, `rep_model`, `rep_suggestion`, `substituted_manufacturer`, `rep_models2`, `rep_suggestion2`, `substituted_manufacturer2`, `rep_models3`, `rep_suggestion3`, `substituted_manufacturer3`, `if_selection`, `if_match`, `reliability_level`, `eq_pro_count`, `manufacturer_contact`, `file_name`, `rep_supplier_level`, `model_name`, `system_name`, `subsystem_name`, `device_name`, `device_model`, `substitute_specification`, `solution_channel`, `alternative_progress`, `reserve_progress`) VALUES (%s, '', NULL, NULL, 156, '厂家名称*', NULL, NULL, '全数据', '进口数据--主机所006', 'JP', NULL, NULL, '工作温度范围 最小值:全数据℃, 最大值:全数据℃, 典型值:全数据℃;输入电压范围 最小值:全数据全数据, 最大值:全数据全数据, 典型值:全数据全数据;全数据', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, '全数据', '全数据', '全数据', 1, NULL, 1, 1, '陈秀琴电话15395327207', NULL, NULL, NULL, '1', 1, 'admin', 'admin', '2020-12-03 17:10:34', '2020-12-03 17:10:34', '替代型号1', '1', '可替代产品厂家1', '替代型号2', '2', '可替代产品厂家2', '替代型号3', '3', '可替代产品厂家3', 1, '全数据', '全数据', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);"%p
#     cursor.execute(sql)
#     cursor.execute(sql2)
#     conn.commit()
#     print(a)
#     a += 1
#     p += 1
# # 关闭数据库连接
# conn.close()

#
# import requests
#
# s = requests.session()
#
# url = 'http://component_avic.huazhi365.com/component/pdinfomanagement/save'
#
# header = {
#     'Host': 'component_avic.huazhi365.com',
#     'Proxy-Connection': 'keep-alive,
#     'Content-Length': '223',
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'X-Requested-With': XMLHttpRequest
#     'User-Agent': Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36
#     'Content-Type': application/x-www-form-urlencoded; charset=UTF-8
#     'Origin': http://component_avic.huazhi365.com
#     'Referer': http://component_avic.huazhi365.com/component/pdinfomanagement/add
#     'Accept-Encoding': gzip, deflate
#     'Accept-Language': zh-CN,zh;q=0.9
#     'Cookie': remember=false; JSESSIONID=3288b481-c423-46c3-b1e0-a8dfbfb05246
#
# }
#
# s.post()