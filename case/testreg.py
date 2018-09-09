# encoding: utf-8
#author: hanzilong
from appium import webdriver
# import sys
# sys.path.append("..")
import unittest,ddt,os,time
from config import data,make_dis,app_pack,dingwei,img
from untils.getdata import huoqu_test
from untils.memory import caijicpu,getnencun,write_recording
from untils.log import Log
from untils.elemen import elemens
from untils.yamls import open_da

# testcasedata=data()
# data_test=huoqu_test(testcasedata,index=1)     #用列数据集合
# @ddt.ddt
class Regpuliblisdt(unittest.TestCase):
    u"""搜索功能"""
    @classmethod
    def setUpClass(self):
        self.dis_app = make_dis()   #初始配置
        self.img=img()              #截图目录赋值
        self.deriver = webdriver.Remote('http://localhost:4723/wd/hub', self.dis_app)
        time.sleep(15)
        Log('reg测试用例开始执行')
    # @ddt.data(*data_test)        #数据循环运行
    def test_reg(self):
        # self.deriver.find_element_by_id("com.ss.android.ugc.aweme:id/b3z").click()
        elemens(deriver=self.deriver,i=0).click()      #测试步骤1
        cpu=caijicpu(app_pack())              #CPU占用情况
        neicun=getnencun(app_pack())          #内存占有情况
        write_recording(cpu=cpu,neicun=neicun)    #写入操作
        # self.assertEqual('0','0',msg='断言错误')    #断言--通过读取成功来判断成功否
        # self.deriver.get_screenshot_as_file(self.img())    #错误截图
    @classmethod
    def tearDownClass(self):
        Log('测试用例执行完毕，测试环境正在还原！')
        time.sleep(5)
        self.deriver.quit()

# if __name__ == '__main__':
#     unittest.main()