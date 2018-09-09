# encoding: utf-8
#author: hanzilong
'''
获取配置相关手机性能的数据
'''
from untils.log import Log
import platform,os,time
Log('采集cpu信息')
def caijicpu(packagename):#这里采集的cpu时候可以是执行操作采集 就是-n  -d  刷新间隔
	cpu='adb shell top -n 1| findstr %s'%(packagename)
	re_cpu=os.popen(cpu).read().split()[2]
	return re_cpu
Log('获取使用的物理内存信息')
def getnencun(packagename):#Total 的实际使用过物理内存
	cpu = 'adb shell top -n 1| findstr %s' % (packagename)
	re_cpu=os.popen(cpu).read().split()[6]
	re_cpu_m=str(round(int(re_cpu[:-1])/1024))+'M'
	return re_cpu_m

'''采集的性能测试数据存放在txt文档中'''
path=os.getcwd()
now = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
recording=path+'\\reports\\%s.txt'%now
Log('记录当前的cpu占有率，内存')
def write_recording(cpu,neicun):
    try:
        with open(recording,'a',encoding='utf-8') as f:
            m='cpu:%s,内存：%s'%(cpu,neicun)
            f.write(m+'\n')
            f.close()
    except Exception as e:
        Log('写入性能数据失败！失败原因：%s'%e)


# if __name__ == '__main__':
#     print(caijicpu("com.ss.android.ugc.aweme"))
#     print(getnencun('com.ss.android.ugc.aweme'))
#     write_recording(caijicpu("com.ss.android.ugc.aweme"),getnencun('com.ss.android.ugc.aweme'))