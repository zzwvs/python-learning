import requests
# import os
import json
with open(r"大模型API教程\test.json",'r',encoding="utf-8") as f:
    look = json.load(f)

API_KEY = look["API_KEY"]
# API_KEY = os.getenv("API_KEY")  # 从环境变量读取
BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
CHAT_COMPLETION_URL = f"{BASE_URL}/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",   # ← 加了空格
    "Content-Type": "application/json"
}

messages = [
    {"role": "system",    "content": "你是一个乐于助人的ai助手"},
    {"role": "user",      "content": look["txt"]},
#     {"role": "assistant", "content": "大模型是一种基于海量数据训练的大型人工智能模型"},
#     {"role": "user",      "content": "它和不同机器学习有什么区别"}
]

payload = {
    "model":       "qwen3.8-max",
    "messages":    messages,
    "temperature": 0.7,
    "max_tokens":  512,
    "stream":      False
}

try:
    response = requests.post(CHAT_COMPLETION_URL, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    result = response.json()
    with open("demo.json",'w',encoding="utf-8") as f:
        json.dump(result,f,ensure_ascii=False,indent=4)
    print(result["choices"][0]["message"]["content"])   # ← 修正取值路径
except requests.exceptions.RequestException as e:
    print(f"请求异常: {e}")