from datetime import datetime

def main():
    responses = {}  # 格式: {用户名: [{"answer": str, "timestamp": str}, ...]}
    is_running = True
    
    print("=== 调查系统启动 ===")
    print("提示：输入'是'开始录入，'否'结束调查\n")
    
    while is_running:
        choice = input('是否愿意参加此次调查？(是/否): ').strip()
        
        if choice == '是':
            name = input('请输入你的名字: ').strip()
            if not name:
                print("⚠️ 名字不能为空，请重新输入\n")
                continue
            
            answer = input('请输入你的回答: ').strip()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # 创建新记录
            new_record = {
                "answer": answer,
                "timestamp": timestamp
            }
            
            # 追加到对应用户的列表中（避免覆盖）
            if name not in responses:
                responses[name] = []
            responses[name].append(new_record)
            
            print(f"✅ 记录成功！当前共有 {len(responses)} 位参与者，{sum(len(v) for v in responses.values())} 条记录\n")
        
        elif choice == '否':
            print("\n=== 调查结果汇总 ===")
            if not responses:
                print("暂无调查数据")
            else:
                for name, records in responses.items():
                    print(f"\n👤 用户: {name}")
                    for i, record in enumerate(records, 1):
                        print(f"  {i}. 回答: {record['answer']} | 时间: {record['timestamp']}")
                print(f"\n总计: {len(responses)} 位参与者，{sum(len(v) for v in responses.values())} 条记录")
            is_running = False
        
        else:
            print("❌ 输入无效，请重新输入'是'或'否'\n")

if __name__ == "__main__":
    main()
