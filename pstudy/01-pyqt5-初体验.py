
from PyQt5.Qt import *
import  sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle("我是标题党")
window.resize(500,600)
window.move(1200,400)

label=QLabel(window)
label.setText("你好呀，逗比")
label.move(200,200)

window.show();
sys.exit(app.exec_())