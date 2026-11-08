import requests
import json


URL = "https://api.deepseek.com/chat/completions"
txt = input()
# with open(r"大模型API教程\dpkey.json",'r',encoding="utf-8") as f:
#     char = json.load(f)
#     char["content"] = txt

# with open(r"大模型API教程\dpkey.json",'w',encoding="utf-8") as f:
#     json.dump(char,f,ensure_ascii=False,indent=4)

with open(r"大模型API教程\dpkey.json",'r',encoding="utf-8") as f:
    look = json.load(f)
API_KEY = look["API_KEY"]

headers = {
    "Authorization": f"Bearer {API_KEY}",# 注意⚠️apikey前面有一个空格
    "Content-Type": "application/json"
}

messages = [
    {"role":"system", "content":"你是一个乐于助人的AI助手"},
    {"role":"user","content":txt},
]

payload = {
    "model":"deepseek-flash",
    "max_tokens":3000,
}
payload["messages"] = messages

                # 请求头：包含apikey和返回信息   # 把参数放在json里面
r = requests.post(URL,headers=headers,json=payload)
print(f"状态码：{r.status_code}")
data = r.json()
with open(r"大模型API教程\dptokens.json",'a',encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False,indent=4)
