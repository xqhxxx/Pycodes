#author_='xqh';
#date: 2021/7/23 9:38
import datetime

import xlwt


def export_data(self):
    # 准备数据  文件选择
    today_date = datetime.today().date()
    today_hour = datetime.today().hour
    filename, ok = QFileDialog.getSaveFileName(self,
                                               'save file', os.path.abspath(os.path.dirname(__file__)) + '/data_' + str(
            today_date) + '_' + str(today_hour) + '.xls',
                                               "Excel 97-2003 工作簿(*.xls);;All Files (*)")
    # with open(filename[0], 'w') as f:
    if 'xls' in filename:
        # results = sqlTools.queryData(self, "select data_name,attribute_01,attribute_02,attribute_03 from data_tb;")
        # print(results)
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('Sheet1', cell_overwrite_ok=True)
        # 表头
        table_head = ['名称', 'arr1', 'arr2', 'arr3']
        for field in range(len(table_head)):
            sheet.write(0, field, table_head[field])

        row = 1
        col = 0
        for row in range(1, len(results) + 1):
            for col in range(len(results[row - 1])):
                sheet.write(row, col, '%s' % results[row - 1][col])
        workbook.save(filename)
        print('文件已保存至%s' % filename)

