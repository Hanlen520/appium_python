# encoding: utf-8
# author: hanzilong
'''主运行文件'''
from untils.HTMLTestReportCN import HTMLTestRunner
import os,unittest,time
from untils.log  import Log 
from config import casepy
# import untils.emails

#运行测试脚本，生成Html测试报告
Log('UI自动化相关测试开始执行')
test_suit = unittest.TestSuite()
discover = unittest.defaultTestLoader.discover(casepy(), pattern='test*.py', top_level_dir=None)   #运行整目录文件
for test in discover:
	for test_case in test:
		test_suit.addTest(test_case)
now=time.strftime('%Y-%m-%d %Hh_%Mm',time.localtime(time.time()))
filename = os.getcwd() + "\\reports\\" + now + "_report.html"
re_open= open(filename,'wb')
runer = HTMLTestRunner(
		stream=re_open,
		title=u'APP自动化测试报告',
		description=u'自动化用例执行情况：',
		tester=u'hanzilong',
		verbosity = 2 )
runer.run(test_suit)
re_open.close()
Log('UI自动化相关测试执行完毕！') 



#  邮件发送配置