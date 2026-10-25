import os

"""文件/文件夹重命名"""
# os.rename(log_filename:str,nwe_filename:str) -> None
os.rename("小吉祥草王.png",r"D:\code\图片\纳西妲.png")
# 同时rename还能移动文件,在同磁盘下移动效率非常高,在D盘和G盘不同磁盘移动会报错

"""删除文件"""
'''与普通删除不同,一旦删除无法恢复,不能Ctrl+Z回来'''
# os.rename(filepath:str) -> None
os.remove("实验.txt")

"""创建文件夹"""
# os.mkdir(dirpath:str) -> None
os.mkdir()

"""删除文件夹"""
# os.rmdir(dirpath:str) -> None
os.rmdir()

"""获取当前目录路径"""
# os.getcwd() -> str
print(os.getcwd())

"""获取目录列表"""
# 不写东西默认获取当前文件的目录列表
# print(os.listdir(dirpath:str) -> list[str]
print(os.listdir("../"))   # 获取上一级的文件夹目录列表

"""打开文件夹"""
# os.scandir(dirpath:str) -> 迭代器对象,获取字符串路径可以用str()或者.path来获取
with os.scandir(r"D:\zzw_keli\Documents\照片") as f: # 不需要写访问模式
    for i in f:
        with open(i,'rb') as v:
            data = v.read()
            print(data)

# os.walk(dirpath:str) -> 生成器对象
with os.walk(r"G:\浏览器下载") as f:
    """os.walk()是生成器,遍历完值就消失,通常在它遍历完之前就执行要执行的操作"""
# 返回3个变量 (当前文件所在目录路径,文件夹名称,文件名称)
    for filepath,folders,file in f:
        """for循环每执行一次就会深入一次文件夹,它属于迭代器,有__next__()方法"""
        print(f"{filepath}\n{folders}\n{file}")

# os.listdir(dirpath:str) -> list[str] 返回一级目录下的文件名和文件夹名
for file in os.listdir(r"G:\浏览器下载"):
    """不会像上面的一样去穿透文件夹,打印当前目录"""
    print(file)
    if 'txt' in file:
        """只打印txt的文件"""
        '''最好用 if Path(file).suffix.upper(): 因为如果filename里有txt但格式不是txt也会执行if'''
        print(file)

"""判断路径是否存在"""
# os.path.exists(filepath:str) -> bool
os.path.exists()
# 存在返回True

"""获取文件大小"""
# os.path.getsize(文件路径) / 1024 / 1024   返回的单位是bit,除以1024则返回kb,再除1024返回mb,以此类推

"""获取文件创建时间"""
import time
create_time = os.path.getmtime("输入路径") # 获取时间戳
real_time = time.localtime(create_time) # 先转换,下面才能格式化时间
dt = time.strftime("%Y-%m-%d %H:%M",real_time) # 按一定格式输出时间字符串
print(dt)
'''比较时间大小'''
create_time = "2026-10-17 16:14"
time_array = time.strptime(dt,"%Y-%m-%d %H:%M") # 先反格式化
my_target_time = float(time.mktime(time_array)) # 再转换成时间戳
if my_target_time > create_time:
    """时间戳数字越大文件创建的时间就越晚"""
    """如果my_target_time大于2026-10-17 16:14就返回Turn"""
    '''可以筛选出文件'''


"""压缩文件"""
import zipfile
def zipf():
    z = zipfile.ZipFile("abc.zip",'w') # 打开压缩包,没有会自动创建,模式为写入
    for file in os.listdir("输入路径"): # 要放在压缩包里的文件的文件夹
        z.write(os.path.join("输入路径",file)) # 把文件压缩到压缩包文件夹里
        with open("abc.txt",'a',encoding="utf-8") as w: # 写入压缩清单
            w.write(file + '\n')
    z.close() # 最后需要关闭压缩包文件,防止泄露

def unzipf():
    """解压文件"""
    f = zipfile.ZipFile("abc.zip",'r') # 先打开压缩包,文件为只读模式,没要文件会报错
    for file in f.namelist():
        '''返回列表对象给file'''
        f.extract(file,"MYunzip/") # f.extract(解压缩谁,解压缩到哪)

"""复制文件需要导入库"""
import shutil
'''小项目使用这种方法'''
# os.makedirs(dirpath:str) -->接收路径,不是文件对象
# shutil.copy2(filepath:str) -->接收路径,不是文件对象
# shutil.copy(filepath:str) 与 shutil.copy2的区别:前者只复制数据和权限,后者复制数据和全部(包括修改时间等原数据)
os.makedirs(r"D:\py文件夹\纳西妲",exist_ok=True) # 建造仓库
shutil.copy2(r"G:\浏览器下载\纳西妲.jfif",r"D:\py文件夹\纳西妲.jfif") # 搬进仓库
'''针对大文件(性能优化)'''
# 分块读取(流式复制)
# shutil.copyfileobj() -->接收文件对象,不是路径
def copy_large_file(src,dst,buffer_size=1024*1024): # 1MB缓存区
    with open(src,'rb') as f,open(dst,'wb') as g:
        shutil.copyfileobj(f,g,length=buffer_size)
copy_large_file(r"G:\浏览器下载\纳西妲.jfif",r"D:\py文件夹\纳西妲.jfif")

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
