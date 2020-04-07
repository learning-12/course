# author:lyr time:2019-10-20外部程序的调用
import os
import subprocess
# os.system('ipconfig')#直接调用第三方，阻塞式
sc=subprocess.check_output('ipconfig')#调用第三方，需要一个返回值接收，阻塞式
# print(sc.decode('gbk'))#因为返回值不是返回cmd窗口gbk格式的所以用decode设置编码格式才能打印出来

#Popen--程序启动，到达这个的时候会新开一个进程所以，以前的执行完了新开辟的在执行
#可以联合多线程理解
subprocess.Popen('ipconfig')#非阻塞式调用加个wait（）方法就变成阻塞式的
# subprocess.Popen('ipconfig').wait()
print('after')
print('after11')