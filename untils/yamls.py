# encoding: utf-8
#author: hanzilong
import yaml
from untils.log import Log
from untils.py_app import deriver_fengzhuang as feng

Log('解析yaml文件')
def open_da(path):
    try:
        file = open(r'%s'%path,'r',encoding='utf-8')
        data = yaml.load(file)
        return {'code':0,'data':data} 
    except Exception as e:
        Log('yaml文档解析失败！原因：%s'%e)
        return {'code':1,'data':e}
