from openpyxl import load_workbook,Workbook

'''
保存工作簿
'''
wb = Workbook() # 新建工作簿,示例化对象,wb是刚刚创建的新的工作簿

wb.save(r"xlsx办公自动化\XLSX文件夹\我的工作簿") # 保存文件,默认存在一个工作表
# 保存时如果有其他的程序在使用这个表格就会报错,需要先解除占用
87
'''
读取保存的工作表
'''
wb = load_workbook(r"xlsx办公自动化\XLSX文件夹\我的工作簿")
# read_only=False/True  False表示可读,True表示只能读,不能写
# guess_types=False/True  False表示转换数据,True表示不能转换数据
# data_only=False/True   False表示序单元格的真实信息,True表示只读取值



































