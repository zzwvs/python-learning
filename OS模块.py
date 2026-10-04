import os

"""文件/文件夹重命名"""
# os.rename(旧名字,新名字)
# os.rename("小吉祥草王.png",r"D:\code\图片\纳西妲.png")
# 同时rename还能移动文件,在同磁盘下移动效率非常高,在D盘和G盘不同磁盘移动会报错

"""删除文件"""
# os.remove()test.txt
# os.rename("实验.txt")

"""创建文件夹"""
# os.mkdir()
# os.mkdir()

"""删除文件夹"""
# os.rmdir()
# os.rmdir()

"""获取当前目录路径"""
# os.getcwd()
# print(os.getcwd())

"""获取目录列表"""
# 不写东西默认获取当前文件的目录列表
# print(os.listdir(r"D:\py临时项目"))
# print(os.listdir("../"))   # 获取上一级的文件夹目录列表

"""打开文件夹"""
# os.scandir()
# with os.scandir(r"D:\zzw_keli\Documents\照片") as f: # 不需要写访问模式
#     for i in f:
#         with open(i,'rb') as v:
#             data = v.read()
#             print(data)

"""复制文件需要导入库"""
import shutil
'''小项目使用这种方法'''
# os.makedirs() -->接收路径,不是文件对象
# shutil.copy2 -->接收路径,不是文件对象
# shutil.copy() 与 shutil.copy2的区别:前者只复制数据和权限,后者复制数据和全部(包括修改时间等原数据)
# os.makedirs(r"D:\py文件夹\纳西妲",exist_ok=True) # 建造仓库
# shutil.copy2(r"G:\浏览器下载\纳西妲.jfif",r"D:\py文件夹\纳西妲.jfif") # 搬进仓库
'''针对大文件(性能优化)'''
# 分块读取(流式复制)
# shutil.copyfileobj() -->接收文件对象,不是路径
# def copy_large_file(src,dst,buffer_size=1024*1024): # 1MB缓存区
#     with open(src,'rb') as f,open(dst,'wb') as g:
#         shutil.copyfileobj(f,g,length=buffer_size)
# copy_large_file(r"G:\浏览器下载\纳西妲.jfif",r"D:\py文件夹\纳西妲.jfif")

"""Path模块"""
from pathlib import Path
S_dir = r"G:\浏览器下载"    # 起始文件夹夹
F_dir = r"D:\code\图片"     # 目标文件夹
with os.scandir(S_dir) as x,os.scandir(F_dir) as y:
    '''os.scandir() 打开文件夹不需要写访问模式'''
    for i in x:
        # data = Path(i.path) # i.Path() 返回文件的完整路径
        if os.path.isdir(i.path): # 仅处理文件,跳过子目录
            continue
        F = os.path.join(S_dir,i.name)
        with open(i.path,"rb") as s,open(F,"wb") as f:
            shutil.copyfileobj(s,f,1024*1024)
