import os
from openpyxl import load_workbook

"""加载excel"""

# # load_workbook(filepath:str) -> Workbook
# wb = load_workbook(r"D:\zzw_keli\Documents\个人文档\班级干部信息表汇总.xlsx")
# ws = wb["Sheet1"]
# ws = [x for x in ws.rows]

# for x in ws[1:]:#.rows: # ws.rows 读取每一行的内容 返回生成器
#     print(x[0].value,x[1].value)


# s_file = r"D:\zzw_keli\Documents\个人文档\班级干部信息表汇总.xlsx"

# wb = load_workbook(s_file)
# ws = wb["Sheet1"]

# print(ws["M18"].value)
# print(ws.cell(row=18,column=15).value) # row = 行  column = 列   等价于  O15

# for row in ws.iter_rows(min_row=1,max_row=5,values_only=True):
#     print(row)

# uses = set() # {班级:[姓名:xxx,职务:xxx,电话号码:xxx]} 数据结构

# for x in range(3,15):
#     for y in range(1,16):
#         values = ws.cell(row=x,column=y).value
#         # if '计科1班' in str(values):
#         #     uses.add()
#         if values is None:
#             continue
#         else:
#             uses.add(values)

# print(uses)

# wb.close()



"""
办公三件套:
Worh:Document(文档)/Paragraphs(段落)/run(文字/最小的元素)
PPT:Presentation(演示)/Slides(演示页)/shapes(元素)
Excel:workbook(工作薄)/worksheets(工作表)/cells(单元)
"""
# 三个库
# import docx
# import openpyxl
# import pptx
"""
场景1:word邀请函
"""
from docx import Document # 创建文档
from docx.oxml.ns import qn # 中文兼容问题
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT # 段落
from docx.shared import Pt,RGBColor,Mm,Cm # 大小磅数/字号    Pt,Mm,Cm是字体大小的单位,RGBColor是字体颜色
# from docx import *

from openpyxl import load_workbook

class 原神七国聚会(object):
    dir = r"D:\zzw_keli\Documents"
    def template1(name,gen):
        # 创建嘉宾模板_男士
        word_document = Document()
                                                # 这里有个全局字体
        word_document.styles['Normal'].font.name = u'微软雅黑' # 正题/标题1/标题2 (英文)
        word_document.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'),u'微软雅黑') # 中文
        
        '''
        一个文档示例化一个对象,一个段落实例化一个对象
        '''
        
        #----段落创建p1----
        p1 = word_document.add_paragraph() # 向word添加段落
        # 对齐                              居中
        p1.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        #----添加文字----  实例化对象添加文字
        run_text_1 = p1.add_run('提瓦特七神聚会')
        #           字体 大小
        run_text_1.font.size = Pt(20)
        
        
        #----段落创建p2----
        p2 = word_document.add_paragraph()
        p2.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        #----添加文字----
        run_text_2 = p2.add_run('邀请行')
        run_text_2.font.size = Pt(36)
        
        
        #----段落创建p customer----
        p_customer =  word_document.add_paragraph()
        p_customer.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
        run_text_c = p_customer.add_run(f'尊敬的{name}{gen}: 谨以此函，诚邀您拨冗莅临「提瓦特七神聚会」')
        run_text_c.font.size = Pt(20)
        
        
        #----创建段落3----
        p3 = word_document.add_paragraph()
        #----添加文子
        run_text_3 = p3.add_run("自天空岛帷幕垂落以来，七国之神久未同席。今逢星辰归位之夜，应天理维系者之召，七位神明将齐聚云海之巅，共叙旧谊、同议提瓦特之未来。您的到来，将为这场盛会再添一段新的传奇。届时，风起地之风神、纳塔之火神、枫丹之水神、稻妻之雷神、须弥之草神、至冬之冰神与璃月之岩神，皆将亲临。宴会之上，烛火与星光交映，七元素共鸣，愿与您共饮一杯。\n盼君赴约。")
        run_text_c.font.size = Pt(16)
        
        
        #----创建段落,添加图片(也是段落)
        p4 = word_document.add_paragraph()
        p4.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER #居中对齐
        
        
        #----添加文字(图片)----
        run_text_4 = p4.add_run()         # 宽度    高度
        run_text_4.add_picture('路径.jpg',width=40,height=40)
        
        file = os.path.join(dir,name)
        with open(file,'w',encoding='utf-8'):
            pass
        word_document.save(file)

'''
设置了局部字体会有先使用,如果没有设置字体就会使用全局字体
'''

