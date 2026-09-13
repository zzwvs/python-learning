import tkinter as tk
from tkinter import scrolledtext, messagebox, Menu
from datetime import datetime
import json
import os

# 尝试导入 ttkbootstrap 进行美化，如果没有安装则回退到普通主题
try:
    import ttkbootstrap as ttk
    from ttkbootstrap.constants import *
    BOOTSTRAP_AVAILABLE = True
except ImportError:
    import tkinter.ttk as ttk
    BOOTSTRAP_AVAILABLE = False
    # 定义一些常量以防报错（如果是普通tkinter模式）
    SUCCESS = "success"
    DANGER = "danger"
    PRIMARY = "primary"
    WARNING = "warning"

DATA_FILE = "survey_data.json"


class SurveyApp:
    def __init__(self, root):
        self.root = root

        # 1. 窗口初始化与主题设置
        if BOOTSTRAP_AVAILABLE:
            self.root.title("✨ 现代化调查录入系统")
            self.style = ttk.Style(theme="cosmo")  # 使用 cosmo 主题，清新风格
            self.root.geometry("600x650")
        else:
            self.root.title("调查录入系统 (普通模式)")
            self.root.geometry("520x520")

        self.root.resizable(False, False)

        # 2. 数据加载 (持久化)
        self.responses = self.load_data()

        # 3. 构建 UI
        self._build_ui()
        self._update_stats()  # 初始化时更新统计信息

        # 4. 绑定关闭窗口事件，确保退出时保存
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def load_data(self):
        """从 JSON 文件加载数据"""
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                messagebox.showerror("错误", f"读取数据文件失败: {e}")
                return {}
        return {}

    def save_data(self):
        """保存数据到 JSON 文件"""
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(self.responses, f, ensure_ascii=False, indent=4)
            return True
        except Exception as e:
            messagebox.showerror("错误", f"保存数据失败: {e}")
            return False

    def on_closing(self):
        """关闭窗口时的处理"""
        if self.save_data():
            self.root.destroy()

    def _build_ui(self):
        # --- 标题区域 ---
        title_font = ("微软雅黑", 16, "bold")
        if BOOTSTRAP_AVAILABLE:
            ttk.Label(self.root, text="📝 调查问卷录入", font=title_font, bootstyle=PRIMARY).pack(pady=15)
        else:
            ttk.Label(self.root, text="=== 调查问卷录入 ===", font=title_font).pack(pady=15)

        # --- 输入区域 (使用 Labelframe 包裹更美观) ---
        input_frame = ttk.LabelFrame(self.root, text="录入信息")
        input_frame.pack(pady=5, fill="x", padx=20)

        # 姓名
        name_row = ttk.Frame(input_frame)
        name_row.pack(fill="x", padx=10, pady=5)
        ttk.Label(name_row, text="姓名：", width=6).pack(side="left")
        self.name_entry = ttk.Entry(name_row)
        self.name_entry.pack(side="left", fill="x", expand=True)

        # 回答
        ans_row = ttk.Frame(input_frame)
        ans_row.pack(fill="x", padx=10, pady=5)
        ttk.Label(ans_row, text="回答：", width=6).pack(side="left")
        self.answer_entry = ttk.Entry(ans_row)
        self.answer_entry.pack(side="left", fill="x", expand=True)
        # 绑定回车键提交
        self.answer_entry.bind("<Return>", lambda event: self.submit_record())

        # --- 按钮区域 ---
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)

        btn_style_submit = SUCCESS if BOOTSTRAP_AVAILABLE else None
        btn_style_end = DANGER if BOOTSTRAP_AVAILABLE else None

        ttk.Button(btn_frame, text="提交记录", width=12, command=self.submit_record, bootstyle=btn_style_submit).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="结束/刷新", width=12, command=self.end_survey, bootstyle=btn_style_end).pack(side="left", padx=5)

        # --- 统计信息 ---
        self.stat_label = ttk.Label(self.root, text="当前：0 位参与者，0 条记录", font=("微软雅黑", 9), foreground="#666")
        self.stat_label.pack(pady=2)

        self.status_label = ttk.Label(self.root, text="", font=("微软雅黑", 9), foreground="#2196F3")
        self.status_label.pack(pady=2)

        # --- 结果展示区 (带右键菜单) ---
        result_frame = ttk.LabelFrame(self.root, text="数据详情 (右键可编辑/删除)")
        result_frame.pack(pady=(10, 0), fill="both", expand=True, padx=20)

        self.result_text = scrolledtext.ScrolledText(result_frame, width=60, height=15, font=("Consolas", 10), state="disabled")
        self.result_text.pack(fill="both", expand=True)

        # 创建右键菜单
        self.context_menu = Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="✏️ 编辑此条记录", command=self.edit_selected_record)
        self.context_menu.add_command(label="🗑️ 删除此条记录", command=self.delete_selected_record)

        # 绑定右键事件
        self.result_text.bind("<Button-3>", self.show_context_menu)

    def show_context_menu(self, event):
        """显示右键菜单"""
        try:
            # 获取点击位置的索引
            index = self.result_text.index(f"@{event.x},{event.y}")
            # 简单的判断逻辑：检查点击的行是否包含 "回答：" 关键字，防止在空白处或标题处弹出
            line_content = self.result_text.get(f"{index} linestart", f"{index} lineend")

            if "回答：" in line_content or "时间：" in line_content:
                # 存储当前选中的行索引，用于后续定位数据
                self.selected_line_index = index
                self.context_menu.post(event.x_root, event.y_root)
            else:
                pass # 点击了无关区域，不显示菜单
        except Exception:
            pass

    def _update_stats(self):
        total_people = len(self.responses)
        total_records = sum(len(v) for v in self.responses.values())
        self.stat_label.config(text=f"📊 统计：{total_people} 位参与者 | {total_records} 条总记录")

    def submit_record(self):
        name = self.name_entry.get().strip()
        answer = self.answer_entry.get().strip()

        if not name:
            messagebox.showwarning("提示", "名字不能为空，请重新输入")
            self.name_entry.focus()
            return
        if not answer:
            messagebox.showwarning("提示", "回答内容不能为空")
            self.answer_entry.focus()
            return

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_record = {
            "answer": answer,
            "timestamp": timestamp
        }

        if name not in self.responses:
            self.responses[name] = []
        self.responses[name].append(new_record)

        # 自动保存
        self.save_data()

        # 更新 UI
        self._update_stats()
        self.status_label.config(text="✅ 记录已保存")
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.focus()  # 保持焦点在回答框，方便连续录入

    def end_survey(self):
        """刷新并展示所有结果"""
        self.result_text.config(state="normal")
        self.result_text.delete("1.0", tk.END)

        if not self.responses:
            self.result_text.insert(tk.END, "暂无调查数据\n")
        else:
            for name, records in self.responses.items():
                self.result_text.insert(tk.END, f"\n👤 用户：{name}\n", "header")
                for i, record in enumerate(records):
                    # 给每一行添加 Tag，方便后续定位（这里简单处理，实际可以通过行号计算）
                    self.result_text.insert(tk.END, f"   {i+1}. 回答：{record['answer']}\n")
                    self.result_text.insert(tk.END, f"      时间：{record['timestamp']}\n\n")

        self.result_text.config(state="disabled")
        self.status_label.config(text="🔄 列表已刷新")

    # --- 新增：编辑与删除逻辑 ---

    def _find_record_by_visual_index(self, target_line_idx):
        """
        根据文本框的大致行号，反查对应的数据结构。
        这是一个简化的查找逻辑，通过遍历文本内容来匹配。
        """
        # 获取从开始到点击行的所有内容
        content_up_to_click = self.result_text.get("1.0", f"{target_line_idx} lineend")
        lines = content_up_to_click.split('\n')

        current_name = None
        last_answer_idx = -1

        # 向上回溯寻找最近的一个 "用户：" 和 "回答："
        for i in range(len(lines) - 1, -1, -1):
            line = lines[i]
            if "👤 用户：" in line:
                current_name = line.split("👤 用户：")[1].strip()
                break

        if not current_name:
            return None, None, None

        # 找到该用户下的具体是哪一条回答
        # 重新遍历该用户下的记录来匹配文本
        user_records = self.responses.get(current_name, [])
        
        # 获取点击行的纯文本内容用于匹配
        clicked_line_text = self.result_text.get(f"{target_line_idx} linestart", f"{target_line_idx} lineend").strip()
        
        # 如果点击的是时间行，往上找一行作为回答行
        if "时间：" in clicked_line_text:
             prev_line = self.result_text.get(f"{target_line_idx}-1l linestart", f"{target_line_idx}-1l lineend").strip()
             # 提取回答内容
             answer_content = prev_line.replace(f"{len(user_records)}. 回答：", "").replace("回答：", "").strip() 
             # 注意：这里的序号匹配比较脆弱，更好的方式是依靠完全匹配内容
        elif "回答：" in clicked_line_text:
             answer_content = clicked_line_text.replace("回答：", "").strip()
             # 去除前面的序号 "1. ", "10. " 等
             if ". " in answer_content:
                 answer_content = answer_content.split(". ", 1)[1]
        else:
            return None, None, None

        # 在数据中查找匹配的记录
        for idx, record in enumerate(user_records):
            if record['answer'] == answer_content:
                return current_name, idx, record
        
        return None, None, None

    def delete_selected_record(self):
        name, idx, record = self._find_record_by_visual_index(self.selected_line_index)
        if name and idx is not None:
            if messagebox.askyesno("确认删除", f"确定要删除 {name} 的这条记录吗？\n内容：{record['answer']}"):
                del self.responses[name][idx]
                if not self.responses[name]:
                    del self.responses[name]
                self.save_data()
                self.end_survey() # 刷新视图
                self._update_stats()
                messagebox.showinfo("成功", "记录已删除")
        else:
            messagebox.showwarning("错误", "无法定位要删除的记录，请刷新后重试")

    def edit_selected_record(self):
        name, idx, record = self._find_record_by_visual_index(self.selected_line_index)
        if name and idx is not None:
            # 弹出编辑窗口
            edit_win = tk.Toplevel(self.root)
            edit_win.title("编辑记录")
            edit_win.geometry("300x150")
            
            ttk.Label(edit_win, text=f"用户：{name}").pack(pady=5)
            
            entry_var = tk.StringVar(value=record['answer'])
            new_entry = ttk.Entry(edit_win, textvariable=entry_var, width=30)
            new_entry.pack(pady=5)
            new_entry.focus()

            def save_edit():
                new_ans = entry_var.get().strip()
                if new_ans:
                    self.responses[name][idx]['answer'] = new_ans
                    self.save_data()
                    self.end_survey()
                    edit_win.destroy()
                    messagebox.showinfo("成功", "修改已保存")
                else:
                    messagebox.showwarning("提示", "内容不能为空")

            ttk.Button(edit_win, text="保存修改", command=save_edit, bootstyle=SUCCESS if BOOTSTRAP_AVAILABLE else None).pack(pady=10)
        else:
            messagebox.showwarning("错误", "无法定位要编辑的记录")


if __name__ == "__main__":
    root = tk.Tk()
    app = SurveyApp(root)
    root.mainloop()
    