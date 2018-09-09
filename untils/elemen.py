from untils.py_app import deriver_fengzhuang as feng
from untils.yamls import open_da
from config import dingwei
# path=dingwei()
# data=open_da(path=path)['data']  
def elemens(deriver,i):
    # data=open_da(path)
    path=dingwei()
    data=open_da(path=path)['data']  
    case_der=feng(deriver)
    f=case_der.find_elemens(lujing=data[i]['element_info'],fangfa=data[i]['find_type'])
    return f

