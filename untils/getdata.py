# encoding: utf-8
#author: hanzilong
'''从Excel获取测试用例相关数据'''
import xlrd
from untils.log import Log
Log('获取测试用例所需要的参数')
def huoqu_test(filepath,index):
    # filepath="F:\\python_appium框架\\data\\testcase_data.xlsx"
    # index="0"
    try:
        file = xlrd.open_workbook(filepath)
        me = file.sheets()[index]
        nrows = me.nrows
        listdata = []
        for i in range(1, nrows):
            dict_canshu = {}
            dict_canshu['id']=me.cell(i, 0).value
            dict_canshu['logout']=(me.cell(i,2).value)
            dict_canshu.update(eval(me.cell(i,3).value))
            dict_canshu.update(eval(me.cell(i,4).value))
            listdata.append(dict_canshu)
        return listdata
  
    except Exception as e:
        Log('获取测试用例参数失败！失败原因：%s'%e)