'''
                输出行，转成列表，再切片，因为生成器不能切片
for r in list(ws.iter_rows())[1:]:
    row = [data.value for data in r] # 这个推到列表很重要
    
'''

"""工作表获取方法"""
my_elsx = r"D:\zzw_keli\Documents\个人文档\我的账单.xlsx"
import openpyxl

'''获取当前活动的工作表'''
wb = openpyxl.load_workbook(my_elsx)
ws = wb.active # 获取当前活动的工作表
print(ws)

'''以索引值的方式获取工作表'''
# worksheets会返回所有的工作表名的列表,注意这是对象
ws = wb.worksheets[0] # 第一个工作表

'''以工作表名获取工作表'''
ws=wb["Sheet1"] # 没有成员提示

wb.sheetnames # 所有工作表名的列表,注意这不是对象

'''读取并修改工作表名'''
wb.worksheets[0].title = "2026-10"

"""
工作表的新建,复制和删除
"""
'''创建工作表和工作簿'''
wb = openpyxl.Workbook() # 创建工作簿
wb.create_sheet() # 默认工作表名是Sheet,也可以指定位置(第二个参数)
wb.save('demo.xlsx')

'''复制工作表'''
wb1 = openpyxl.load_workbook("demo.xlsx")
wb.copy_worksheet(wb['Sheet1']).title = "Sheet01" # 参数必须是对象

'''删除工作表'''
wb2 = openpyxl.load_workbook("demo.xlsx")
wb2.remove(wb2["Sheet"])
wb2.save("demo.xlsx")


"""
单元格信息获取
"""
wb3 = openpyxl.load_workbook("demo.xlsx")
ws3 = wb3.worksheets[0]
print(ws3['A1'].value) # 获取A1单元格
print(ws3.cell(2,1).value) # 获取2行1列单元格,等价于A2
print(ws3.cell(2,1).row,ws3.cell(2,1).column) # 返回 1 A

"""
单元格区域获取
"""
wb4 = openpyxl.load_workbook("demo.xlsx")
ws4 = wb4.worksheets[0]

print(ws4['A1':'H2']) # 这是一个矩形区域,没有I1,返回每一行的对象的元组

print(ws4['1:3']) # 从1行到3行,会把工作表使用过的单元格都获取,有I1

print(ws4['a:c']) # 从a列到c列,与按行同理

print(list(ws4.values)[0][2]) # values返回所有的单元格的数据,找到第1行第3列的数据

'''列表推导式'''
data_2 = [[cell.value for cell in row] for row in ws4] # 2维单元格区域推导式
# 数据结构 [[第一行的数据],[第二行的数据],...]

w = wb4["A1:A6"] # 1维单元格区域
data_1 = [cell[0].value for cell in w] # 获取1维单元格区域的列表推导式

for i in data_2:
    print(i) # 每一行的数据就是一个列表


"""
行列信息获取
"""
wb = openpyxl.load_workbook("demo.xlsx")
ws = wb.worksheets[0]

# 它们都是生成器，惰性求值，不能向后，只能向前
vs = ws.rows # 按行的方式取值的迭代器
vs_columns = ws.columns # 按列的方式取值的迭代器
# 可以用列表推导或者循环的方式来取值

for _ in range(5):
    # 手动调用__next__()方法，这不常用，旨在理解迭代器和for循环方法的原理
    x = vs.__next__()
    v = [cell.value for cell in x]
    print(v)

for row in vs:
    # row 是一行数据的对象
    # c是一个单元的数据
    print([c.value for c in row])

'''获取工作表的边界'''

# 获取最小行号
ws.min_row
# 最大行号
ws.max_row
# 最小列号
ws.min_column
# 最大列号
ws.max_column
print(f"cor:{ws.min_row}-{ws.max_row}\ncolumn:{ws.min_column}-{ws.max_column}")
print(f"总单元格的数量为：{(ws.max_column-ws.min_column+1)*{ws.max_row-ws.min_row+1}}")


"""
两种表示单元格坐标的转换问题
"""
wb = openpyxl.load_workbook("demo.xlsx")
ws = wb.worksheets[0]

list_data = list(ws.values) # 将所有数据全放在列表里面,好处是访问数据时可以减少频繁访问表格提升性能

def char(cell:str):
    try:
        row,col = openpyxl.utils.coordinate_to_tuple(cell.upper()) # 此方法可以将A1转换成row=1,col=1
        return list_data[row-1][col-1]
    except Exception:
        return None

print(ws.cell(2,1).row,ws3.cell(2,1).column) # 返回 1 A







