import requests

URL = r"https://uapis.cn/api/v1/misc/hotboard"

type_data = {
    1:["bilibili","哔哩哔哩"],
    2:["weibo","新浪微博"],
    3:["zhihu","知乎"],
    4:["douyin","抖音"],
    5:["xiaohongshu","小红书"],
    6:["toutiao","今日头条"],
    7:["qq-news","腾讯新闻"],
    8:["genshin","原神"]
}

print("欢迎使用我的热点新闻搜索程序")

print("请选择你想要使用的搜索引擎")
for k,v in type_data.items():
    print(f"输入{k}  使用{v[1]}搜索")

e = int(input().strip())

hea = {}
hea["type"] = type_data[e][0]

URL += f"?type={hea['type']}"

r = requests.get(url=URL,timeout=5)
if r.status_code == 200:
    data = r.json() 
    print(f"搜索平台:{hea['type']}")
    print(f"总新闻数量{len(data["list"])}")
    for dic in data["list"]:
        print(f"{dic["title"]}")
        print(f"{dic["url"]}")
        print("\n")
else:
    print(f"响应状态码: {r.status_code}")

input("按回车键退出...")



