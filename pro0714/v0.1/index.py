from datetime import datetime
import os
import time
import xlwt
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog

# 3步骤3
# UI--逻辑分离  不用转成文件
from PyQt5.uic import loadUiType

from tools import sqlTools

ui, _ = loadUiType("ui/main.ui")


class MainApp(QMainWindow, ui):
    # pass
    # 定义构造方法
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        # 默认显示登录 隐藏主界面
        self.handle_ui_init()

        #
        self.handle_menus()


    # todo UI的初始化
    def handle_ui_init(self):
        # self.show_themes(self.login_widget)
        # self.hide_themes(self.main_widget)
        # self.hide_themes(self.data_widget)
        self.stackedWidget.setCurrentIndex(0)
        self.hide_themes(self.menu_Bar)

        # 动态显示时间在label上
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()

    # 显示时间
    def showtime(self):
        datetime = QDateTime.currentDateTime()
        text = datetime.toString()
        self.label_time.setText(text)

    # todo 界面切换
    def handle_menus(self):
        # pass
        # todo 1 登录
        self.login_Button.clicked.connect(self.on_login)
        # todo 2 监测主界面
        # 2.1 回到监测界面
        self.action_jc.triggered.connect(self.monitor_management)

        # todo 3 数据管理
        self.action_data.triggered.connect(self.data_management)

    # 监测界面
    def monitor_management(self):
        # self.hide_themes(self.data_widget)
        # self.show_themes(self.main_widget)
        self.stackedWidget.setCurrentIndex(1)

        # 保存数据
        self.save_data_button.clicked.connect(self.save_data)

    # 处理数据 保存
    def save_data(self):
        # 测试数据
        v1 = time.asctime(time.localtime(time.time()))
        print(v1)
        sql = "insert into data_tb(data_name,attribute_01,attribute_02,attribute_03)values" \
              "('xxx监测数据%s','属性一的数据：22','属性2的数据：33','属性3的数据：77')" % v1
        print(sql)
        sqlTools.updateData(self, sql)
        print("save data true" )

    def on_login(self):
        flag = False
        # 登录确认 ok 切换界面
        print(44)
        query_tb_user = '''select * from user_tb;'''
        res = sqlTools.queryData(self, query_tb_user)
        # 数据库查询结果 处理
        for re in res:
            if self.user_input.text() == re[1]:
                if self.pass_input.text() == re[2]:
                    flag = True
        if flag:
            # self.hide_themes(self.login_widget)
            # self.show_themes(self.main_widget)
            self.stackedWidget.setCurrentIndex(1)
            self.show_themes(self.menu_Bar)
        else:
            self.laber_err.setText(str("用户名或密码错误，请重试"))
            self.pass_input.setText('')

    # 数据管理界面
    def data_management(self):
        # self.hide_themes(self.main_widget)
        # self.show_themes(self.data_widget)
        self.stackedWidget.setCurrentIndex(2)

        # 1 数据初始化显示
        res = sqlTools.queryData(self, "select data_name,attribute_01,attribute_02,attribute_03 from data_tb;")
        print(res)

        rowIndex = 0
        for lis in res:
            self.table_data.setRowCount(self.table_data.rowCount() + 1)
            colIndex = 0
            for l in lis:
                self.table_data.setItem(rowIndex, colIndex, QTableWidgetItem(l))
                colIndex += 1
            rowIndex += 1
        #   2  数据导出
        self.export_data_button.clicked.connect(self.export_data)

    #   导出数据
    def export_data(self):
        # 准备数据  文件选择
        today_date = datetime.today().date()
        today_hour = datetime.today().hour
        filename, ok = QFileDialog.getSaveFileName(self, 'save file',
                                                   os.path.abspath(os.path.dirname(__file__)) + '/data_' + str(
                                                       today_date) + '_' + str(today_hour) + '.xls',
                                                   "Excel 97-2003 工作簿(*.xls);;All Files (*)")
        # with open(filename[0], 'w') as f:
        if 'xls' in filename:
            results = sqlTools.queryData(self, "select data_name,attribute_01,attribute_02,attribute_03 from data_tb;")
            print(results)
            workbook = xlwt.Workbook()
            sheet = workbook.add_sheet('Sheet1', cell_overwrite_ok=True)
            # 表头
            table_head = ['名称', 'arr1', 'arr2', 'arr3']
            for field in range(len(table_head)):
                sheet.write(0, field, table_head[field])

            # row = 1
            # col = 0
            for row in range(1, len(results) + 1):
                for col in range(len(results[row - 1])):
                    sheet.write(row, col, '%s' % results[row - 1][col])
            workbook.save(filename)
            print('文件已保存至%s' % filename)


    #  界面显示
    def show_themes(self, _widget):
        _widget.show()

    #  界面隐藏
    def hide_themes(self, _widget):
        _widget.hide()


def main():
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
