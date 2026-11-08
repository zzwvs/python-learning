import requests
URL = "https://api.pearapi.ai/api/brainteasers/"
def main():
    while True:
        print("正在生成题目,请稍候...")
        r = requests.get(url=URL)
        print(r.status_code)
        js_data = r.json()
        print("请听题:")
        print(js_data["data"]["question"])
        input("按回车键查看答案")
        print("答案是:")
        print(js_data["data"]["answer"])
        input("按回车键继续猜")

if __name__ == "__main__":
    main()