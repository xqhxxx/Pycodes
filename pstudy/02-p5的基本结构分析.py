# 1导包
from PyQt5.Qt import *
import sys
# 2
#可传参
agrs = sys.argv

# print(agrs)
# if agrs[1]=='1':
#     print("aaa")
# else:
#     print("ooo")

# 1--创建一个应用程序对象
app=QApplication(sys.argv)
#
# 2创建控件 设置控件 展示控件
# window=QWidget()
window=QPushButton("按钮")
window.show()

# 3--r让整个程序进入消息循环 不退出
# 监测整个程序与用户的交换信息
app.exec_()

# 退出码 0为正常
sys.exit()