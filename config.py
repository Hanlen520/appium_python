# encoding: utf-8
#author: hanzilong
#配置app以及测试设备的相关信息
import time,os
 #包名
def app_pack():                       
    app_packs='com.ss.android.ugc.aweme'
    return app_packs
 #Appium配置
def make_dis():                   
    dis_app={}
    dis_app['platformName'] = 'Android'
    dis_app['platformVersion'] = '5.1.1'
    dis_app['deviceName'] =  '127.0.0.1:62001'
    dis_app['appPackage'] = 'com.ss.android.ugc.aweme'
    dis_app['appActivity'] ='com.ss.android.ugc.aweme.splash.SplashActivity'
    dis_app['androidDeviceReadyTimeout'] =30
    dis_app['unicodeKeyboard'] ='True'
    dis_app['resetKeyboard'] ='True'
    dis_app['noReset']='True'
    return  dis_app
#用例截图目录
def img():
    now = time.strftime('%Y-%m-%d %Hh_%Mm', time.localtime(time.time()))
    path2=r"F:\\selenium框架\\img\\"+now+".png"
    return path2
# 测试定位地址
def dingwei():
    # path=os.getcwd()
    path_yongli="F:\\python_appium框架\\data\\dingwei\\reg.yaml"
    return path_yongli
#执行测试用例目录
def casepy():
    case_path="F:\\python_appium框架\\case"
    return case_path
#测试用例数据目录
def data():
    testcasedata="F:\\python_appium框架\\data\\testcase_data.xlsx"
    return  testcasedata
#发送测试报告到邮箱
def dir(): 
    dirs ="F:\\selenium框架\\reports"  # 指定报告目录
    return dirs
#邮箱附件地址
#xlsx测试数据附件
def xlsx_case():
    attach_xlsx="F:\\python_appium框架\\data\\testcase_data.xlsx"
    return attach_xlsx
#log地址
def logs():
    File_log = "F:\\python_appium框架\\log\\appium.log"  # log记录目录
    return  File_log




