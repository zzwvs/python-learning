import requests
import os
import json

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept":"application/vnd.github.v3+json"}

        # 请求的网址  请求的头部信息(补充说名)
r = requests.get(url,headers=headers)
# 这是响应对象(r)
print(f"响应状态码:{r.status_code}") # 200 意味着请求成功,404 没有找到服务器 一般是网址写错了
# r.text 是json字符串,将其转换为字典
response_dict = r.json()


# 查看第一层 key
print(response_dict.keys())
print(f"总仓库数:{response_dict['total_count']}")
print(f"是否全部:{not response_dict['incomplete_results']}")
print(f"仓库数量:{len(response_dict['items'])}")

repos_dict = response_dict["items"][0]
print(f"每个仓库有{len(repos_dict)}个key,即信息项")

print(f"仓库地址:{repos_dict['html_url']}")



res = requests.get(url,timeout=0.0001) # 超出这个时间如果没有返回数据,就不等服务器响应了,直接抛出异常

# 处理异常

try:
    res = requests.get(url,timeout=30)
    print(res.status_code)
    print(res.json())
except requests.exceptions.Timeout: # 模块里的异常处理
    print("请求超时!")



